import json

import psycopg2
import unittest

from microsetta_private_api.model.log_event import LogEvent, EventType, \
    EventSubtype
from microsetta_private_api.repo.activation_repo import ActivationRepo
from microsetta_private_api.repo.event_log_repo import EventLogRepo
from microsetta_private_api.repo.transaction import Transaction

import uuid

from microsetta_private_api.util.util import json_converter


class ActivationRepoTests(unittest.TestCase):
    def test_activate(self):
        with Transaction() as t:
            activations = ActivationRepo(t)
            email1 = "foo@baz.com"
            email2 = "bar@baz.com"

            code1 = activations.get_activation_code(email1)
            code2 = activations.get_activation_code(email2)

            self.assertFalse(activations.use_activation_code(email1, code2))
            self.assertFalse(activations.use_activation_code(email2, code1))

            self.assertTrue(activations.use_activation_code(email1, code1))
            self.assertTrue(activations.use_activation_code(email2, code2))

            self.assertFalse(activations.use_activation_code(email1, code1))
            self.assertFalse(activations.use_activation_code(email2, code2))
            t.rollback()

    def test_return_code_from_db(self):
        with Transaction() as t:
            activations = ActivationRepo(t)
            email1 = "foo@baz.com"
            code1 = activations.get_activation_code(email1)
            code2 = activations.get_activation_code(email1)
            self.assertEqual(code1,code2)
            t.rollback()

    def test_code_nondeterminism(self):
        email1 = "foo@baz.com"
        with Transaction() as t:
            activations = ActivationRepo(t)
            code1 = activations.get_activation_code(email1)
            t.rollback()
        with Transaction() as t:
            activations = ActivationRepo(t)
            code2 = activations.get_activation_code(email1)
            t.rollback()
        self.assertNotEqual(code1, code2)
