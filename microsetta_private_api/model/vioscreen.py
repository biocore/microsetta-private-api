import pandas as pd
from microsetta_private_api.model.model_base import ModelBase


def normalize_timestamp(timestamp, timezone, normalize_to='US/Pacific'):
    """Normalize a timestamp to a specific timezone
    Vioscreen timezone information is not encoded directly within the
    timestamp, but separately.
    Parameters
    ----------
    timestamp : str
        The timestamp to normalize
    timezone : str
        The timezone information as provided by vioscreen
    normalize_to : str
        What timezone to normalize too, using Pandas timezone conventions
    Returns
    -------
    pd.Timestamp
        A normalized timestamp
    """
    timezone_lookup = {'Eastern Standard Time': 'US/Eastern',
                       'Central Standard Time': 'US/Central',
                       'Pacific Standard Time': 'US/Pacific'}

    if timezone not in timezone_lookup:
        raise KeyError(f"Unexpected timezone '{timezone}' observed")
    if timestamp is None:
        return None

    timestamp = pd.to_datetime(timestamp)
    timestamp_tz = timestamp.tz_localize(timezone_lookup[timezone])
    return timestamp_tz.tz_convert(normalize_to)


class VioscreenSession(ModelBase):
    def __init__(self, sessionId, username, protocolId, status, startDate,
                 endDate, cultureCode, created, modified):
        self.sessionId = sessionId
        self.username = username
        self.protocolId = protocolId
        self.status = status
        self.startDate = startDate
        self.endDate = endDate
        self.cultureCode = cultureCode
        self.created = created
        self.modified = modified

    def update_from_vioscreen(self, update):
        self.startDate = update.startDate
        self.endDate = update.endDate
        self.modified = update.modified
        self.status = update.status
        self.protocolId = update.protocolId
        self.cultureCode = update.cultureCode
        self.created = update.created
        return self

    @property
    def is_complete(self):
        return (self.endDate is not None) and (self.status == 'Finished')

    @classmethod
    def from_registry(cls, username):
        # Support the special case of a username existing in the
        # vioscreen_registry but not yet existing in the vioscreen_sessions
        # table
        return cls(sessionId=None, username=username, protocolId=None,
                   status=None, startDate=None, endDate=None, cultureCode=None,
                   created=None, modified=None)

    @classmethod
    def from_vioscreen(cls, sessions_data, users_data):
        timeZone = users_data['timeZone']
        startDate = normalize_timestamp(sessions_data['startDate'], timeZone)
        endDate = normalize_timestamp(sessions_data['endDate'], timeZone)
        created = normalize_timestamp(sessions_data['created'], timeZone)
        modified = normalize_timestamp(sessions_data['modified'], timeZone)

        return cls(sessions_data['sessionId'], sessions_data['username'],
                   sessions_data['protocolId'], sessions_data['status'],
                   startDate, endDate, sessions_data['cultureCode'],
                   created, modified)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'username': self.username,
            'protocolId': self.protocolId,
            'status': self.status,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'cultureCode': self.cultureCode,
            'created': self.created,
            'modified': self.modified
        }

    def __repr__(self):
        args = ", ".join([f"{key}={str(value)}"
                          for key, value in self.__dict__.items()])
        return f"VioscreenSession({args})"


class VioscreenPercentEnergyComponent(ModelBase):
    def __init__(self, code, description, short_description, units, amount):
        self.code = code
        self.description = description
        self.short_description = short_description
        self.units = units
        self.amount = amount

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['code'], component['description'],
                   component['shortDescription'], component['units'],
                   component['amount'])

    def to_api(self):
        return {
            'code': self.code,
            'description': self.description,
            'shortDescription': self.short_description,
            'units': self.units,
            'amount': self.amount
        }

    def __lt__(self, other):
        return self.code < other.code


class VioscreenPercentEnergy(ModelBase):
    def __init__(self, sessionId, energy_components):
        self.sessionId = sessionId
        self.energy_components = energy_components

    @classmethod
    def from_vioscreen(cls, pe_data):
        sessionId = pe_data['sessionId']

        energy_components = [
            VioscreenPercentEnergyComponent.from_vioscreen(component)
            for component in pe_data['calculations']
        ]

        return cls(sessionId, energy_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'calculations': [component.to_api()
                             for component in self.energy_components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.energy_components)
        b = sorted(other.energy_components)

        return a == b


class VioscreenDietaryScoreComponent(ModelBase):
    def __init__(self, code, name, score, lowerLimit, upperLimit):
        self.code = code
        self.name = name
        self.score = score
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['type'], component['name'], component['score'],
                   component['lowerLimit'], component['upperLimit'])

    def to_api(self):
        return {
            'type': self.code,
            'name': self.name,
            'score': self.score,
            'lowerLimit': self.lowerLimit,
            'upperLimit': self.upperLimit
        }

    def __lt__(self, other):
        return self.code < other.code


