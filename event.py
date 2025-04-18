import json
from datetime import datetime

class Event:
    """Implement Google Calendar event for easy comparing and display"""
    def __init__(self, event_json: json = None,
                 creator_email: str='sync.shahzadqadir@gmail.com',
                 summary: str='',
                 start_date: datetime.date = '',
                 end_date: datetime.date = '',
                 start_time: datetime.time='',
                 end_time: datetime.time = '',
                 ):
        if event_json is not None:
            self.creator_email = event_json['creator']['email']
            self.summary = event_json['summary']
            self.start_date = datetime.fromisoformat(event_json['start']['dateTime']).date()
            self.start_time = datetime.fromisoformat(event_json['start']['dateTime']).time()
            self.end_date = datetime.fromisoformat(event_json['end']['dateTime']).date()
            self.end_time = datetime.fromisoformat(event_json['end']['dateTime']).time()
        else:
            self.creator_email = creator_email
            self.summary = summary
            self.start_date = start_date
            self.end_date = end_date
            self.start_time = start_time
            self.end_time = end_time


    def __str__(self):
        return self.summary

    def __gt__(self, other):
        """Greater means later in this context."""
        if self.start_date == other.start_date:
            return self.start_time > other.start_time
        return self.start_date > other.start_date

    def __le__(self, other):
        if self.start_date == other.start_date:
            return self.start_time < other.start_time
        return self.start_date < other.start_date
