from __future__ import print_function
import datetime
import os.path
from flask import Flask, render_template
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(service, calendar_id):
    print("Criar um novo evento:")
    event_name = input("Nome do evento: ")
    event_description = input("Descrição do evento: ")
    event_start_date = input("Data de início (YYYY-MM-DD): ")
    event_start_time = input("Hora de início (HH:MM): ")
    event_end_date = input("Data de término (YYYY-MM-DD): ")
    event_end_time = input("Hora de término (HH:MM): ")

    event_start_datetime = f"{event_start_date}T{event_start_time}:00"
    event_end_datetime = f"{event_end_date}T{event_end_time}:00"

    event = {
        'summary': event_name,
        'description': event_description,
        'start': {
            'dateTime': event_start_datetime,
            'timeZone': 'UTC',  # Defina o fuso horário apropriado
        },
        'end': {
            'dateTime': event_end_datetime,
            'timeZone': 'UTC',  # Defina o fuso horário apropriado
        },
    }

    created_event = service.events().insert(calendarId= calendar_id, body=event).execute()
    print(f'Evento criado: {created_event["htmlLink"]}')

def main(calendar_id):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='frc8276@gmail.com', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        else:
            print('Próximos eventos:')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

        # Chamar a função para criar um evento
        create_event(service, 'frc8276@gmail.com')
    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    calendar_id = 'frc8276@gmail.com'
    main(calendar_id)