class VioscreenDietaryScore(ModelBase):
    def __init__(self, sessionId, scoresType, scores):
        self.sessionId = sessionId
        self.scoresType = scoresType
        self.scores = scores

    @classmethod
    def from_vioscreen(cls, ds_data):
        sessionId = ds_data['sessionId']
        scoresType = ds_data['dietaryScore']['type']

        scores = [
            VioscreenDietaryScoreComponent.from_vioscreen(component)
            for component in ds_data['dietaryScore']['scores']
        ]

        return cls(sessionId, scoresType, scores)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'type': self.scoresType,
            'scores': [component.to_api()
                       for component in self.scores]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        if self.scoresType != other.scoresType:
            return False

        a = sorted(self.scores)
        b = sorted(other.scores)

        return a == b


class VioscreenSupplementsComponent(ModelBase):
    def __init__(self, supplement, frequency, amount, average):
        self.supplement = supplement
        self.frequency = frequency
        self.amount = amount
        self.average = average

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['supplement'], component['frequency'],
                   component['amount'], component['average'])

    def to_api(self):
        return {
            'supplement': self.supplement,
            'frequency': self.frequency,
            'amount': self.amount,
            'average': self.average
        }

    def __lt__(self, other):
        return self.supplement < other.supplement


class VioscreenSupplements(ModelBase):
    def __init__(self, sessionId, supplements_components):
        self.sessionId = sessionId
        self.supplements_components = supplements_components

    @classmethod
    def from_vioscreen(cls, supplements_data):
        sessionId = supplements_data['sessionId']

        supplements_components = [
            VioscreenSupplementsComponent.from_vioscreen(component)
            for component in supplements_data['data']
        ]

        return cls(sessionId, supplements_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'data': [component.to_api()
                     for component in self.supplements_components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.supplements_components)
        b = sorted(other.supplements_components)

        return a == b


class VioscreenFoodComponentsComponent(ModelBase):
    def __init__(self, code, description, units, amount, valueType):
        self.code = code
        self.description = description
        self.units = units
        self.amount = amount
        self.valueType = valueType

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['code'], component['description'],
                   component['units'], component['amount'],
                   component['valueType'])

    def to_api(self):
        return {
            'code': self.code,
            'description': self.description,
            'units': self.units,
            'amount': self.amount,
            'valueType': self.valueType
        }

    def __lt__(self, other):
        return self.code < other.code


class VioscreenFoodComponents(ModelBase):
    def __init__(self, sessionId, components):
        self.sessionId = sessionId
        self.components = components

    @classmethod
    def from_vioscreen(cls, fc_data):
        sessionId = fc_data['sessionId']

        food_components = [
            VioscreenFoodComponentsComponent.from_vioscreen(component)
            for component in fc_data['data']
        ]

        return cls(sessionId, food_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'data': [component.to_api()
                     for component in self.components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.components)
        b = sorted(other.components)

        return a == b


class VioscreenEatingPatternsComponent(ModelBase):
    def __init__(self, code, description, units, amount, valueType):
        self.code = code
        self.description = description
        self.units = units
        self.amount = amount
        self.valueType = valueType

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['code'], component['description'],
                   component['units'], component['amount'],
                   component['valueType'])

    def to_api(self):
        return {
            'code': self.code,
            'description': self.description,
            'units': self.units,
            'amount': self.amount,
            'valueType': self.valueType
        }

    def __lt__(self, other):
        return self.code < other.code


