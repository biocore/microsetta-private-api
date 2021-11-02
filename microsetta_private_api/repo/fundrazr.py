import json
import psycopg2
from microsetta_private_api.repo.base_repo import BaseRepo


class UnknownItem(psycopg2.errors.ForeignKeyViolation):
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

    TMI_STATUS_RECEIVED = 'received'

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
