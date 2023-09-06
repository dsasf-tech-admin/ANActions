import os
import datetime
from parsons import ActionNetwork

# Load API key from environment variable
api_key = os.environ['AN_API_KEY']

# Instantiate the class
an = ActionNetwork(api_key)

# Get a list of all events
events = an._get_entry_list('events')

#Loading a month of calendar events to populate frontend calendar
this_month = datetime.datetime.now() - datetime.timedelta(days=30)
print(this_month)

for event in events:
    event['start_date'] = event['start_date'].split('T')[0]
    event['start_date'] = datetime.datetime.strptime(event['start_date'], '%Y-%m-%d')
    if event['start_date'] >= this_month:
        print(event['title'], event['start_date'])
