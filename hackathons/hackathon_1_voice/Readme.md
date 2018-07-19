# Google AIY Voice kit (v1) setup

Assumptions:

- We're using Mac.
- We're using Google Voice Kit v1.

## Repo
The repo contains a modified version of the Google AIY Voice v1 repo. It also contains several other codebases. In this readme I have attempted to make sure all the links are clear. If there are omissions let me know, as it is not our intention to obscure who created the repo's we used - they are simply included here so we have one comprehensive version that is easy to work with. 

## Google AIY Voice Kit Demos

### Setting up Google Accounts (Steps 11, 12 from the booklet)

(Google account TMI, project name Hackathon-ai-Voice)

The booklet has you do all of this on the raspberry and you can certainly do that through terminal services, but it may be easier to do it on your computer instead. This will leave you with a downloaded client secrets file on your mac, while it should be on the raspberry. Luckily, there is the magic of `scp` to copy between systems which are connected over ssh.

To copy the client secrets file to raspberry over ssh from a local folder, in this example your Downloads folder:

`scp ~/Downloads <filename> pi@<raspberry ip>:Downloads`

This will copy it from `~/Downloads` on your mac and have it end up in the `~/Downloads` folder on the pi.

The library demo file is in a different place than in the booklet: `~/AIY-voice-kit-python/src/examples/voice`.

### Google Assistant Demo
Once this is done, start the assistant demo:
`exec ~/AIY-voice-kit-python/src/examples/voice/assistant_library_demo.py`

It has you first get some credentials from the internet through a URL and once these are filled correctly, you are able to issue voice commands.

Try this:

```
OK Google,
what's the weather forecast in Amsterdam tonight,
in Celcius?
```
And it will tell you.

It will also often fail:
```
OK Google,
what is a waterslide?
...

OK Google,
what is deep learning?
...
```

### Hack 1: Local Commands

To run:
`exec ~/AIY-voice-kit-python/src/examples/voice/assistant_library_with_local_commands_demo.py`

#### Adding your own sounds
**Note** the 'computer' example doesn't work in this way, needs to be started from the local folder for the file paths to wav files to work...

We'll use some Star Trek sounds from [here](http://www.trekcore.com/audio/) and [here](http://www.stdimension.org/MediaLib/effects/computer/federation/)

