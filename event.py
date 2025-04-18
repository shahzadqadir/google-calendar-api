import json
from datetime import datetime

class Event:
    """Implement Google Calendar event for easy comparing and display"""
    def __init__(self, event_json: json):
        self.creator_email = event_json['creator']['email']
        self.summary = event_json['summary']
        self.start_date = datetime.fromisoformat(event_json['start']['dateTime']).date()
        self.start_time = datetime.fromisoformat(event_json['start']['dateTime']).time()
        self.end_date = datetime.fromisoformat(event_json['end']['dateTime']).date()
        self.end_time = datetime.fromisoformat(event_json['end']['dateTime']).time()

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
