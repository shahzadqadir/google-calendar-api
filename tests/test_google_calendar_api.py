import datetime
from unittest import TestCase

from calendar_services import GoogleCalendarAPI
from event import Event


class TestGoogleCalendarAPI(TestCase):

    def setUp(self):
        self.calendar = GoogleCalendarAPI()


    def test_create_event(self):
        event = Event(
            summary='test event - 18Apr25-1828', start_date=datetime.datetime.now().date(),
            end_date=datetime.datetime.now().date(),
            start_time=datetime.datetime.now().time(),
            end_time=(datetime.datetime.now() + datetime.timedelta(hours=1)).time(),
            )
        self.calendar.add_event_to_google_calendar(
            event.summary, start=(datetime.datetime.combine(event.start_date, event.start_time)).isoformat(),
            end=(datetime.datetime.combine(event.end_date, event.end_time)).isoformat()
            )
        events = self.calendar.view_events()