#### Custom hotword
The hotword for the assistant can be changed in v2 :
[repo](https://bitbucket.org/dani_thomas/aiyhotworddetector/src)

References:

* [https://console.cloud.google.com/home/dashboard?project=api-project-687914046043](https://console.cloud.google.com/home/dashboard?project=api-project-687914046043)
* [Hotword hack?](https://www.raspberrypi.org/forums/viewtopic.php?t=183932#p1164380)
* [https://www.hackster.io/shiva-siddharth/custom-wake-word-for-google-assistant-on-raspberry-pi-124fda](https://www.hackster.io/shiva-siddharth/custom-wake-word-for-google-assistant-on-raspberry-pi-124fda): Snowboy
* With hotword github repo: [https://github.com/warchildmd/google-assistant-hotword-raspi](https://github.com/warchildmd/google-assistant-hotword-raspi)

We're using [Snowboy](http://docs.kitt.ai/snowboy/#downloads) to do hotword detection. Snowboy runs hotword as a service.

`exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/hotword/HotwordDemo.py`
`exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/hotword/assistant_library_hotword.py`

#### Linking to Slack
Install python code to use slack.

##### Setting up slack
Setup a slack webhook here: [https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)

##### Changing the python code in the example

We're using this reference: [https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784](https://gist.github.com/devStepsize/b1b795309a217d24566dcc0ad136f784)

You'll see the script ([on Github](https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/src/examples/voice/assistant_library_with_local_commands_demo.py)).

It basically tries to find several keywords, and when it finds one, it performs a certain action. We'll add a new action.

Find the example code under
`~/hackademy.ai/hackathons/hackathon_1_voice/experiments/slack`

It's already integrated in
`~/hackademy.ai/hackathons/hackathon_1_voice/aiy-voice-v1/src/examples/voice/assistant_library_with_local_commands_demo.py`

#### Linking to IFTTT
This basically works in the same way. The code is in the repo.


Find the example code under
`~/hackademy.ai/hackathons/hackathon_1_voice/experiments/ifttt`

It's already integrated in
`~/hackademy.ai/hackathons/hackathon_1_voice/aiy-voice-v1/src/examples/voice/assistant_library_with_local_commands_demo.py`


### Google Cloud Speech API
The cloud API can be setup using the booklet.
This script works fine. Quite easy to change also

#### Hack 3: Add a new Activation Trigger
There is an example with the button, but it can also be done in other ways.

#### Optional: Adding a camera trigger
You might do this through Google Vision Kit

#### Hack 4: Edit Cloudspeech_demo.py
This is included in the booklet.

### Google Actions and Dialog Flow
[https://dialogflow.com/docs/integrations/google-assistant](https://dialogflow.com/docs/integrations/google-assistant)

### Tensorflow
#### Hack 5: Tensorflow and on-device audio detection
We did not prepare a demo for this, but below are some interesting resources

See [aiyprojects.withgoogle.com/voice](aiyprojects.withgoogle.com/voice)

[Tensorflow Speech Recognition Training](https://www.tensorflow.org/versions/master/tutorials/audio_recognition)

Custom Voice interface stuff:
[https://aiyprojects.withgoogle.com/voice/#makers-guide--custom-voice-user-interface](https://aiyprojects.withgoogle.com/voice/#makers-guide--custom-voice-user-interface)

Recognize if specific voice is speaking: e.g. voice unlock?
[Recognize Voices - not speech](https://dzone.com/articles/voice-recognition-not-speech-recognition-is-here)

Tensorflow NLP using RNN:
[https://www.tensorflow.org/tutorials/sequences/recurrent](https://www.tensorflow.org/tutorials/sequences/recurrent)

Simple Audio classification using Tensorflow: e.g. count number of claps? recognize if there is conversation or no conversation?
[https://dzone.com/articles/sound-classification-with-tensorflow](https://dzone.com/articles/sound-classification-with-tensorflow)

[Audio tutorial](https://www.tensorflow.org/tutorials/sequences/audio_recognition)

[Recognize sounds](https://www.iotforall.com/tensorflow-sound-classification-machine-learning-applications/)

* Get audio data of voice vs other voices
* Resample to 16 kHz
* Fourier transform and MEL transform

[Audio data](https://research.google.com/audioset/index.html)
[Audioset models](https://github.com/tensorflow/models/tree/master/research/audioset)

You need to get features that are the same in dimensions, the fourier helps with this. VGG-like model looks like this:

```
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

# Generate dummy data
x_train = np.random.random((100, 100, 100, 3))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
x_test = np.random.random((20, 100, 100, 3))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(x_train, y_train, batch_size=32, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=32)
```
This one is built for images but it is possible to change that for fourier.

#### Tensorboard
Install tensorboard to make visualizing tensorflow training easy.

### Make assistant startup at boot
See [https://medium.com/@swapratimroy/google-aiy-voice-kit-hacking-part-2-23aa122eedd2](https://medium.com/@swapratimroy/google-aiy-voice-kit-hacking-part-2-23aa122eedd2)

### Hack 6: Adventure Game
- [Repo](https://github.com/devshane/zork) Ok so in 1980 they coded slightly differently.
- [Better Repo](https://pypi.org/project/adventure/) It's not Zork, it's Colossal Cave / Adventure, but it works.

I got this to work based on the cloudspeech api.

Run from the ~ folder using
`exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/adventure/game.py`

## Happy Hacking!
Any ideas or additions are welcome!
