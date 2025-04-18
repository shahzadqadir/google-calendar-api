from unittest import TestCase
from event import Event

class TestEvent(TestCase):

    def setUp(self):
        self.event = Event(
            {'kind': 'calendar#event', 'etag': '"3483900261288766"',
             'id': 'coo64dpp61j30b9n6com6b9k70ojab9oc4p62b9n6gp34d356lh3cd9o70', 'status': 'confirmed',
             'htmlLink': 'https://www.google.com/calendar/event?eid=Y29vNjRkcHA2MWozMGI5bjZjb202YjlrNzBvamFiOW9jNHA2MmI5bjZncDM0ZDM1NmxoM2NkOW83MCBzeW5jLnNoYWh6YWRxYWRpckBt',
             'created': '2025-03-14T11:02:10.000Z', 'updated': '2025-03-14T11:02:10.644Z',
             'summary': 'Community Mental Health', 'creator': {'email': 'sync.shahzadqadir@gmail.com', 'self': True},
             'organizer': {'email': 'sync.shahzadqadir@gmail.com', 'self': True},
             'start': {'dateTime': '2025-04-30T11:30:00+01:00', 'timeZone': 'Europe/London'},
             'end': {'dateTime': '2025-04-30T12:30:00+01:00', 'timeZone': 'Europe/London'},
             'iCalUID': 'coo64dpp61j30b9n6com6b9k70ojab9oc4p62b9n6gp34d356lh3cd9o70@google.com', 'sequence': 0,
             'reminders': {'useDefault': True}, 'eventType': 'default'}
            )
        self.event2 = Event(
            {'kind': 'calendar#event', 'etag': '"3483900261288766"',
             'id': 'coo64dpp61j30b9n6com6b9k70ojab9oc4p62b9n6gp34d356lh3cd9o70', 'status': 'confirmed',
             'htmlLink': 'https://www.google.com/calendar/event?eid=Y29vNjRkcHA2MWozMGI5bjZjb202YjlrNzBvamFiOW9jNHA2MmI5bjZncDM0ZDM1NmxoM2NkOW83MCBzeW5jLnNoYWh6YWRxYWRpckBt',
             'created': '2025-03-14T11:02:10.000Z', 'updated': '2025-03-14T11:02:10.644Z',
             'summary': 'Community Mental Health', 'creator': {'email': 'sync.shahzadqadir@gmail.com', 'self': True},
             'organizer': {'email': 'sync.shahzadqadir@gmail.com', 'self': True},
             'start': {'dateTime': '2025-04-30T11:45:00+01:00', 'timeZone': 'Europe/London'},
             'end': {'dateTime': '2025-04-30T12:30:00+01:00', 'timeZone': 'Europe/London'},
             'iCalUID': 'coo64dpp61j30b9n6com6b9k70ojab9oc4p62b9n6gp34d356lh3cd9o70@google.com', 'sequence': 0,
             'reminders': {'useDefault': True}, 'eventType': 'default'}
            )

    def test_event_creation(self):
        self.assertEqual(self.event.__str__(), 'Community Mental Health')
        self.assertEqual(str(self.event.start_time), '11:30:00')
        self.assertEqual(str(self.event.end_time), '12:30:00')

    def test_event_comparison(self):
        self.assertGreater(self.event2, self.event, 'event 1 comes first')
        self.assertLess(self.event, self.event2, 'event 1 comes first')
