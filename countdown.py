#!/usr/bin/env python
# countdown.py - A simple countdown script.

import time, subprocess, sys

if len(sys.argv) < 2:
    print("Usage: countdown.py seconds")
    sys.exit()

timeLeft = int(sys.argv[1])
while timeLeft > 0:
    print(timeLeft, end=", ")
    sys.stdout.flush()
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
# subprocess.Popen(['open', 'alert.wav'])

import subprocess

audio_file = "alert.wav"
for i in range(3):
    return_code = subprocess.call(["afplay", audio_file])
