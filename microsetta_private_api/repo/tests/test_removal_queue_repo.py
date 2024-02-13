import datetime
import unittest
from microsetta_private_api.repo.removal_queue_repo import RemovalQueueRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
from psycopg2.errors import InvalidTextRepresentation, ForeignKeyViolation
from microsetta_private_api.exceptions import RepoException


class RemovalQueueTests(unittest.TestCase):
    ACC_ID = '500d79fc-99e8-4c48-b911-a72005c9e0c9'
    ADM_ID = '500d79fc-99e8-4c48-b911-a72005c9e0ca'

    # a UUID generated from parts of existing UUIDs. Statistically
    # unlikely to be an existing account, but is of the correct
    # form.
    bad_id = '54a236d8-8439-48f2-b273-0c42fb82278c'

    def setUp(self):
        with Transaction() as t:
            acct_repo = AccountRepo(t)

            # Set up test account with sources
            self.acc = Account(RemovalQueueTests.ACC_ID,
                               "uniqueid@somedomain.org",
                               "standard",
                               "https://www.somedomain.org",
                               "1234ThisIsNotARealSub",
                               "Charles",
                               "C",
                               Address(
                                   "9500 Gilman Drive",
                                   "La Jolla",
                                   "CA",
                                   92093,
                                   "US"
                               ),
                               32.8798916,
                               -117.2363115,
                               False,
                               "en_US",
                               True)

            acct_repo.create_account(self.acc)

            self.adm = Account(RemovalQueueTests.ADM_ID,
                               "somebodyelse@somedomain.org",
                               "admin",
                               "https://www.somedomain2.org",
                               "1234ThisIsNotARealSub",
                               "Charles2",
                               "C2",
                               Address(
                                   "95002 Gilman Drive",
                                   "La Jolla",
                                   "CA",
                                   92093,
                                   "US"
                               ),
                               32.8798916,
                               -117.2363115,
                               False,
                               "en_US",
                               True)

            acct_repo.create_account(self.adm)

            t.commit()

    def tearDown(self):
        ids = (RemovalQueueTests.ACC_ID, RemovalQueueTests.ADM_ID)
        with Transaction() as t:
            cur = t.cursor()
            cur.execute("DELETE FROM ag.delete_account_queue WHERE account_id"
                        " in %s", (ids,))
            cur.execute("DELETE FROM ag.account_removal_log WHERE account_id"
                        " in %s", (ids,))
            t.commit()

        with Transaction() as t:
            acct_repo = AccountRepo(t)
            acct_repo.delete_account(self.acc.id)
            acct_repo.delete_account(self.adm.id)
            t.commit()

    def test_check_request_remove_account(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # this newly-generated account should not already be in the
            # queue. Confirm this is true.
            self.assertFalse(rqr.check_request_remove_account(self.acc.id))

            # use request_remove_account() to push the valid account onto
            # the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # assume request_remove_account() succeeded.
            # check_request_remove_account() should return True.
            self.assertTrue(rqr.check_request_remove_account(self.acc.id))

    def test_check_request_remove_account_invalid_ids(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # a UUID generated from parts of existing UUIDs. Statistically
            # unlikely to be an existing account, but is of the correct
            # form.
            bad_id = '54a236d8-8439-48f2-b273-0c42fb82278c'
            self.assertFalse(rqr.check_request_remove_account(bad_id))

            # request removal for an obviously invalid account_id.
            with self.assertRaises(InvalidTextRepresentation):
                rqr.check_request_remove_account('XXXX')

    def test_request_remove_account(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)
            # use request_remove_account() to push the valid account onto
            # the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # assume check_request_remove_account() works correctly.
            # verify account is now in the queue.
            self.assertTrue(rqr.check_request_remove_account(self.acc.id))

    def test_request_remove_account_failure(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # remove a valid account twice
            rqr.request_remove_account(self.acc.id, 'delete reason')
            with self.assertRaises(RepoException):
                rqr.request_remove_account(self.acc.id, 'delete reason')

            # remove a non-existant id.
            with self.assertRaises(ForeignKeyViolation):
                rqr.request_remove_account(RemovalQueueTests.bad_id,
                                           'delete reason')

    def test_cancel_request_remove_account(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)
            # use request_remove_account() to push the valid account onto
            # the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # assume check_request_remove_account() works correctly.
            # verify account is now in the queue.
            self.assertTrue(rqr.check_request_remove_account(self.acc.id))

            # cancel the request to delete the account.
            rqr.cancel_request_remove_account(self.acc.id)

            # verify account is not in the queue.
            self.assertFalse(rqr.check_request_remove_account(self.acc.id))

    def test_cancel_request_remove_account_failure(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # use request_remove_account() to push the valid account onto
            # the queue.
            with self.assertRaises(InvalidTextRepresentation):
                rqr.cancel_request_remove_account('XXXX')

        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # remove a non-existant id.
            with self.assertRaises(RepoException):
                rqr.cancel_request_remove_account(RemovalQueueTests.bad_id)

        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # use request_remove_account() to push the valid account onto
            # the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # cancel the request to delete the account twice.
            rqr.cancel_request_remove_account(self.acc.id)
            with self.assertRaises(RepoException):
                rqr.cancel_request_remove_account(self.acc.id)

    def test_update_queue_success(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # push the standard account onto the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # update_queue should migrate the relevant information to the
            # ag.account_removal_log table and delete the entry from the
            # queue table.
            rqr.update_queue(self.acc.id, self.adm.email, 'deleted',
                             'delete reason')

            # confirm that the account id is no longer in the queue table.
            self.assertFalse(rqr.check_request_remove_account(self.acc.id))

            t.commit()

        # confirm using SQL that the info exists in ag.account_removal_log.
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("SELECT account_id, admin_id, disposition, "
                            "requested_on, reviewed_on, delete_reason FROM "
                            "ag.account_removal_log")
                rows = cur.fetchall()
                self.assertEqual(len(rows), 1)
                for account_id, admin_id, disposition, requested_on,\
                        reviewed_on, delete_reason in rows:
                    # note this loop should only execute once.
                    self.assertEqual(account_id, self.acc.id)
                    self.assertEqual(admin_id, self.adm.id)
                    self.assertEqual(disposition, 'deleted')
                    self.assertEqual(delete_reason, 'delete reason')
                    now = datetime.datetime.now().timestamp()
                    # the requested_on time should be not far in the past.
                    # assume it is not NULL and is less than a minute ago.
                    self.assertLess(now - requested_on.timestamp(), 60)
                    # ditto for reviewed_on.
                    self.assertLess(now - reviewed_on.timestamp(), 60)

    def test_update_queue_failure(self):
        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            with self.assertRaises(InvalidTextRepresentation):
                rqr.update_queue('XXXX', self.adm.email, 'ignored', None)

        with Transaction() as t:
            rqr = RemovalQueueRepo(t)

            # push the standard account onto the queue.
            rqr.request_remove_account(self.acc.id, 'delete reason')

            # ensure that an Error is raised when an invalid admin
            # email address is passed.
            with self.assertRaises(RepoException):
                rqr.update_queue(self.acc.id, 'XXXX', 'ignored', None)

            # ensure that an Error is raised when disposition is None or
            # emptry string.
            with self.assertRaises(RepoException):
                rqr.update_queue(self.acc.id, self.adm.email, None, None)

            with self.assertRaises(RepoException):
                rqr.update_queue(self.acc.id, self.adm.email, '', None)
