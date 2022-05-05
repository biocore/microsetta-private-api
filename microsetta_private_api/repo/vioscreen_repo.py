import pandas as pd
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenPercentEnergy,
    VioscreenPercentEnergyComponent,
    VioscreenDietaryScore, VioscreenDietaryScoreComponent,
    VioscreenSupplements, VioscreenSupplementsComponent,
    VioscreenFoodComponents, VioscreenFoodComponentsComponent,
    VioscreenEatingPatterns, VioscreenEatingPatternsComponent,
    VioscreenMPeds, VioscreenMPedsComponent,
    VioscreenFoodConsumption, VioscreenFoodConsumptionComponent,
    VioscreenComposite)
from werkzeug.exceptions import NotFound


class VioscreenSessionRepo(BaseRepo):
    COLS = ["sessionId", "username", "protocolId", "status",
            "startDate", "endDate", "cultureCode", "created",
            "modified"]

    @property
    def _sql_cols(self):
        return ', '.join(self.COLS)

    def __init__(self, transaction):
        super().__init__(transaction)

    def upsert_session(self, session):
        """Insert or update a vioscreen session

        Parameters
        ----------
        session : VioscreenSession
            The session object to insert or update

        Returns
        -------
        bool
            True if something was updated or inserted
        """
        # upsert based off of https://stackoverflow.com/a/36799500/19741
        with self._transaction.cursor() as cur:
            doupdateset = ["%s = EXCLUDED.%s" % (a, a) for a in self.COLS
                           if a not in ('sessionId', 'username')]
            doupdateset = ','.join(doupdateset)

            cur.execute(f"""INSERT INTO ag.vioscreen_sessions (
                               {self._sql_cols}
                               )
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                           ON CONFLICT (sessionId)
                           DO UPDATE SET
                               {doupdateset}
                           """,
                        tuple([getattr(session, attr) for attr in self.COLS]))
            return cur.rowcount == 1

    def get_session(self, sessionId):
        """Obtain a session model for a sessionId

        Parameters
        ----------
        sessionId : str
            The session ID to retrieve

        Returns
        -------
        VioscreenSession or None
            An instance of a VioscreenSession model or None if a session
            was not found
        """
        with self._transaction.cursor() as cur:
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions
                            WHERE sessionId = %s""",
                        (sessionId, ))
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return VioscreenSession(*row)

    def get_sessions_by_username(self, username):
        """Obtain all sessions associated with a username

        Parameters
        ----------
        username : str
            The username to search for

        Returns
        -------
        list of VioscreenSession, or None
            Instances of the observed vioscreen sessions or None if the
            username was not found
        """
        with self._transaction.cursor() as cur:
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions
                            WHERE username = %s""",
                        (username, ))
            rows = cur.fetchall()

            # TODO: test if we can add a unique constraint
            # on username
            if len(rows) == 0:
                return None
            else:
                return [VioscreenSession(*row) for row in rows]

    def get_unfinished_sessions(self):
        """Obtain the sessions for that appear incomplete

        An incomplete session is one that meets any of the following criteria:

        1) the ag.vioscreen_registry.vio_id does not exist in the
           ag.vioscreen_sessions table
        2) the ag.vioscreen_sessions.endDate is null
        3) the ag.vioscreen_sessions.status is not "Finished"

        In the event a user has multiple sessions:

        * if ALL sessions are incomplete, all sessions will be returned
        * if ANY session is complete, no sessions will be returned

        The operating model for AG/TMI has been a single session per vioscreen
        username (i.e., vio_id). As such, *if* a vioscreen vio_id has multiple
        sessions associated with it, we do not actually know right now how to
        appropriately handle a scenario where *multiple* sessions are finished.

        Returns
        -------
        list of VioscreenSession
            In the event of criteria (1) noted above, only the username
            attribute of an instance will be not None
        """
        with self._transaction.cursor() as cur:
            # criteria 1, vio_ids which are not in vioscreen_sessions
            cur.execute("""SELECT distinct(vio_id)
                           FROM ag.vioscreen_registry
                           WHERE vio_id NOT IN (
                               SELECT distinct(username)
                               FROM ag.vioscreen_sessions)""")
            not_in_vioscreen_sessions = [VioscreenSession.from_registry(u[0])
                                         for u in cur.fetchall()]

            # criteria 2 and 3
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions""")

            # array_agg doesn't work over these datatypes... ugh. this
            # almost certainly could be done better directly within SQL
            # but another problem for another day
            records = pd.DataFrame(cur.fetchall(), columns=self.COLS)
            incomplete_sessions = []
            for user, rows in records.groupby('username'):
                sessions = rows.apply(lambda row: VioscreenSession(*row),
                                      axis=1)
                are_incomplete = [not s.is_complete for s in sessions]
                if all(are_incomplete):
                    incomplete_sessions.extend(sessions)

            return not_in_vioscreen_sessions + incomplete_sessions

    def get_ffq_status_by_sample(self, sample_uuid):
        """Obtain the FFQ status for a given sample

        Parameters
        ----------
        sample_uuid : UUID4
            The UUID to check the status of

        Returns
        -------
        (bool, bool, str or None)
            The first index if True indicates the FFQ is completed.
            The second index if True indicates the FFQ has been started,
                but may or may not be completed.
            The third index is the exact status from Vioscreen, or None
                if there is no FFQ associated with the sample.
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT status
                           FROM ag.vioscreen_sessions AS vs
                           JOIN ag.vioscreen_registry AS vr
                               ON vs.username=vr.vio_id
                           WHERE sample_id=%s""", (sample_uuid, ))
            res = cur.fetchall()
            if len(res) == 0:
                return (False, False, None)
            elif len(res) == 1:
                status = res[0][0]
                is_complete = status == 'Finished'
                is_taken = status in ('Started', 'Review', 'Finished')
                return (is_complete, is_taken, status)
            else:
                raise ValueError("A sample should not have multiple FFQs")

    def get_missing_ffqs(self):
        """The set of valid sessions which lack FFQ data

        An valid session but missing session is one that meets
        the following criteria:

        1) the ag.vioscreen_sessions entry is "Finished"
        2) the ag.vioscreen_sessions entry endDate is not null
        3) the sessionId is not present in one of the vioscreen FFQ
           decomposed tables

        Returns
        -------
        list of VioscreenSession
            The missing sessions
        """
        with self._transaction.cursor() as cur:
            # criteria 1 and 2, check endDate and status
            cur.execute("""SELECT sessionid
                           FROM ag.vioscreen_sessions
                           WHERE endDate IS NOT NULL
                               AND status = 'Finished'""")
            complete_sessions = {i[0] for i in cur.fetchall()}

            # criteria 3, determine sessions which we have ffq data for
            cur.execute("""SELECT distinct(sessionid)
                           FROM ag.vioscreen_percentenergy""")
            sessions_with_data = {i[0] for i in cur.fetchall()}

            sessions_without_data = complete_sessions - sessions_with_data

            without_data = []
            if sessions_without_data:
                # construct session objects for all of our missing sessions
                cur.execute(f"""SELECT {self._sql_cols}
                                FROM ag.vioscreen_sessions
                                  WHERE sessionId IN %s""",
                            (tuple(sessions_without_data), ))
                for row in cur.fetchall():
                    without_data.append(VioscreenSession(*row))

        return without_data


class VioscreenPercentEnergyRepo(BaseRepo):
    # code : (long description, short description, units)
    _CODES = {'%mfatot': ('Percent of calories from Monounsaturated Fat',
                          'Monounsaturated Fat', '%'),
              '%pfatot': ('Percent of calories from Polyunsaturated Fat',
                          'Polyunsaturated Fat', '%'),
              '%carbo': ('Percent of calories from Carbohydrate',
                         'Carbohydrate', '%'),
              '%sfatot': ('Percent of calories from Saturated Fat',
                          'Saturated Fat', '%'),
              '%alcohol': ('Percent of calories from Alcohol', 'Alcohol', '%'),
              '%protein': ('Percent of calories from Protein', 'Protein', '%'),
              '%adsugtot': ('Percent of calories from Added Sugar',
                            'Added Sugar', '%'),
              '%fat': ('Percent of calories from Fat', 'Fat', '%')}

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_percent_energy(self, vioscreen_percent_energy):
        """Add percent energy data for a session

        Parameters
        ----------
        vioscreen_percent_energy : VioscreenPercentEnergy
            The observed percent energy data

        Returns
        -------
            Returns number of rows modified
        """
        with self._transaction.cursor() as cur:
            energy_components = vioscreen_percent_energy.energy_components
            inserts = []
            for energy_component in energy_components:
                # checking if code exists in lookup
                self._get_code_info(energy_component.code)
                inserts.append((vioscreen_percent_energy.sessionId,
                                energy_component.code,
                                energy_component.amount))

            cur.executemany("""INSERT INTO ag.vioscreen_percentenergy
                                (sessionId, code, amount)
                                VALUES (%s, %s, %s)""",
                            inserts)
            return cur.rowcount

    def get_percent_energy(self, sessionId):
        """Obtain the percent energy data for a sessionId

        Parameters
        ----------
        sessionId : str
            The session ID to retrieve data for

        Returns
        -------
        VioscreenPercentEnergy or None
            The observed percent energy data or None if the session ID is
            invalid
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_percentenergy
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for code, amount in rows:
                    codeInfo = self._get_code_info(code)
                    vpec = VioscreenPercentEnergyComponent(code=code,
                                                           description=codeInfo[0],  # noqa
                                                           short_description=codeInfo[1],  # noqa
                                                           units=codeInfo[2],
                                                           amount=amount)
                    components.append(vpec)
                return VioscreenPercentEnergy(sessionId=sessionId,
                                              energy_components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular energy component by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The description, short description and units for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        if code not in self._CODES:
            raise NotFound("No such code: " + code)

        return self._CODES[code]


class VioscreenDietaryScoreRepo(BaseRepo):
    # scoresType : { code: (name, lower limit, upper limit) }
    _CODES = {
        'Hei2010': {
            'TotalVegetables': ('Total Vegetables', 0.0, 5.0),
            'GreensAndBeans': ('Greens and Beans', 0.0, 5.0),
            'TotalFruit': ('Total Fruit', 0.0, 5.0),
            'WholeFruit': ('Whole Fruit', 0.0, 5.0),
            'WholeGrains': ('Whole Grains', 0.0, 10.0),
            'Dairy': ('Dairy', 0.0, 10.0),
            'TotalProteins': ('Total Protein Foods', 0.0, 5.0),
            'SeafoodAndPlantProteins': ('Seafood and Plant Proteins',
                                        0.0, 5.0),
            'FattyAcids': ('Fatty Acids', 0.0, 10.0),
            'RefinedGrains': ('Refined Grains', 0.0, 10.0),
            'Sodium': ('Sodium', 0.0, 10.0),
            'EmptyCalories': ('Empty Calories', 0.0, 20.0),
            'TotalScore': ('Total HEI Score', 0.0, 100.0)},
        'Hei2015': {
            'TotalVegetables': ('Total Vegetables', 0.0, 5.0),
            'GreensAndBeans': ('Greens and Beans', 0.0, 5.0),
            'TotalFruit': ('Total Fruit', 0.0, 5.0),
            'WholeFruit': ('Whole Fruit', 0.0, 5.0),
            'WholeGrains': ('Whole Grains', 0.0, 10.0),
            'Dairy': ('Dairy', 0.0, 10.0),
            'TotalProteins': ('Total Protein Foods', 0.0, 5.0),
            'SeafoodAndPlantProteins': ('Seafood and Plant Proteins',
                                        0.0, 5.0),
            'FattyAcids': ('Fatty Acids', 0.0, 10.0),
            'RefinedGrains': ('Refined Grains', 0.0, 10.0),
            'Sodium': ('Sodium', 0.0, 10.0),
            'SaturatedFat': ('SaturatedFat', 0.0, 10.0),
            'AddedSugars': ('AddedSugars', 0.0, 10.0),
            'TotalScore': ('Total HEI Score', 0.0, 100.0)},
        }

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_dietary_scores(self, vioscreen_dietary_scores):
        """Add in dietary score results for a session

        Parameters
        ----------
        vioscreen_dietary_scores : list of VioscreenDietaryScore
            Dietary score models to insert

        Returns
        -------
        int
            The number of inserted rows
        """
        count = 0
        with self._transaction.cursor() as cur:
            for model in vioscreen_dietary_scores:
                scores = model.scores
                inserts = []
                for score in scores:
                    # checking if code exists in lookup
                    self._get_code_info(model.scoresType, score.code)
                    inserts.append((model.sessionId,
                                    model.scoresType,
                                    score.code,
                                    score.score))

                cur.executemany("""INSERT INTO ag.vioscreen_dietaryscore
                                    (sessionId, scoresType, code, score)
                                    VALUES (%s, %s, %s, %s)""",
                                inserts)
                count += cur.rowcount
        return count

    def get_dietary_scores(self, sessionId):
        """Obtain the dietary score detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        list of VioscreenDietaryScore or None
            The dietary score detail, or None if no record was found
        """
        sql = """SELECT scoresType, code, score
                 FROM ag.vioscreen_dietaryscore
                 WHERE sessionId = %s"""
        df = pd.read_sql(sql, self._transaction.conn, params=(sessionId, ))

        if len(df) == 0:
            return None

        scores = []
        # note the header is cast to lowerase
        for type_, grp in df.groupby('scorestype'):
            components = []
            for _, row in grp.iterrows():
                code = row['code']
                score = row['score']
                codeInfo = self._get_code_info(type_, code)
                vdsc = VioscreenDietaryScoreComponent(code=code,
                                                      name=codeInfo[0],
                                                      score=score,
                                                      lowerLimit=codeInfo[1],
                                                      upperLimit=codeInfo[2])
                components.append(vdsc)

            scores.append(VioscreenDietaryScore(sessionId=sessionId,
                                                scoresType=type_,
                                                scores=components))
        return scores

    def _get_code_info(self, scoresType, code):
        """Obtain the detail about a particular score type by its code

        Parameters
        ----------
        scoresType : str
            The score type (e.g. Hei2010) to obtain detail for
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The name, lower and upper limit for a particular code
            and score type

        Raises
        ------
        NotFound
            A NotFound error is raised if the code or score type are
            unrecognized
        """
        if scoresType not in self._CODES:
            raise NotFound("No such scoresType: " + scoresType)

        scores = self._CODES[scoresType]
        if code not in scores:
            raise NotFound("No such code: " + code)

        return scores[code]

    def get_dietary_scores_by_component(self, scoresType, code):
        """Obtain the all the dietary scores for a particular component
        Parameters
        ----------
        scoresType : str
            The scoresType to query
        code : str
            The code to query
        Returns
        -------
        Float Array or None
            The dietary scores, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT score
                           FROM ag.vioscreen_dietaryscore
                           WHERE scoresType = %s AND code = %s""",
                        (scoresType, code))

            rows = cur.fetchall()
            if len(rows) > 0:
                scores = []
                for score in rows:
                    scores.append(score[0])
                return scores

            else:
                return None

    def get_dietary_scores_descriptions(self):
        return self._CODES


class VioscreenSupplementsRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_supplements(self, vioscreen_supplements):
        """Add in supplement results for a session

        Parameters
        ----------
        vioscreen_supplements : VioscreenSupplements
            An instance of a supplements model

        Returns
        -------
        int
            The number of inserted rows
        """
        with self._transaction.cursor() as cur:
            components = vioscreen_supplements.supplements_components
            inserts = [(vioscreen_supplements.sessionId,
                        component.supplement,
                        component.frequency,
                        component.amount,
                        component.average)
                       for component in components]

            cur.executemany("""INSERT INTO ag.vioscreen_supplements
                                (sessionId, supplement, frequency,
                                 amount, average)
                                VALUES (%s, %s, %s, %s, %s)""",
                            inserts)
            return cur.rowcount

    def get_supplements(self, sessionId):
        """Obtain the supplement detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        VioscreenSupplements or None
            The supplements detail, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT supplement, frequency, amount, average
                           FROM ag.vioscreen_supplements
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for row in rows:
                    vsc = VioscreenSupplementsComponent(supplement=row[0],
                                                        frequency=row[1],
                                                        amount=row[2],
                                                        average=row[3])
                    components.append(vsc)
                return VioscreenSupplements(sessionId=sessionId,
                                            supplements_components=components)
            else:
                return None


class VioscreenFoodComponentsRepo(BaseRepo):
    # code : (description, units, valueType)
    _CODES = {'acesupot': ('Acesulfame Potassium', 'mg', 'Amount'),
              'addsugar': ('Added Sugars (by Available Carbohydrate)',
                           'g', 'Amount'),
              'adsugtot': ('Added Sugars (by Total Sugars)', 'g', 'Amount'),
              'alanine': ('Alanine', 'g', 'Amount'),
              'alcohol': ('Alcohol', 'g', 'Amount'),
              'alphacar': ('Alpha-Carotene (provitamin A carotenoid)', 'mcg',
                           'Amount'),
              'alphtoce': ('Total Vitamin E Activity (total alpha-tocopherol equivalents)',  # noqa
                           'mg', 'Amount'),
              'alphtoco': ('Alpha-Tocopherol', 'mg', 'Amount'),
              'arginine': ('Arginine', 'g', 'Amount'),
              'ash': ('Ash', 'g', 'Amount'),
              'aspartam': ('Aspartame', 'mg', 'Amount'),
              'aspartic': ('Aspartic Acid', 'g', 'Amount'),
              'avcarb': ('Available Carbohydrate', 'g', 'Amount'),
              'betacar': ('Beta-Carotene (provitamin A carotenoid)', 'mcg',
                          'Amount'),
              'betacryp': ('Beta-Cryptoxanthin (provitamin A carotenoid)',
                           'mcg', 'Amount'),
              'betaine': ('Betaine', 'mg', 'Amount'),
              'betatoco': ('Beta-Tocopherol', 'mg', 'Amount'),
              'biochana': ('Biochanin A', 'mg', 'Amount'),
              'caffeine': ('Caffeine', 'mg', 'Amount'),
              'calcium': ('Calcium', 'mg', 'Amount'),
              'calories': ('Energy', 'kcal', 'Amount'),
              'carbo': ('Total Carbohydrate', 'g', 'Amount'),
              'cholest': ('Cholesterol', 'mg', 'Amount'),
              'choline': ('Choline', 'g', 'Amount'),
              'clac9t11': ('CLA cis-9, trans-11', 'g', 'Amount'),
              'clat10c12': ('CLA trans-10, cis-12', 'g', 'Amount'),
              'copper': ('Copper', 'mg', 'Amount'),
              'coumest': ('Coumestrol', 'mg', 'Amount'),
              'cystine': ('Cystine', 'g', 'Amount'),
              'daidzein': ('Daidzein', 'mg', 'Amount'),
              'delttoco': ('Delta-Tocopherol', 'mg', 'Amount'),
              'erythr': ('Erythritol', 'g', 'Amount'),
              'fat': ('Total Fat', 'g', 'Amount'),
              'fiber': ('Total Dietary Fiber', 'g', 'Amount'),
              'fibh2o': ('Soluble Dietary Fiber', 'g', 'Amount'),
              'fibinso': ('Insoluble Dietary Fiber', 'g', 'Amount'),
              'fol_deqv': ('Dietary Folate Equivalents', 'mcg', 'Amount'),
              'fol_nat': ('Natural Folate (food folate)', 'mcg', 'Amount'),
              'fol_syn': ('Synthetic Folate (folic acid)', 'mcg', 'Amount'),
              'formontn': ('Formononetin', 'mg', 'Amount'),
              'fructose': ('Fructose', 'g', 'Amount'),
              'galactos': ('Galactose', 'g', 'Amount'),
              'gammtoco': ('Gamma-Tocopherol', 'mg', 'Amount'),
              'genistn': ('Genistein', 'mg', 'Amount'),
              'glucose': ('Glucose', 'g', 'Amount'),
              'glutamic': ('Glutamic Acid', 'g', 'Amount'),
              'glycine': ('Glycine', 'g', 'Amount'),
              'glycitn': ('Glycitein', 'mg', 'Amount'),
              'grams': ('Total Grams', 'g', 'Amount'),
              'histidin': ('Histidine', 'g', 'Amount'),
              'inositol': ('Inositol', 'g', 'Amount'),
              'iron': ('Iron', 'mg', 'Amount'),
              'isoleuc': ('Isoleucine', 'g', 'Amount'),
              'isomalt': ('Isomalt', 'g', 'Amount'),
              'joules': ('Energy', 'kj', 'Amount'),
              'lactitol': ('Lactitol', 'g', 'Amount'),
              'lactose': ('Lactose', 'g', 'Amount'),
              'leucine': ('Leucine', 'g', 'Amount'),
              'lutzeax': ('Lutein + Zeaxanthin', 'mcg', 'Amount'),
              'lycopene': ('Lycopene', 'mcg', 'Amount'),
              'lysine': ('Lysine', 'g', 'Amount'),
              'magnes': ('Magnesium', 'mg', 'Amount'),
              'maltitol': ('Maltitol', 'g', 'Amount'),
              'maltose': ('Maltose', 'g', 'Amount'),
              'mangan': ('Manganese', 'mg', 'Amount'),
              'mannitol': ('Mannitol', 'g', 'Amount'),
              'methhis3': ('3-Methylhistidine', 'mg', 'Amount'),
              'methion': ('Methionine', 'g', 'Amount'),
              'mfa141': ('MUFA 14:1 (myristoleic acid)', 'g', 'Amount'),
              'mfa161': ('MUFA 16:1 (palmitoleic acid)', 'g', 'Amount'),
              'mfa181': ('MUFA 18:1 (oleic acid)', 'g', 'Amount'),
              'mfa201': ('MUFA 20:1 (gadoleic acid)', 'g', 'Amount'),
              'mfa221': ('MUFA 22:1 (erucic acid)', 'g', 'Amount'),
              'mfatot': ('Total Monounsaturated Fatty Acids (MUFA)', 'g',
                         'Amount'),
              'natoco': ('Natural Alpha-Tocopherol (RRR-alpha-tocopherol or d-alpha-tocopherol)',  # noqa
                         'mg', 'Amount'),
              'niacin': ('Niacin (vitamin B3)', 'mg', 'Amount'),
              'niacineq': ('Niacin Equivalents', 'mg', 'Amount'),
              'nitrogen': ('Nitrogen', 'g', 'Amount'),
              'omega3': ('Omega-3 Fatty Acids', 'g', 'Amount'),
              'oxalic': ('Oxalic Acid', 'mg', 'Amount'),
              'pantothe': ('Pantothenic acid', 'mg', 'Amount'),
              'pectins': ('Pectins', 'g', 'Amount'),
              'pfa182': ('PUFA 18:2 (linoleic acid)', 'g', 'Amount'),
              'pfa183': ('PUFA 18:3 (linolenic acid)', 'g', 'Amount'),
              'pfa183n3': ('PUFA 18:3 n-3 (alpha-linolenic acid [ALA])', 'g',
                           'Amount'),
              'pfa184': ('PUFA 18:4 (parinaric acid)', 'g', 'Amount'),
              'pfa204': ('PUFA 20:4 (arachidonic acid)', 'g', 'Amount'),
              'pfa205': ('PUFA 20:5 (eicosapentaenoic acid [EPA])', 'g',
                         'Amount'),
              'pfa225': ('PUFA 22:5 (docosapentaenoic acid [DPA])', 'g',
                         'Amount'),
              'pfa226': ('PUFA 22:6 (docosahexaenoic acid [DHA])', 'g',
                         'Amount'),
              'pfatot': ('Total Polyunsaturated Fatty Acids (PUFA)', 'g',
                         'Amount'),
              'phenylal': ('Phenylalanine', 'g', 'Amount'),
              'phosphor': ('Phosphorus', 'mg', 'Amount'),
              'phytic': ('Phytic Acid', 'mg', 'Amount'),
              'pinitol': ('Pinitol', 'g', 'Amount'),
              'potass': ('Potassium', 'mg', 'Amount'),
              'proline': ('Proline', 'g', 'Amount'),
              'protanim': ('Animal Protein', 'g', 'Amount'),
              'protein': ('Total Protein', 'g', 'Amount'),
              'protveg': ('Vegetable Protein', 'g', 'Amount'),
              'retinol': ('Retinol', 'mcg', 'Amount'),
              'ribofla': ('Riboflavin (vitamin B2)', 'mg', 'Amount'),
              'sacchar': ('Saccharin', 'mg', 'Amount'),
              'satoco': ('Synthetic Alpha-Tocopherol (all rac-alpha-tocopherol or dl-alpha-tocopherol)',  # noqa
                         'mg', 'Amount'),
              'selenium': ('Selenium', 'mcg', 'Amount'),
              'serine': ('Serine', 'g', 'Amount'),
              'sfa100': ('SFA 10:0 (capric acid)', 'g', 'Amount'),
              'sfa120': ('SFA 12:0 (lauric acid)', 'g', 'Amount'),
              'sfa140': ('SFA 14:0 (myristic acid)', 'g', 'Amount'),
              'sfa160': ('SFA 16:0 (palmitic acid)', 'g', 'Amount'),
              'sfa170': ('SFA 17:0 (margaric acid)', 'g', 'Amount'),
              'sfa180': ('SFA 18:0 (stearic acid)', 'g', 'Amount'),
              'sfa200': ('SFA 20:0 (arachidic acid)', 'g', 'Amount'),
              'sfa220': ('SFA 22:0 (behenic acid)', 'g', 'Amount'),
              'sfa40': ('SFA 4:0 (butyric acid)', 'g', 'Amount'),
              'sfa60': ('SFA 6:0 (caproic acid)', 'g', 'Amount'),
              'sfa80': ('SFA 8:0 (caprylic acid)', 'g', 'Amount'),
              'sfatot': ('Total Saturated Fatty Acids (SFA)', 'g', 'Amount'),
              'sodium': ('Sodium', 'mg', 'Amount'),
              'solidfat': ('Solid Fats', 'g', 'Amount'),
              'sorbitol': ('Sorbitol', 'g', 'Amount'),
              'starch': ('Starch', 'g', 'Amount'),
              'sucpoly': ('Sucrose polyester', 'g', 'Amount'),
              'sucrlose': ('Sucralose', 'mg', 'Amount'),
              'sucrose': ('Sucrose', 'g', 'Amount'),
              'tagatose': ('Tagatose', 'mg', 'Amount'),
              'tfa161t': ('TRANS 16:1 (trans-hexadecenoic acid)', 'g',
                          'Amount'),
              'tfa181t': ('TRANS 18:1 (trans-octadecenoic acid [elaidic acid])',  # noqa
                          'g', 'Amount'),
              'tfa182t': ('TRANS 18:2 (trans-octadecadienoic acid [linolelaidic acid]; incl. c-t, t-c, t-t)',  # noqa
                          'g', 'Amount'),
              'thiamin': ('Thiamin (vitamin B1)', 'mg', 'Amount'),
              'threonin': ('Threonine', 'g', 'Amount'),
              'totaltfa': ('Total Trans-Fatty Acids (TRANS)', 'g', 'Amount'),
              'totcla': ('Total Conjugated Linoleic Acid (CLA 18:2)', 'g',
                         'Amount'),
              'totfolat': ('Total Folate', 'mcg', 'Amount'),
              'totsugar': ('Total Sugars', 'g', 'Amount'),
              'tryptoph': ('Tryptophan', 'g', 'Amount'),
              'tyrosine': ('Tyrosine', 'g', 'Amount'),
              'valine': ('Valine', 'g', 'Amount'),
              'vita_iu': ('Total Vitamin A Activity', 'IU', 'Amount'),
              'vita_rae': ('Total Vitamin A Activity (Retinol Activity Equivalents)',  # noqa
                           'mcg', 'Amount'),
              'vita_re': ('Total Vitamin A Activity (Retinol Equivalents)',
                          'mcg', 'Amount'),
              'vitb12': ('Vitamin B-12 (cobalamin)', 'mcg', 'Amount'),
              'vitb6': ('Vitamin B-6 (pyridoxine, pyridoxyl, & pyridoxamine)',
                        'mg', 'Amount'),
              'vitc': ('Vitamin C (ascorbic acid)', 'mg', 'Amount'),
              'vitd': ('Vitamin D (calciferol)', 'mcg', 'Amount'),
              'vitd2': ('Vitamin D2 (ergocalciferol)', 'mcg', 'Amount'),
              'vitd3': ('Vitamin D3 (cholecalciferol)', 'mcg', 'Amount'),
              'vite_iu': ('Vitamin E', 'IU', 'Amount'),
              'vitk': ('Vitamin K (phylloquinone)', 'mcg', 'Amount'),
              'water': ('Water', 'g', 'Amount'),
              'xylitol': ('Xylitol', 'g', 'Amount'),
              'zinc': ('Zinc', 'mg', 'Amount'),
              'oxalicm': ('Oxalic Acid from Mayo', 'mg', 'Amount'),
              'vitd_iu': ('Vitamin D', 'IU', 'Amount'),
              'omega3_epadha': ('Omega-3 Fatty Acids [EPA + DHA]', 'g',
                                'Amount'),
              'omega6_la': ('pfa182 + pfa204, la = linoleic acid', 'g',
                            'Amount')}

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_food_components(self, vioscreen_food_components):
        """Add in food components results for a session

        Parameters
        ----------
        vioscreen_food_components : VioscreenFoodComponents
            An instance of a food components model

        Returns
        -------
        int
            The number of inserted rows
        """
        with self._transaction.cursor() as cur:
            components = vioscreen_food_components.components
            inserts = []
            for component in components:
                # checking if code exists in lookup
                self._get_code_info(component.code)
                inserts.append((vioscreen_food_components.sessionId,
                                component.code,
                                component.amount))

            cur.executemany("""INSERT INTO ag.vioscreen_foodcomponents
                                (sessionId, code, amount)
                                VALUES (%s, %s, %s)""",
                            inserts)
            return cur.rowcount

    def get_food_components(self, sessionId):
        """Obtain the food components detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        VioscreenFoodComponents or None
            The food components detail, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_foodcomponents
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for code, amount in rows:
                    codeInfo = self._get_code_info(code)
                    vfcc = VioscreenFoodComponentsComponent(code=code,
                                                            description=codeInfo[0],  # noqa
                                                            units=codeInfo[1],  # noqa
                                                            amount=amount,
                                                            valueType=codeInfo[2])  # noqa
                    components.append(vfcc)
                return VioscreenFoodComponents(sessionId=sessionId,
                                               components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular food component by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The description, units and valueType for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        if code not in self._CODES:
            raise NotFound("No such code: " + code)

        return self._CODES[code]

    def get_food_components_by_code(self, code):
        """Obtain the all the amounts for a particular code
        Parameters
        ----------
        code : str
            The code to query
        Returns
        -------
        Float Array or None
            The amounts, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT amount
                           FROM ag.vioscreen_foodcomponents
                           WHERE code = %s""",
                        (code,))

            rows = cur.fetchall()
            if len(rows) > 0:
                amounts = []
                for amount in rows:
                    amounts.append(amount[0])
                return amounts

            else:
                return None

    def get_food_components_descriptions(self):
        return self._CODES


