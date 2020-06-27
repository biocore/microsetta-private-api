import json

import psycopg2
import unittest

from microsetta_private_api.model.log_event import LogEvent, EventType, \
    EventSubtype
from microsetta_private_api.repo.event_log_repo import EventLogRepo
from microsetta_private_api.repo.transaction import Transaction

import uuid

from microsetta_private_api.util.util import json_converter, fromisotime


class EventLogTests(unittest.TestCase):
    def test_event_log(self):
        event_id = uuid.uuid4()
        acct_id = uuid.uuid4()
        event = LogEvent(
            event_id,
            EventType.EMAIL,
            EventSubtype.EMAIL_BANKED_SAMPLE_NOW_PLATED,
            None,
            {
                "email": "foobarbaz@kasdgklhasg.com",
                "account_id": str(acct_id),
                "blahblah": "Blah blah blah",
                "ski": "ball"
            }
        )

        with Transaction() as t:
            events = EventLogRepo(t)

            insertion = events.add_event(event)
            self.assertTrue(insertion)

            # Check full event log
            self.assertEqual(events.get_events()[0].event_id, event_id)

            # Check event log filtered by primary type
            primary_type = events.get_events_by_type(EventType.EMAIL)[0]
            self.assertEqual(primary_type.event_id, event_id)

            # Check fields
            client_obj = json.loads(json.dumps(primary_type.to_api(),
                                    default=json_converter))
            self.assertEqual(client_obj['event_id'], str(event_id))
            self.assertEqual(client_obj['event_type'],
                             EventType.EMAIL.value)
            self.assertEqual(client_obj['event_subtype'],
                             EventSubtype.EMAIL_BANKED_SAMPLE_NOW_PLATED.value)
            self.assertEqual(client_obj['event_state']['ski'], 'ball')

            # Check event log filtered by subtype
            subtype = events.get_events_by_subtype(
                EventType.EMAIL,
                EventSubtype.EMAIL_BANKED_SAMPLE_NOW_PLATED)[0]
            self.assertEqual(subtype.event_id, event_id)

            # Check event log filtered by exact email
            exact = events.get_events_by_email("foobarbaz@kasdgklhasg.com")[0]
            self.assertEqual(exact.event_id, event_id)

            # Check event log filtered by email prefix
            partial = events.get_events_by_email("foobarbaz@ka")[0]
            self.assertEqual(partial.event_id, event_id)

            # Check event log filtered by account
            acct = events.get_events_by_account(acct_id)[0]
            self.assertEqual(acct.event_id, event_id)

            # Check event can be deleted
            deletion = events.delete_event(event_id)
            self.assertTrue(deletion)

            # Check event is no longer there
            all = events.get_events()
            if len(all) > 0:
                assert all[0].event_id != event_id
            t.rollback()

    def test_dups_rejected(self):
        event = LogEvent(
            uuid.uuid4(),
            EventType.EMAIL,
            EventSubtype.EMAIL_BANKED_SAMPLE_NOW_PLATED,
            None,
            {}
        )
        with Transaction() as t:
            events = EventLogRepo(t)
            events.add_event(event)
            with self.assertRaises(psycopg2.errors.UniqueViolation):
                events.add_event(event)
            t.rollback()
