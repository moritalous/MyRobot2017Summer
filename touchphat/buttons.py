#!/usr/bin/env python

import signal
import time

import touchphat

import json
import boto3

import threading

print("""

Touch pHAT: Buttons Demo

Lights up each LED in turn, then detects your button presses.

Press a button to see the corresponding LED light up, and the name printed.

Press Ctrl+C to exit!

""")

class UpdateShadowThread(threading.Thread):
    def __init__(self, type):
        super(UpdateShadowThread, self).__init__()
        self.type = type

    def run(self):
        data = {"state": {"desired": {"face": {"type": self.type}}}}
        mypayload = json.dumps(data)
        response = client.update_thing_shadow(
            thingName = 'testThing1', 
            payload = mypayload
        )

for pad in ['Back','A','B','C','D','Enter']:
    touchphat.set_led(pad, True)
    time.sleep(0.1)
    touchphat.set_led(pad, False)
    time.sleep(0.1)
    touchphat.set_led(pad, True)

client = boto3.client('iot-data', region_name='ap-northeast-1')

@touchphat.on_touch(['Back','D','Enter'])
def handle_touch(event):
    print(event.name)

@touchphat.on_touch(['A'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceA').start()

@touchphat.on_touch(['B'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceB').start()
    
@touchphat.on_touch(['C'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceC').start()

@touchphat.on_touch(['D'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceD').start()

@touchphat.on_touch(['Back'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceBack').start()

@touchphat.on_touch(['Enter'])
def handle_touch(event):
    print(event.name)
    UpdateShadowThread('faceEnter').start()
    
signal.pause()
