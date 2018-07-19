#!/usr/bin/env python3
# Copyright 2017 Cyber-Renegade.
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

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import random
import re

import sys

import adventure.game as Game
import adventure.load as Loader

def main():
    recognizer = aiy.cloudspeech.get_recognizer()

    # Todo get the recognizer prepped for the game commands
    # recognizer.expect_phrase('turn off the light')

    # Start game
    #
    game = Game.Game()
    Loader.load_advent_dat(game)
    game.start()
    aiy.audio.say(game.output)

    # button to get it triggered
    #
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
      reply=""
      print('Press the button and speak')
      button.wait_for_press()
      led.set_state(aiy.voicehat.LED.ON)
      print('Listening...')
      text = recognizer.recognize()
      print(text)

      if not text:
          print('Sorry, I did not hear you.')
      else:
          print('You said "', text, '"')

          words = re.findall(r'\w+', text)
          if words:
              reply = game.do_command(words)

      if len(reply) > 0:
        #aiy.audio.say(reply)
        print("Answer:", reply)
        led.set_state(aiy.voicehat.LED.OFF)

    aiy.voicehat.get_status_ui().status('stopping')
    aiy.voicehat.get_status_ui().status('power-off')

if __name__ == '__main__':
    main()
    # To run the demo say the hotword and then ask about a holiday
