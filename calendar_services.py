import datetime
import os
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
]

class GoogleCalendarAPI:
    
    def __init__(self):
        creds = None
        if not creds or not creds.valid:
            creds = service_account.Credentials.from_service_account_file(
                os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE'),
                scopes=['https://www.googleapis.com/auth/calendar']
            )
        self.service = build('calendar', 'v3', credentials=creds)

    def view_events(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = self.service.events().list(
            calendarId='sync.shahzadqadir@gmail.com',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        for event in events:
            print(event)

    def add_event_to_google_calendar(self, summary: str, description: str='', start: datetime=datetime.datetime.now().isoformat(),
                  end: datetime=(datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(), colorId: str='8'):
        event = {
            'summary': f'{summary}',
            'description': f'{description}',
            'start': {
                'dateTime': str(start),
                'timeZone': 'Europe/London',
                },
            'end': {
                'dateTime': str(end),
                'timeZone': 'Europe/London',
                },
            'colorId': colorId,
            }
        event_result = self.service.events().insert(calendarId='sync.shahzadqadir@gmail.com', body=event).execute()
        print(f'Event created: {event_result.get("htmlLink")}')



if __name__ == "__main__":
    test = GoogleCalendarAPI()
    test.add_event_to_google_calendar(summary='Test Meeting 1')