class VioscreenEatingPatternsRepo(BaseRepo):
    # code : (description, units, valueType)
    _CODES = {'ADDEDFATS': ('Eating Pattern', 'PerDay', 'Amount'),
              'ALCOHOLSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'ANIMALPROTEIN': ('Eating Pattern', 'PerDay', 'Amount'),
              'CALCDAIRYSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'CALCSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'FISHSERV': ('Eating Pattern', 'PerWeek', 'Amount'),
              'FRIEDFISH': ('Eating Pattern', 'PerWeek', 'Amount'),
              'FRTSUMM': ('Eating Pattern', 'PerDay', 'Amount'),
              'GRAINSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'JUICESERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'LOWFATDAIRYSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'NOFRYFISHSERV': ('Eating Pattern', 'PerWeek', 'Amount'),
              'NONFATDAIRY': ('Eating Pattern', 'PerDay', 'Amount'),
              'PLANTPROTEIN': ('Eating Pattern', 'PerDay', 'Amount'),
              'SALADSERV': ('Eating Pattern', 'PerDay', 'Amount'),
              'SOYFOODS': ('Eating Pattern', 'PerDay', 'Amount'),
              'VEGSUMM': ('Eating Pattern', 'PerDay', 'Amount')}

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_eating_patterns(self, vioscreen_eating_patterns):
        """Add in eating patterns results for a session

        Parameters
        ----------
        vioscreen_eating_patterns : VioscreenEatingPatterns
            An instance of a eating patterns model

        Returns
        -------
        int
            The number of inserted rows
        """
        with self._transaction.cursor() as cur:
            components = vioscreen_eating_patterns.components
            inserts = []
            for component in components:
                # checking if code exists in lookup
                self._get_code_info(component.code)
                inserts.append((vioscreen_eating_patterns.sessionId,
                                component.code,
                                component.amount))

            cur.executemany("""INSERT INTO ag.vioscreen_eatingpatterns
                                (sessionId, code, amount)
                                VALUES (%s, %s, %s)""",
                            inserts)
            return cur.rowcount

    def get_eating_patterns(self, sessionId):
        """Obtain the eating patterns detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        VioscreenEatingPatterns or None
            The eating patterns detail, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_eatingpatterns
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for code, amount in rows:
                    codeInfo = self._get_code_info(code)
                    vepc = VioscreenEatingPatternsComponent(code=code,
                                                            description=codeInfo[0],  # noqa
                                                            units=codeInfo[1],  # noqa
                                                            amount=amount,
                                                            valueType=codeInfo[2])  # noqa
                    components.append(vepc)
                return VioscreenEatingPatterns(sessionId=sessionId,
                                               components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular eating pattern by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The description, units and valueType for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        if code not in self._CODES:
            raise NotFound("No such code: " + code)

        return self._CODES[code]


class VioscreenMPedsRepo(BaseRepo):
    # code : (description, units, valueType)
    _CODES = {'A_BEV': ('MPED: Total drinks of alcohol', 'alc_drinks',
                        'Amount'),
              'A_CAL': ('MPED: Calories from alcoholic beverages', 'kcal',
                        'Amount'),
              'ADD_SUG': ('MPED: Teaspoon equivalents of added sugars',
                          'tsp_eq', 'Amount'),
              'D_CHEESE': ('MPED: Number of cheese cup equivalents', 'cup_eq',
                           'Amount'),
              'D_MILK': ('MPED: Number of milk cup equivalents', 'cup_eq',
                         'Amount'),
              'D_TOT_SOYM': ('MPED: Total number of milk group (milk, yogurt & cheese) cup equivalents PLUS soy milk',  # noqa
                             'cup_eq', 'Amount'),
              'D_TOTAL': ('MPED: Total number of milk group (milk, yogurt & cheese) cup equivalents',  # noqa
                          'cup_eq', 'Amount'),
              'D_YOGURT': ('MPED: Number of yogurt cup equivalents', 'cup_eq',
                           'Amount'),
              'DISCFAT_OIL': ('MPED: Grams of discretionary Oil', 'g',
                              'Amount'),
              'DISCFAT_SOL': ('MPED: Grams of discretionary Solid fat', 'g',
                              'Amount'),
              'F_CITMLB': ('MPED: Number of citrus, melon, berry cup equivalents',  # noqa
                           'cup_eq', 'Amount'),
              'F_NJ_CITMLB': ('MPED: Number of non-juice citrus, melon, berry cup equivalents',  # noqa
                              'cup_eq', 'Amount'),
              'F_NJ_OTHER': ('MPED: Number of other non-juice fruit cup equivalents',  # noqa
                             'cup_eq', 'Amount'),
              'F_NJ_TOTAL': ('MPED: Total number of non-juice fruit cup equivalents',  # noqa
                             'cup_eq', 'Amount'),
              'F_OTHER': ('MPED: Number of other fruit cup equivalents',
                          'cup_eq', 'Amount'),
              'F_TOTAL': ('MPED: Total number of fruit cup equivalents',
                          'cup_eq', 'Amount'),
              'G_NWHL': ('MPED: Number of non-whole grain ounce equivalents',
                         'oz_eq', 'Amount'),
              'G_TOTAL': ('MPED: Total number of grain ounce equivalents',
                          'oz_eq', 'Amount'),
              'G_WHL': ('MPED: Number of whole grain ounce equivalents',
                        'oz_eq', 'Amount'),
              'LEGUMES': ('MPED: Number of cooked dry beans and peas cup equivalents',  # noqa
                          'cup_eq', 'Amount'),
              'M_EGG': ('MPED: Oz equivalents of lean meat from eggs', 'oz_eq',
                        'Amount'),
              'M_FISH_HI': ('MPED: Oz cooked lean meat from fish, other seafood high in Omega-3',  # noqa
                            'oz_eq', 'Amount'),
              'M_FISH_LO': ('MPED: Oz cooked lean meat from fish, other seafood low in Omega-3',  # noqa
                            'oz_eq', 'Amount'),
              'M_FRANK': ('MPED: Oz cooked lean meat from franks, sausages, luncheon meats',  # noqa
                          'oz_eq', 'Amount'),
              'M_MEAT': ('MPED: Oz cooked lean meat from beef, pork, veal, lamb, and game',  # noqa
                         'oz_eq', 'Amount'),
              'M_MPF': ('MPED: Oz cooked lean meat from meat, poultry, fish',
                        'oz_eq', 'Amount'),
              'M_NUTSD': ('MPED: Oz equivalents of lean meat from nuts and seeds',  # noqa
                          'oz_eq', 'Amount'),
              'M_ORGAN': ('MPED: Oz cooked lean meat from organ meats',
                          'oz_eq', 'Amount'),
              'M_POULT': ('MPED: Oz cooked lean meat from chicken, poultry, and other poultry',  # noqa
                          'oz_eq', 'Amount'),
              'M_SOY': ('MPED: Oz equivalents of lean meat from soy product',
                        'oz_eq', 'Amount'),
              'rgrain': ('Refined Grains (ounce equivalents)', 'oz_eq',
                         'Amount'),
              'tgrain': ('Total Grains (ounce equivalents)', 'oz_eq',
                         'Amount'),
              'V_DRKGR': ('MPED: Number of dark-green vegetable cup equivalents',  # noqa
                          'cup_eq', 'Amount'),
              'V_ORANGE': ('MPED: Number of orange vegetable cup equivalents',
                           'cup_eq', 'Amount'),
              'V_OTHER': ('MPED: Number of other vegetable cup equivalents',
                          'cup_eq', 'Amount'),
              'V_POTATO': ('MPED: Number of white potato cup equivalents',
                           'cup_eq', 'Amount'),
              'V_STARCY': ('MPED: Number of other starchy vegetable cup equivalents',  # noqa
                           'cup_eq', 'Amount'),
              'V_TOMATO': ('MPED: Number of tomato cup equivalents', 'cup_eq',
                           'Amount'),
              'V_TOTAL': ('MPED: Total number of vegetable cup equivalents, excl legumes',  # noqa
                          'cup_eq', 'Amount'),
              'wgrain': ('Whole Grains (ounce equivalents)', 'oz_eq',
                         'Amount')}

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_mpeds(self, vioscreen_mpeds):
        """Add in mpeds results for a session

        Parameters
        ----------
        vioscreen_mpeds : VioscreenMPeds
            An instance of a mpeds model

        Returns
        -------
        int
            The number of inserted rows
        """
        with self._transaction.cursor() as cur:
            components = vioscreen_mpeds.components
            inserts = []
            for component in components:
                # checking if code exists in lookup
                self._get_code_info(component.code)
                inserts.append((vioscreen_mpeds.sessionId,
                                component.code,
                                component.amount))

            cur.executemany("""INSERT INTO ag.vioscreen_mpeds
                                (sessionId, code, amount)
                                VALUES (%s, %s, %s)""",
                            inserts)
            return cur.rowcount

    def get_mpeds(self, sessionId):
        """Obtain the mpeds detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        VioscreenMPeds or None
            The mpeds detail, or None if no record was found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_mpeds
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for code, amount in rows:
                    codeInfo = self._get_code_info(code)
                    vmpc = VioscreenMPedsComponent(code=code,
                                                   description=codeInfo[0],  # noqa
                                                   units=codeInfo[1],  # noqa
                                                   amount=amount,
                                                   valueType=codeInfo[2])
                    components.append(vmpc)
                return VioscreenMPeds(sessionId=sessionId,
                                      components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular mped by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The description, units and valueType for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        if code not in self._CODES:
            raise NotFound("No such code: " + code)

        return self._CODES[code]


class VioscreenFoodConsumptionRepo(BaseRepo):
    # code : (description, units, valueType)
    _CODES = {'acesupot': ('Acesulfame Potassium', 'mg', 'Amount'),
              'addsugar': ('Added Sugar', 'g', 'Amount'),
              'adsugtot': ('Added Sugars (by Total Sugars)', 'g', 'Amount'),
              'alanine': ('Alanine', 'g', 'Amount'),
              'alcohol': ('Alcohol', 'g', 'Amount'),
              'alphacar': ('Alpha-Carotene (provitamin A carotenoid)', 'mcg',
                           'Amount'),
              'alphtoce': ('Total Vitamin E Activity (total alpha-tocopherol equivalents)',  # noqa
                           'mg', 'Amount'),
              'alphtoco': ('Alpha-Tocopherol', 'mg', 'Amount'),
              'arginine': ('Arginine', 'g', 'Amount'),
              'ash': ('Ash', 'g', 'Amount'),
              'aspartam': ('Aspartame', 'mg', 'Amount'),
              'aspartic': ('Aspartic Acid', 'g', 'Amount'),
              'avcarb': ('Available Carbohydrate', 'g', 'Amount'),
              'betacar': ('Beta-Carotene (provitamin A carotenoid)', 'mcg',
                          'Amount'),
              'betacryp': ('Beta-Cryptoxanthin (provitamin A carotenoid)',
                           'mcg', 'Amount'),
              'betaine': ('Betaine', 'mg', 'Amount'),
              'betatoco': ('Beta-Tocopherol', 'mg', 'Amount'),
              'biochana': ('Biochanin A', 'mg', 'Amount'),
              'caffeine': ('Caffeine', 'mg', 'Amount'),
              'calcium': ('Calcium', 'mg', 'Amount'),
              'calories': ('Energy (kcal)', 'kcal', 'Amount'),
              'carbo': ('Total Carbohydrate', 'g', 'Amount'),
              'cholest': ('Cholesterol', 'mg', 'Amount'),
              'choline': ('Choline', 'mg', 'Amount'),
              'clac9t11': ('CLA cis-9, trans-11', 'g', 'Amount'),
              'clat10c12': ('CLA trans-10, cis-12', 'g', 'Amount'),
              'copper': ('Copper', 'mg', 'Amount'),
              'coumest': ('Coumestrol', 'mg', 'Amount'),
              'cystine': ('Cystine', 'g', 'Amount'),
              'daidzein': ('Daidzein', 'mg', 'Amount'),
              'delttoco': ('Delta-Tocopherol', 'mg', 'Amount'),
              'erythr': ('Erythritol', 'g', 'Amount'),
              'fat': ('Total Fat', 'g', 'Amount'),
              'fiber': ('Total Dietary Fiber', 'g', 'Amount'),
              'fibh2o': ('Soluble Dietary Fiber', 'g', 'Amount'),
              'fibinso': ('Insoluble Dietary Fiber', 'g', 'Amount'),
              'fol_deqv': ('Dietary Folate Equivalents', 'mcg', 'Amount'),
              'fol_nat': ('Natural Folate (food folate)', 'mcg', 'Amount'),
              'fol_syn': ('Synthetic Folate (folic acid)', 'mcg', 'Amount'),
              'formontn': ('Formononetin', 'mg', 'Amount'),
              'fructose': ('Fructose', 'g', 'Amount'),
              'galactos': ('Galactose', 'g', 'Amount'),
              'gammtoco': ('Gamma-Tocopherol', 'mg', 'Amount'),
              'genistn': ('Genistein', 'mg', 'Amount'),
              'GLAC': ('Glycemic Load Available Carbs', 'unit', 'Index'),
              'GLTC': ('Glycemic Load Total Carbs', 'unit', 'Index'),
              'glucose': ('Glucose', 'g', 'Amount'),
              'glutamic': ('Glutamic Acid', 'g', 'Amount'),
              'glycine': ('Glycine', 'g', 'Amount'),
              'glycitn': ('Glycitein', 'mg', 'Amount'),
              'grams': ('grams', '-', 'Amount'),
              'histidin': ('Histidine', 'g', 'Amount'),
              'inositol': ('Inositol', 'g', 'Amount'),
              'iron': ('Iron', 'mg', 'Amount'),
              'isoleuc': ('Isoleucine', 'g', 'Amount'),
              'isomalt': ('Isomalt', 'g', 'Amount'),
              'joules': ('Energy (kj)', 'g', 'Amount'),
              'lactitol': ('Lactitol', 'g', 'Amount'),
              'lactose': ('Lactose', 'g', 'Amount'),
              'leucine': ('Leucine', 'g', 'Amount'),
              'LineGi': ('LineGi', 'unit', 'Index'),
              'lutzeax': ('Lutein + Zeaxanthin', 'mcg', 'Amount'),
              'lycopene': ('Lycopene', 'mcg', 'Amount'),
              'lysine': ('Lysine', 'g', 'Amount'),
              'magnes': ('Magnesium', 'mg', 'Amount'),
              'maltitol': ('Maltitol', 'g', 'Amount'),
              'maltose': ('Maltose', 'g', 'Amount'),
              'mangan': ('Manganese', 'mg', 'Amount'),
              'mannitol': ('Mannitol', 'g', 'Amount'),
              'methhis3': ('3-Methylhistidine', 'mg', 'Amount'),
              'methion': ('Methionine', 'g', 'Amount'),
              'mfa141': ('MUFA 14:1 (myristoleic acid)', 'g', 'Amount'),
              'mfa161': ('MUFA 16:1 (palmitoleic acid)', 'g', 'Amount'),
              'mfa181': ('MUFA 18:1 (oleic acid)', 'g', 'Amount'),
              'mfa201': ('MUFA 20:1 (gadoleic acid)', 'g', 'Amount'),
              'mfa221': ('MUFA 22:1 (erucic acid)', 'g', 'Amount'),
              'mfatot': ('Total Monounsaturated Fatty Acids (MUFA)', 'g',
                         'Amount'),
              'natoco': ('Natural Alpha-Tocopherol (RRR-alpha-tocopherol or d-alpha-tocopherol)',  # noqa
                         'mg', 'Amount'),
              'nccglbr': ('NCC Glycemic Load (bread reference)', 'g', 'Index'),
              'nccglgr': ('NCC Glycemic Load (glucose reference)', 'unit',
                          'Index'),
              'niacin': ('Niacin (vitamin B3)', 'mg', 'Amount'),
              'niacineq': ('Niacin Equivalents', 'mg', 'Amount'),
              'nitrogen': ('Nitrogen', 'g', 'Amount'),
              'omega3': ('Omega-3 Fatty Acids', 'g', 'Amount'),
              'oxalic': ('Oxalic Acid', 'mg', 'Amount'),
              'pantothe': ('Pantothenic acid', 'mg', 'Amount'),
              'pectins': ('Pectins', 'g', 'Amount'),
              'pfa182': ('PUFA 18:2 (linoleic acid)', 'g', 'Amount'),
              'pfa183': ('PUFA 18:3 (linolenic acid)', 'g', 'Amount'),
              'pfa183n3': ('PUFA 18:3 n-3 (alpha-linolenic acid [ALA])', 'g',
                           'Amount'),
              'pfa184': ('PUFA 18:4 (parinaric acid)', 'g', 'Amount'),
              'pfa204': ('PUFA 20:4 (arachidonic acid)', 'g', 'Amount'),
              'pfa205': ('PUFA 20:5 (eicosapentaenoic acid [EPA])', 'g',
                         'Amount'),
              'pfa225': ('PUFA 22:5 (docosapentaenoic acid [DPA])', 'g',
                         'Amount'),
              'pfa226': ('PUFA 22:6 (docosahexaenoic acid [DHA])', 'g',
                         'Amount'),
              'pfatot': ('Total Polyunsaturated Fatty Acids (PUFA)', 'g',
                         'Amount'),
              'phenylal': ('Phenylalanine', 'g', 'Amount'),
              'phosphor': ('Phosphorus', 'mg', 'Amount'),
              'phytic': ('Phytic Acid', 'mg', 'Amount'),
              'pinitol': ('Pinitol', 'g', 'Amount'),
              'potass': ('Potassium', 'mg', 'Amount'),
              'proline': ('Proline', 'g', 'Amount'),
              'protanim': ('Animal Protein', 'g', 'Amount'),
              'protein': ('Total Protein', 'g', 'Amount'),
              'protveg': ('Vegetable Protein', 'g', 'Amount'),
              'retinol': ('Retinol', 'mcg', 'Amount'),
              'ribofla': ('Riboflavin (vitamin B2)', 'mg', 'Amount'),
              'sacchar': ('Saccharin', 'mg', 'Amount'),
              'satoco': ('Synthetic Alpha-Tocopherol (all rac-alpha-tocopherol or dl-alpha-tocopherol)',  # noqa
                         'mg', 'Amount'),
              'selenium': ('Selenium', 'mcg', 'Amount'),
              'serine': ('Serine', 'g', 'Amount'),
              'sfa100': ('SFA 10:0 (capric acid)', 'g', 'Amount'),
              'sfa120': ('SFA 12:0 (lauric acid)', 'g', 'Amount'),
              'sfa140': ('SFA 14:0 (myristic acid)', 'g', 'Amount'),
              'sfa160': ('SFA 16:0 (palmitic acid)', 'g', 'Amount'),
              'sfa170': ('SFA 17:0 (margaric acid)', 'g', 'Amount'),
              'sfa180': ('SFA 18:0 (stearic acid)', 'g', 'Amount'),
              'sfa200': ('SFA 20:0 (arachidic acid)', 'g', 'Amount'),
              'sfa220': ('SFA 22:0 (behenic acid)', 'g', 'Amount'),
              'sfa40': ('SFA 4:0 (butyric acid)', 'g', 'Amount'),
              'sfa60': ('SFA 6:0 (caproic acid)', 'g', 'Amount'),
              'sfa80': ('SFA 8:0 (caprylic acid)', 'g', 'Amount'),
              'sfatot': ('Total Saturated Fatty Acids (SFA)', 'g', 'Amount'),
              'sodium': ('Sodium', 'mg', 'Amount'),
              'solidfat': ('solidfat', 'g', 'Amount'),
              'sorbitol': ('Sorbitol', 'g', 'Amount'),
              'starch': ('Starch', 'g', 'Amount'),
              'sucpoly': ('Sucrose polyester', 'g', 'Amount'),
              'sucrlose': ('Sucralose', 'g', 'Amount'),
              'sucrose': ('Sucrose', 'g', 'Amount'),
              'tagatose': ('Tagatose', 'mg', 'Amount'),
              'tfa161t': ('TRANS 16:1 (trans-hexadecenoic acid)', 'g',
                          'Amount'),
              'tfa181t': ('TRANS 18:1 (trans-octadecenoic acid [elaidic acid])',  # noqa
                          'g', 'Amount'),
              'tfa182t': ('TRANS 18:2 (trans-octadecadienoic acid [linolelaidic acid]; incl. c-t, t-c, t-t)',  # noqa
                          'g', 'Amount'),
              'thiamin': ('Thiamin (vitamin B1)', 'mg', 'Amount'),
              'threonin': ('Threonine', 'g', 'Amount'),
              'totaltfa': ('Total Trans-Fatty Acids (TRANS)', 'g', 'Amount'),
              'totcla': ('Total Conjugated Linoleic Acid (CLA 18:2)', 'g',
                         'Amount'),
              'totfolat': ('Total Folate', 'mcg', 'Amount'),
              'totsugar': ('Total Sugars', 'g', 'Amount'),
              'tryptoph': ('Tryptophan', 'g', 'Amount'),
              'tyrosine': ('Tyrosine', 'g', 'Amount'),
              'valine': ('Valine', 'g', 'Amount'),
              'vita_iu': ('Total Vitamin A Activity (International Units)',
                          'IU', 'Amount'),
              'vita_rae': ('Total Vitamin A Activity (Retinol Activity Equivalents)',  # noqa
                           'mcg', 'Amount'),
              'vita_re': ('Total Vitamin A Activity (Retinol Equivalents)',
                          'mcg', 'Amount'),
              'vitb12': ('Vitamin B-12 (cobalamin)', 'mcg', 'Amount'),
              'vitb6': ('Vitamin B-6 (pyridoxine, pyridoxyl, & pyridoxamine)',
                        'mg', 'Amount'),
              'vitc': ('Vitamin C (ascorbic acid)', 'mg', 'Amount'),
              'vitd': ('Vitamin D (calciferol)', 'mcg', 'Amount'),
              'vitd2': ('vitd2', '-', 'Amount'),
              'vitd3': ('vitd3', '-', 'Amount'),
              'vite_iu': ('Vitamin E (International Units)', 'IU', 'Amount'),
              'vitk': ('Vitamin K (phylloquinone)', 'mcg', 'Amount'),
              'water': ('Water', 'g', 'Amount'),
              'xylitol': ('Xylitol', 'g', 'Amount'),
              'zinc': ('Zinc', 'mg', 'Amount'),
              'oxalicm': ('Oxalic Acid from Mayo', 'mg', 'Amount'),
              'vitd_iu': ('Vitamin D (International Units)', 'IU', 'Amount'),
              'omega3_epadha': ('Omega-3 Fatty Acids [EPA + DHA]', 'g',
                                'Amount'),
              'omega6_la': ('pfa182 + pfa204, la = linoleic acid', 'g',
                            'Amount')}

    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_food_consumption(self, vioscreen_food_consumption):
        """Add in food consumption results for a session

        Parameters
        ----------
        vioscreen_food_consumption : VioscreenFoodConsumption
            An instance of a food consumption model

        Returns
        -------
        int
            The number of inserted rows
        """
        with self._transaction.cursor() as cur:
            rowcount = 0
            components = vioscreen_food_consumption.components

            component_inserts = []
            component_consumption_inserts = []
            for component in components:
                component_inserts.append((
                    vioscreen_food_consumption.sessionId,
                    component.foodCode,
                    component.description,
                    component.foodGroup,
                    component.amount,
                    component.frequency,
                    component.consumptionAdjustment,
                    component.servingSizeText,
                    component.servingFrequencyText,
                    component.created))

                for component2 in component.data:
                    # checking if code exists in lookup
                    self._get_code_info(component2.code)
                    component_consumption_inserts.append((
                        vioscreen_food_consumption.sessionId,
                        component.description,
                        component2.code,
                        component2.amount))

            cur.executemany("""INSERT INTO ag.vioscreen_foodconsumption
                               (sessionId, foodCode, description, foodGroup,
                                amount, frequency, consumptionAdjustment,
                                servingSizeText, servingFrequencyText, created)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, component_inserts)
            rowcount += cur.rowcount

            cur.executemany("""
                            INSERT INTO ag.vioscreen_foodconsumptioncomponents
                            (sessionId, description, code, amount)
                            VALUES (%s, %s, %s, %s)""",
                            component_consumption_inserts)
            rowcount += cur.rowcount

            return rowcount

    def get_food_consumption(self, sessionId):
        """Obtain the food consumption detail for a particular session

        Parameters
        ----------
        sessionId : str
            The session ID to query

        Returns
        -------
        VioscreenFoodConsumption or None
            The food consumption detail, or None if no record was found
        """
        # TODO: it may be possible to do this all in a single query. An
        # attempt was made using array_agg(code, amount), however postgres
        # coerces that to a string. A two dimensional array is possible with
        # array_agg(array[code, amount]) however the types need to be the
        # same (as best as I understand), leading to some theatrics on
        # formatting and parsing. A problem for another day.
        with self._transaction.cursor() as cur:
            cur.execute(
                """SELECT foodCode, description, foodGroup, amount, frequency,
                           consumptionAdjustment, servingSizeText,
                           servingFrequencyText, created
                   FROM ag.vioscreen_foodconsumption
                   WHERE sessionId = %s""", (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                components = []
                for (foodCode, description, foodGroup, amount_outer, frequency,
                     consumptionAdjustment, servingSizeText,
                     servingFrequencyText, created) in rows:
                    cur.execute("""SELECT code, amount
                                   FROM ag.vioscreen_foodconsumptioncomponents
                                   WHERE sessionId = %s AND description = %s
                                """,
                                (sessionId, description))
                    rows2 = cur.fetchall()

                    components2 = []
                    for code, amount in rows2:
                        codeInfo = self._get_code_info(code)
                        vfcc2 = VioscreenFoodComponentsComponent(
                            code=code,
                            description=codeInfo[0],
                            units=codeInfo[1],
                            amount=amount,
                            valueType=codeInfo[2])
                        components2.append(vfcc2)

                    vfcc = VioscreenFoodConsumptionComponent(
                        foodCode=foodCode,
                        description=description,
                        foodGroup=foodGroup,
                        amount=amount_outer,
                        frequency=frequency,
                        consumptionAdjustment=consumptionAdjustment,
                        servingSizeText=servingSizeText,
                        servingFrequencyText=servingFrequencyText,
                        created=created,
                        data=components2)
                    components.append(vfcc)

                return VioscreenFoodConsumption(sessionId=sessionId,
                                                components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular food consumption component by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The description, units and valueType for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        if code not in self._CODES:
            raise NotFound("No such code: " + code)

        return self._CODES[code]


# This was ported from the american_gut_project's ag_data_access.py.
class VioscreenRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_ffq(self, ffq):
        """Represent an ffq instance in our database

        Parameters
        ----------
        ffq : VioscreenComposite instance
            A complete ffq
        """
        sess = VioscreenSessionRepo(self._transaction)
        supp = VioscreenSupplementsRepo(self._transaction)
        scores = VioscreenDietaryScoreRepo(self._transaction)
        energy = VioscreenPercentEnergyRepo(self._transaction)
        food = VioscreenFoodComponentsRepo(self._transaction)
        patterns = VioscreenEatingPatternsRepo(self._transaction)
        mpeds = VioscreenMPedsRepo(self._transaction)
        cons = VioscreenFoodConsumptionRepo(self._transaction)

        sess.upsert_session(ffq.session)
        energy.insert_percent_energy(ffq.percent_energy)
        scores.insert_dietary_scores(ffq.dietary_scores)
        supp.insert_supplements(ffq.supplements)
        food.insert_food_components(ffq.food_components)
        patterns.insert_eating_patterns(ffq.eating_patterns)
        mpeds.insert_mpeds(ffq.mpeds)
        cons.insert_food_consumption(ffq.food_consumption)

    def get_ffq(self, session_id):
        """Obtain a complete ffq

        Parameters
        ----------
        session_id : str
            The session ID to obtain a FFQ for

        Returns
        -------
        VioscreenComposite or None
            The composite object if the FFQ exists
        """
        sess = VioscreenSessionRepo(self._transaction)
        supp = VioscreenSupplementsRepo(self._transaction)
        scores = VioscreenDietaryScoreRepo(self._transaction)
        energy = VioscreenPercentEnergyRepo(self._transaction)
        food = VioscreenFoodComponentsRepo(self._transaction)
        patterns = VioscreenEatingPatternsRepo(self._transaction)
        mpeds = VioscreenMPedsRepo(self._transaction)
        cons = VioscreenFoodConsumptionRepo(self._transaction)

        session = sess.get_session(session_id)
        percent_energy = energy.get_percent_energy(session_id)
        dietary_scores = scores.get_dietary_scores(session_id)
        supplements = supp.get_supplements(session_id)
        eating_patterns = patterns.get_eating_patterns(session_id)
        mpeds = mpeds.get_mpeds(session_id)
        food_consumption = cons.get_food_consumption(session_id)
        food_components = food.get_food_components(session_id)

        return VioscreenComposite(session, percent_energy, dietary_scores,
                                  supplements, food_components,
                                  eating_patterns, mpeds,
                                  food_consumption)

    def upsert_vioscreen_status(self, account_id, source_id,
                                survey_id, status):
        # Check current survey status
        cur_status = self.get_vioscreen_status(account_id,
                                               source_id,
                                               survey_id)

        # If there is no status, insert a row.
        if cur_status is None:
            with self._transaction.cursor() as cur:
                cur.execute(
                    "INSERT INTO ag_login_surveys("
                    "ag_login_id, survey_id, vioscreen_status, source_id) "
                    "VALUES(%s, %s, %s, %s)",
                    (account_id, survey_id, status, source_id)
                )
        else:
            # Else, upsert a status.
            with self._transaction.cursor() as cur:
                cur.execute(
                    "UPDATE "
                    "ag_login_surveys "
                    "SET "
                    "vioscreen_status = %s "
                    "WHERE "
                    "survey_id = %s",
                    (status, survey_id)
                )
                if cur.rowcount != 1:
                    raise NotFound("No such survey id: " + survey_id)

    def get_vioscreen_status(self, account_id, source_id, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "vioscreen_status "
                "FROM "
                "ag.ag_login_surveys "
                "WHERE "
                "ag_login_id = %s AND "
                "source_id = %s AND "
                "survey_id = %s",
                (account_id, source_id, survey_id,)
            )
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_vioscreen_status(self, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "vioscreen_status "
                "FROM "
                "ag.ag_login_surveys "
                "WHERE "
                "survey_id = %s",
                (survey_id,)
            )
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]
