import defs
import UI
import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']  #Google scope for calendar

CLIENT_file = 'automation.json'  #Your google OAuth2.0 .json file

creds = None

if os.path.exists('token.json'):#checks if user has already allowed program to use google api
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

if not creds  or not creds.valid:#if user haven't done it yet pop-up window will apear where user has to allow program to use google api
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())  # uus kommentti
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_file, SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

def main():
    ui = UI.RegistrationForm()
    ui.run()  #open UI
    
    scraper = defs.ShiftScraper()  #runs class where are all the funktion
    service = build('calendar', 'v3', credentials=creds)  #builds request for google calendar
    
    scraper.login()  #logins into a website
    
    shifts = scraper.get_shifts()  #get list of shifts
    dates = scraper.get_dates()  #get list on dates 
    
    scraper.quit()  #closes website

    x = 0

    for i in shifts:  #for every date in three week period checks if there is a shift
        if i != -1:  #if there is creates event and sends it to google calendar
            start_hour = str(i[:2])
            start_minute = str(i[2:4])  #gets starting hour, minute etc.
            end_hour = str(i[5:7])
            end_minute = str(i[7:9])
            
            date = scraper.change_format(dates[x])  #changes date format to Y.m.d from d.m.Y, it does it only here because i prefere d.m.Y format more
            
            if end_hour < start_hour:  #if shift is continues over midnight shifts ending date changes
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                next_day = date_obj + timedelta(days=1)
                next_day_str = scraper.change_format(next_day.strftime("%d.%m.%Y"))
                
                event = {  #creates event if it is a night shift
                    'summary': 'Work',
                    'start': {'dateTime': f'{date}T{start_hour}:{start_minute}:00+03:00',
                        'timeZone': 'Europe/Helsinki',
                        },
                    'end': {'dateTime': f'{next_day_str}T{end_hour}:{end_minute}:00+03:00',
                        'timeZone': 'Europe/Helsinki',
                        },
                    }
            else:
                event = {  #creates event if it is not a night shift
                    'summary': 'Work',
                    'start': {'dateTime': f'{date}T{start_hour}:{start_minute}:00+03:00',
                        'timeZone': 'Europe/Helsinki',
                        },
                    'end': {'dateTime': f'{date}T{end_hour}:{end_minute}:00+03:00',
                        'timeZone': 'Europe/Helsinki',
                        },
                    }
            e = service.events().insert(calendarId='primary', body=event).execute()  #sends event to google calendar
            print ('Event created: %s' % (e.get('htmlLink')))  #prints errors
        x += 1
    
if __name__ == "__main__":
    main()