class VioscreenEatingPatterns(ModelBase):
    def __init__(self, sessionId, components):
        self.sessionId = sessionId
        self.components = components

    @classmethod
    def from_vioscreen(cls, ep_data):
        sessionId = ep_data['sessionId']

        ep_components = [
            VioscreenEatingPatternsComponent.from_vioscreen(component)
            for component in ep_data['data']
        ]

        return cls(sessionId, ep_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'data': [component.to_api()
                     for component in self.components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.components)
        b = sorted(other.components)

        return a == b


class VioscreenMPedsComponent(ModelBase):
    def __init__(self, code, description, units, amount, valueType):
        self.code = code
        self.description = description
        self.units = units
        self.amount = amount
        self.valueType = valueType

    @classmethod
    def from_vioscreen(cls, component):
        return cls(component['code'], component['description'],
                   component['units'], component['amount'],
                   component['valueType'])

    def to_api(self):
        return {
            'code': self.code,
            'description': self.description,
            'units': self.units,
            'amount': self.amount,
            'valueType': self.valueType
        }

    def __lt__(self, other):
        return self.code < other.code


class VioscreenMPeds(ModelBase):
    def __init__(self, sessionId, components):
        self.sessionId = sessionId
        self.components = components

    @classmethod
    def from_vioscreen(cls, mp_data):
        sessionId = mp_data['sessionId']

        mp_components = [
            VioscreenMPedsComponent.from_vioscreen(component)
            for component in mp_data['data']
        ]

        return cls(sessionId, mp_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'data': [component.to_api()
                     for component in self.components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.components)
        b = sorted(other.components)

        return a == b


class VioscreenFoodConsumptionComponent(ModelBase):
    def __init__(self, foodCode, description, foodGroup, amount, frequency,
                 consumptionAdjustment, servingSizeText, servingFrequencyText,
                 created, data):
        self.foodCode = foodCode
        self.description = description
        self.foodGroup = foodGroup
        self.amount = amount
        self.frequency = frequency
        self.consumptionAdjustment = consumptionAdjustment
        self.servingSizeText = servingSizeText
        self.servingFrequencyText = servingFrequencyText
        self.created = created
        # data is a list of individual VioscreenFoodComponentsComponent objects
        self.data = data

    def __repr__(self):
        parts = ', '.join([f"{k}={v}"
                           for k, v in sorted(self.__dict__.items())
                           if k != 'data'])
        return "<%s>" % parts

    @classmethod
    def from_vioscreen(cls, component):
        data = [
            VioscreenFoodComponentsComponent.from_vioscreen(component2)
            for component2 in component['data']
        ]

        return cls(component['foodCode'], component['description'],
                   component['foodGroup'], component['amount'],
                   component['frequency'], component['consumptionAdjustment'],
                   component['servingSizeText'],
                   component['servingFrequencyText'], component['created'],
                   data)

    def to_api(self):
        return {
            'foodCode': self.foodCode,
            'description': self.description,
            'foodGroup': self.foodGroup,
            'amount': self.amount,
            'frequency': self.frequency,
            'consumptionAdjustment': self.consumptionAdjustment,
            'servingSizeText': self.servingSizeText,
            'servingFrequencyText': self.servingFrequencyText,
            'created': self.created,
            'data': [component.to_api()
                     for component in self.data]
        }

    def __lt__(self, other):
        return self.description < other.description

    def __eq__(self, other):
        for k in self.__dict__:
            if k == 'data':
                continue
            if self.__dict__[k] != other.__dict__[k]:
                return False

        self_data = sorted(self.data)
        other_data = sorted(other.data)

        return self_data == other_data


class VioscreenFoodConsumption(ModelBase):
    def __init__(self, sessionId, components):
        self.sessionId = sessionId
        self.components = components

    @classmethod
    def from_vioscreen(cls, cons_data):
        sessionId = cons_data['sessionId']

        cons_components = [
            VioscreenFoodConsumptionComponent.from_vioscreen(component)
            for component in cons_data['foodConsumption']
        ]

        return cls(sessionId, cons_components)

    def to_api(self):
        return {
            'sessionId': self.sessionId,
            'foodConsumption': [component.to_api()
                                for component in self.components]
        }

    def __eq__(self, other):
        if self.sessionId != other.sessionId:
            return False

        a = sorted(self.components)
        b = sorted(other.components)

        return a == b


class VioscreenComposite(ModelBase):
    def __init__(self, session, percent_energy, dietary_scores, supplements,
                 food_components, eating_patterns, mpeds, food_consumption):
        self.session = session
        self.percent_energy = percent_energy
        self.dietary_scores = dietary_scores
        self.supplements = supplements
        self.food_components = food_components
        self.eating_patterns = eating_patterns
        self.mpeds = mpeds
        self.food_consumption = food_consumption

        # make first class as the vioscreen username is our internal
        # survey identifier
        self.vio_id = session.username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
