'''
This is an example of how to send data to Slack webhooks in Python with the
requests module.
Detailed documentation of Slack Incoming Webhooks:
https://api.slack.com/incoming-webhooks
'''

import json
import requests

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
# event = "robot1_on"
event = "robot1_off"
event = "robot1_color"
webhook_url = 'https://maker.ifttt.com/trigger/'+event+'/with/key/<KEY>'

data = {'Value1': "#ff0000"}

response = requests.post(
    webhook_url, data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

if response.status_code != 200:
    raise ValueError(
        'Request to ifttt returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
