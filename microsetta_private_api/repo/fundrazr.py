import json
import psycopg2
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.fundrazr import Payment


class UnknownItem(psycopg2.errors.ForeignKeyViolation):
    pass


class InvalidStatusChange(ValueError):
    pass


class UnknownTransaction(ValueError):
    pass


class FundRazr(BaseRepo):
    _ORDER = ('id', 'remote_campaign_id', 'created', 'amount', 'net_amount',
              'currency', 'fundrazr_status', 'payer_first_name',
              'payer_last_name', 'payer_email', 'account_type',
              'contact_email', 'subscribed_to_updates', 'phone_number',
              'message', 'tmi_status')

    _SHIPPING = ('shipping_first_name', 'shipping_last_name',
                 'shipping_address1', 'shipping_address2',
                 'shipping_city', 'shipping_country', 'shipping_state',
                 'shipping_postal')

    # enum statuses. status transitions as follows:
    # 1) a transaction regardless of anything, on when first entering the
    #    system a transaction is new (with no status), and immediately
    #    obtains a "received" status
    # 2) a transaction can move to valid-address once validated
    # 3) if the address is not valid, it moves to invalid-shipment
    # 4) if an invalid-address is corrected, and verified, it can become
    #    a valid-address
    # 5) only a valid-address can move to shipment-requested
    #
    # transactions without shipping or items will remain as received
    TMI_STATUS_NEW = None
    TMI_STATUS_RECEIVED = 'received'
    TMI_STATUS_VALID_ADDRESS = 'valid-address'
    TMI_STATUS_INVALID_ADDRESS = 'invalid-address'
    TMI_STATUS_SHIPMENT_REQUESTED = 'shipment-requested'

    def add_transaction(self, payment):
        """Adds a received transaction to the database

        Parameters
        ----------
        payment : Payment object
            An instantiated Payment model, with or without shipping
            and with or without claimed items

        Raises
        ------
        DuplicateTransaction
            If the transaction already exists

        Returns
        -------
        bool
            True if inserted
        """
        shipping = payment.shipping_address
        address = shipping.address if shipping is not None else None
        items = payment.claimed_items

        fields = self._ORDER
        data = (payment.transaction_id,
                payment.campaign_id,
                payment.created,
                payment.amount,
                payment.net_amount,
                payment.currency,
                payment.status,
                payment.payer_first_name,
                payment.payer_last_name,
                payment.payer_email,
                payment.account,
                payment.contact_email,
                payment.subscribe_to_updates,
                payment.phone_number,
                payment.message,
                self.TMI_STATUS_RECEIVED)

        if shipping is not None:
            fields += self._SHIPPING
            data += (shipping.first_name, shipping.last_name,
                     address.street, address.street2,
                     address.city, address.country_code,
                     address.state, address.post_code)

        placeholders = ', '.join(['%s'] * len(fields))
        fields_formatted = ', '.join(fields)
        sql = (f"""INSERT INTO barcodes.fundrazr_transaction
                   ({fields_formatted})
                   VALUES ({placeholders})""",
               data)

        with self._transaction.cursor() as cur:
            cur.execute(*sql)

            if items is not None:
                inserts = [(payment.transaction_id, i.id, i.quantity)
                           for i in items]
                try:
                    cur.executemany("""INSERT INTO
                                           barcodes.fundrazr_transaction_perk
                                       (transaction_id, perk_id, quantity)
                                       VALUES (%s, %s, %s)""",
                                    inserts)
                except psycopg2.errors.ForeignKeyViolation:
                    # this would indicate a synchronization issue, where
                    # fundrazr knows of a perk which we do not
                    detail = [i.to_api() for i in items]
                    raise UnknownItem(f"One or more perks are unknown:\n"
                                      f"{json.dumps(detail, indent=2)}")

        return True

    def update_transaction(self, payment):
        """Update the specific detail about a transaction

        We only allow update of shipping information for a transaction, which
        is necessary if an issue occurs during address verification.

        Notes
        -----
        Record existance is not asserted

        Parameters
        ----------
        payment : Payment object
            An instantiated Payment model, with or without shipping
            and with or without claimed items

        Raises
        ------
        DuplicateTransaction
            If the transaction already exists

        Returns
        -------
        bool
            True if updated, False otherwise
        """
        shipping = payment.shipping_address
        address = shipping.address if shipping is not None else None

        if address is None:
            return False

        fields = self._SHIPPING
        data = (shipping.first_name, shipping.last_name,
                address.street, address.street2,
                address.city, address.country_code,
                address.state, address.post_code,
                payment.transaction_id)

        fields_formatted = ','.join([f'{f}=%s' for f in fields])
        sql = (f"""UPDATE barcodes.fundrazr_transaction
                   SET {fields_formatted}
                   WHERE id=%s
                   RETURNING id""",
               data)

        with self._transaction.cursor() as cur:
            cur.execute(*sql)
            result = cur.fetchone()

        return len(result) == 1

    def set_transaction_status(self, payment, status):
        """Set the status of a transaction

        Parameters
        ----------
        payment : Payment object
            An instantiated Payment model, with or without shipping
            and with or without claimed items
        status : str
            One of ['received', 'valid-address', 'invalid-address',
            'shipment-requested']

        Raises
        ------
        InvalidStatusChange
            If an invalid transition is made, or an unknown status
            type is requested

        Returns
        -------
        Payment
            A copy of the input payment object with the revised status
            reflected
        """
        allowed_transitions = {
            self.TMI_STATUS_RECEIVED: (self.TMI_STATUS_VALID_ADDRESS,
                                       self.TMI_STATUS_INVALID_ADDRESS),
            self.TMI_STATUS_VALID_ADDRESS: (self.TMI_STATUS_SHIPMENT_REQUESTED, ),  # noqa
            self.TMI_STATUS_INVALID_ADDRESS: (self.TMI_STATUS_VALID_ADDRESS, ),
            self.TMI_STATUS_SHIPMENT_REQUESTED: tuple()
        }

        if status not in (self.TMI_STATUS_RECEIVED,
                          self.TMI_STATUS_VALID_ADDRESS,
                          self.TMI_STATUS_INVALID_ADDRESS,
                          self.TMI_STATUS_SHIPMENT_REQUESTED):
            raise InvalidStatusChange(f"Unrecognized status: {status}")

        # do not trust the instance, get the actual current status
        sql = ("""SELECT tmi_status
                  FROM barcodes.fundrazr_transaction
                  WHERE id=%s""",
               (payment.transaction_id, ))
        with self._transaction.cursor() as cur:
            cur.execute(*sql)
            res = cur.fetchone()

        if len(res) == 0:
            return UnknownTransaction(f"Transaction {payment.transaction_id} "
                                      "does not exist")
        current_status = res[0]
        if status not in allowed_transitions[current_status]:
            raise InvalidStatusChange(f"From '{current_status}' to '{status}'")

        sql = ("""UPDATE barcodes.fundrazr_transaction
                  SET tmi_status=%s
                  WHERE id=%s""",
               (status, payment.transaction_id))

        with self._transaction.cursor() as cur:
            cur.execute(*sql)

        payment = payment.copy()
        payment.tmi_status = status
        return payment

    def get_transactions(self, before=None, after=None, transaction_id=None,
                         tmi_status=None, contact_email=None):
        """Somewhat flexible getter for transactions

        Parameters
        ----------
        before : datetime, optional
            Limit transactions to before a specific date
        after : datetime, optional
            Limit transactions to after a specific date
        transaction_id : str, optional
            Limit to a specific transaction ID
        tmi_status : str, optional
            Limit based on a particular status
        contact_email : str, optional
            Limit by a persons contact email

        Returns
        -------
        list of Payment
            A list of constructed Payment instances
        """
        empty = [q is None for q in [before, after, transaction_id,
                                     tmi_status, contact_email]]
        if all(empty):
            # nothing to do...
            return []

        clauses = []
        data = []
        if before is not None:
            clauses.append("created < %s")
            data.append(before)
        if after is not None:
            clauses.append("created > %s")
            data.append(after)
        if transaction_id is not None:
            clauses.append("id = %s")
            data.append(transaction_id)
        if tmi_status is not None:
            clauses.append("tmi_status = %s")
            data.append(tmi_status)
        if contact_email is not None:
            clauses.append("contact_email = %s")
            data.append(contact_email)

        clauses = ' AND '.join(clauses)

        sql = (f"""SELECT id
                   FROM barcodes.fundrazr_transaction
                   WHERE {clauses}""",
               tuple(data))

        with self._transaction.cursor() as cur:
            cur.execute(*sql)
            res = cur.fetchall()

        return [self._payment_from_transaction(id_) for id_ in res]

    def _payment_from_transaction(self, id_):
        """Construct a payment instance from a transaction ID"""
        fields = self._ORDER + self._SHIPPING
        fields_formatted = ','.join(fields)
        transaction_sql = (f"""SELECT {fields_formatted}
                               FROM barcodes.fundrazr_transaction
                               WHERE id=%s
                               ORDER BY created""",
                           (id_, ))
        items_sql = ("""SELECT *
                        FROM barcodes.fundrazr_transaction_perk
                        WHERE transaction_id=%s""",
                     (id_, ))

        with self._transaction.dict_cursor() as cur:
            cur.execute(*transaction_sql)
            trn = cur.fetchone()

            cur.execute(*items_sql)
            items = cur.fetchall()

        if len(items) == 0:
            items = None

        return Payment.from_db(trn, items)
