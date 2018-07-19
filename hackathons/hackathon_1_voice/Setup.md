# Software Setup 

This Readme contains the software setup (SSD setup) that we followed to get the Google AIY Voice Kit v1 to work, and to use it without keyboard and mouse. 

## 1. SSD Disk Image setup

For this step, you'll need a micro SSD card and a cardreader. Make sure the SSD has 16GB or more. It will be formatted so make sure there's nothing valuable on there. 

The kit we're working with is v1, and there is a new kit out, v2. That means some of the links in the booklet are now changed to the v2 version. 

The disk image you need is not in the location specified. 
Find the documentation here instead: [https://aiyprojects.withgoogle.com/voice-v1/](https://aiyprojects.withgoogle.com/voice-v1/). The disk image is [here](https://dl.google.com/dl/aiyprojects/aiyprojects-latest.img.xz).

Download the disk image. 

Use [Etcher](https://etcher.io/) to burn the disk image to an SSD. 

Don't insert the SSD in the Raspberry just yet :) we need to do some minor adjustments. 

## 2. Ssh setup for Raspberry Pi

We're going to use the Raspberry without keyboard, mouse, and monitor. That is not how the Google booklet sets it up, so we'll need to modify the setup. 

(Taken from: [https://desertbot.io/blog/ssh-into-pi-zero-over-usb](https://desertbot.io/blog/ssh-into-pi-zero-over-usb))

### ssh
Insert the SD card into the computer with card reader. Open Terminal. At the command line do the following:

`ls -ls /Volumes/`

You should see something like this:

```
total 13
8 lrwxr-xr-x  1 root   admin     1 Jul 28 09:41 Macintosh HD -> /
5 drwxrwxrwx@ 1 mitch  staff  2560 Jul 28 11:47 boot
```

The volume named `boot` should be the SD card with the Raspbian image on it.

Now do this:

`ls -ls /Volumes/boot`

You should now see the contents of the root of your Raspbian boot image.

There was a security update to the Raspbian images. Now to enable ssh by default you have to do the following:

`touch /Volumes/boot/ssh`

This will write an empty file to the root of your Raspbian image. That will enable ssh on startup.

Next, we hack config.txt: 

1. In the root folder of the SD card, open config.txt: `nano /Volumes/boot/config.txt`
2. Append this line to the bottom of it: `dtoverlay=dwc2`
3. Save the file. 

Now, we hack cmdline.txt:

1. In the root folder of the SD card, open cmdline.txt: `nano /Volumes/boot/cmdline.txt`
2. After rootwait, append this text leaving only one space between rootwait and the new text (otherwise it might not be parsed correctly):`modules-load=dwc2,g_ether`
(If there was any text after the new text make sure that there is only one space between the new text and that text)
3. Save the file

Now, ssh is all setup. There is, however, no wifi connection setup. So we'll need to do that next. 

### WiFi
(ref: [https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html](https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html),[https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/](https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/))

To get the Raspberry Zero to work headless with wifi, you need to setup wifi for it. This can be done on the SD card. 

Create a new text file:
 
`nano /Volumes/boot/wpa_supplicant.conf`

Enter the following in the file: 

```
country=nl
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="MyNetworkSSID"
 psk="Pa55w0rd1234"
}
```

The Country Code should be set the [ISO/IEC alpha2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for the country in which you are using your Pi. Common codes include :

- US (USA)
- NL (Netherlands)
- GB (United Kingdom)
- FR (France)
- DE (Germany)
- US (United States)
- SE (Sweden)


### Boot up the Raspberry Pi

Eject the SD, and insert it in the Raspberry Pi Zero. Turn on the power, and it should boot up. Allow up to 90 seconds to boot up. 

*Important* Once the Raspberry is powered on, don't just remove power. It needs to be properly shutdown. Use terminal command `shutdown -f now`. Otherwise you risk damaging the SSD install and you'll be at square one. 

### Ssh into your Raspberry over Wifi

First, find out the IP address for your Raspberry Pi Zero. This can be done in several ways. If you can't access a device list from your local router, another way to do it is this: 

Install arp-scan via [Homebrew](https://brew.sh/). (Just running `arp -a` won't tell you what device goes with each IP address) : 

```
brew install arp-scan
sudo arp-scan --localnet -v

```

You'll end up with something like this: 

```
Interface: en0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9.5 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.178.1	90:XX:XX:XX:XX:XX	XXXXXXXX.
...
192.168.178.74	XX:XX:XX:XX:XX:XX	XXXXX
192.168.178.122	XX:XX:XX:XX:XX:XX	Apple, Inc.
192.168.178.123	XX:XX:XX:XX:XX:XX	Raspberry Pi Foundation
...
518 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9.5: 256 hosts scanned in 1.866 seconds (137.19 hosts/sec). 15 responded
```

Then, ssh as follows: 
`ssh pi@<raspberry ip address>`

The default password is raspberry. To change it, use passwd from the ssh command line.

### Security

*Tip:* Now that your Raspberry has ssh enabled, it's a good idea to change the password for the `pi` user. 

You can do that by ssh-ing to the raspberry and using the command passwd. 

## 3. Update the Raspberry

**WARNING** Don't update the firmware. Don't `sudo rpi-update`. It will mess up the setup. 

**WARNING** It may seem like a great idea to update the Raspbian OS using e.g. `sudo apt-get update` and so on, but this will destroy the Google Voice AIY setup. Don't do it. `

Now you need setup some things using the `raspi-config` program that configs your pi.

`sudo raspi-config`

Below are the options I configured for my Pi:

1. Set a new password
2. Set a hostname, e.g. GoogleVoice1

## 4. VNC setup for Raspberry Pi

The Google AIY kit has a desktop setup that in some cases makes it easier to use. To access it, we can use VNC. This means setting up VNC on the raspberry.

### Raspberry VNC setup
(Based on: [https://42bots.com/tutorials/access-raspberry-pi-terminal-and-desktop-remotely-with-ssh-and-vnc/](https://42bots.com/tutorials/access-raspberry-pi-terminal-and-desktop-remotely-with-ssh-and-vnc/))

We'll use TightVNCServer, as it is light and easy to install. 

On your raspberry ssh terminal, type: 

```
sudo apt-get install tightvncserver
tightvncserver
``` 

The VNC server will respond: 

```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "UTF-8",
	LANG = "en_GB.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_GB.UTF-8").
```

The system asks you to setup two passwords for viewing/editing and view only. (I chose `12345678` for both):

```
You will require a password to access your desktops.

Password:
Verify:
Would you like to enter a view-only password (y/n)? y
Password:
Verify:

```

The VNC server will now respond: 

```
New 'X' desktop is GoogleVoice1:1

Creating default startup script /home/pi/.vnc/xstartup
Starting applications specified in /home/pi/.vnc/xstartup
Log file is /home/pi/.vnc/GoogleVoice1:1.log
```

Take note of the VNC port number (display number) it gives back. We'll need it in the next step. In my case it is number 1. 

### Setup mac screen sharing

(Taken from: [https://til.hashrocket.com/posts/69cbe9b2c3-how-to-use-the-hidden-vnc-client-in-mac-osx](https://til.hashrocket.com/posts/69cbe9b2c3-how-to-use-the-hidden-vnc-client-in-mac-osx) and [https://smittytone.wordpress.com/2016/03/02/mac_remote_desktop_pi/](https://smittytone.wordpress.com/2016/03/02/mac_remote_desktop_pi/)).

Mac OSX has a good VNC client built in. It is hiding in the Finder. Open Finder, hit Cmd-K, and you'll see a server connect input. 

The key is that you need to connect to the correct VNC port. In my case, it was port 5901. 5900 is base vnc port, and add +1 for the default tightvnc display number. 

Enter the following: 
`vnc://<raspberry ip>:<vnc port>`

You'll be greeted by the Google AIY raspberry linux desktop. 

## 5. Getting the Audio to work 

Ok, all the setup is done! Time for some audio, right?

Let's get it to work. 

Running the audio script from the command line gives an error: 
```
Traceback (most recent call last):
  File "audio.py", line 22, in <module>
    import aiy._drivers._player
ImportError: No module named aiy._drivers._player
```

Apparently, there seems to be a version issue (but i got the latest) as described here: [https://github.com/google/aiyprojects-raspbian/issues/339](https://github.com/google/aiyprojects-raspbian/issues/339) 

They advise to run: 

```
sudo dtoverlay googlevoicehat-soundcard
```

This solved the problem, when starting from the desktop. This command can also be added in `/boot/config.txt`, so it is run every time. Add: 

```
dtoverlay=i2s-mmap
dtoverlay=googlevoicehat-soundcard
```

*Note* Running scripts from the command line using e.g.

```
python ~/AIY-projects-python/checkpoints/check_audio.py
```

does not work, but running it with 

```
exec ~/AIY-projects-python/checkpoints/check_audio.py
```

does. There seems to be a conflict in Python setup. No clue why. 


## 6. Getting Github to work 
The Raspberry initially has been setup with git, but not with the right public keys. You'll need to create a key. Follow this: [https://help.github.com/articles/connecting-to-github-with-ssh/](https://help.github.com/articles/connecting-to-github-with-ssh/).

When adding the key to github, use `scp` to copy from the raspberry to your own machine. This makes it easier in the github interface to enter the key: 

```
scp pi@<raspberry ip>:.ssh/id_rsa.pub ~/Downloads 
```
Setup the github key as described above. 


## 7. Setting up some scripts 
Since sometimes the calls can be a bit lengthy: 

create scripts: 

```
# assistant.sh - normal google assistant 
exec ~/hackademy.ai/hackathons/hackathon_1_voice/aiy-voice-v1/src/examples/voice/assistant_library_with_local_commands_demo0.py
```

```
# ahotword.sh - custom hotword with snowboy with google assistant
exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/hotword/assistant_library_hotword.py
```

```
# hotword.sh - custom hotword with snowboy 
exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/hotword/HotwordDemo.py
```

```
# zork.sh 
exec ~/hackademy.ai/hackathons/hackathon_1_voice/experiments/hotword/zork.py
```

to run these: 

```
. assistant.sh 
```

