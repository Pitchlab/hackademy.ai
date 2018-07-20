#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.audio
import aiy.voicehat
from google.assistant.library.event import EventType

import json
import requests

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

def send_to_slack(text):
    webhook_url = 'https://hooks.slack.com/services/<KEY>'
    slack_data = {'text': text}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

def send_to_ifttt(event):
    webhook_url = 'https://maker.ifttt.com/trigger/'+event+'/with/key/<KEY>'
    print(webhook_url)

    response = requests.post(
        webhook_url,
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

def sound(type):
    print('playing',type)
    path = '/home/pi/hackademy.ai/hackathons/hackathon_1_voice/resources/startrek/'
    file = ''
    if (type == 'acknowledge'):
        file = "voiceinput4.wav"
    elif (type == 'comply'):
        file = "voiceinput3.wav"
    elif (type == 'error'):
        file = "scrclose1.wav"
    elif (type == 'ready'):
        file = "inputfailed1.wav"

    print(path, file)
    aiy.audio.play_wave(path+file)

def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    # The assistant got 'ok google' and now recognizes speech
    #
    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        sound('acknowledge')
        status_ui.status('listening')

    # The assistant got some speech, let's see what it can do
    #
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            sound('comply')
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            sound('comply')
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'computer':
            assistant.stop_conversation()
            sound('acknowledge')
        elif text == 'lights on':
            assistant.stop_conversation()
            send_to_ifttt('robot1_on')
            sound('comply')
        elif text == 'lights off':
            assistant.stop_conversation()
            send_to_ifttt('robot1_off')
            sound('comply')
        elif text.find('slack')==0:
            assistant.stop_conversation()
            print('slacking!', text.lstrip('slack'))
            send_to_slack(text.lstrip('slack'))
            sound('comply')
        # else:
        #     # No command...
        #     sound('ready')

    # Once the command is finished, let the user know
    #
    elif event.type == EventType.ON_END_OF_UTTERANCE:
        # sound('comply')
        status_ui.status('thinking')

    #
    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        # if (event.type == EventType.ON_NO_RESPONSE or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT):
        #     sound('ready')
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)

    elif event.type == EventType.ON_ASSISTANT_ERROR:
        sound('error')

def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
