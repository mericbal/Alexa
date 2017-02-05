# Alexabot is Alexabot: Amazon Alexa Controlled Robot With the Raspberry Pi
#
# This file is the flask server that listens for commands from Alexa.
# You can see the full project here: https://www.dexterindustries.com/projects/alexabot-amazon-alexa-controlled-robot/
# In this tutorial we build Alexabot, the Amazon Alexa Controlled Robot, using the Raspberry Pi.
# We will walk through the steps of building a voice controlled robot with the Raspberry Pi and GoPiGo.
# With Alexabot, you can command the Raspberry Pi Robot around with commands like "Alexa Forward!" or "Alexa Coffee!".
#
# See more about Dexter Industries at http://www.dexterindustries.com
# See more about the GoPiGo at http://www.dexterindustries.com/gopigo

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import time
import json
import requests
import logging


response = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

print(response.content)
print "******************"

headers = {
    "Authorization": "Bearer %s" % token,
}

response_2 = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

print(response_2.content)
print "$$$$$$$$$$$$$$$$$"

payload = {
  "states": [
    {
        "selector" : "all",
        "hue": 200,
        "brightness": 0.6,
        "kelvin": 3000
    }
  ],
  "defaults": {
    "power": "on",
    "saturation": 0,
    "duration": 1.0

	}
}

response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)
print(response.content)

def power_off():
	payload = {
	"states": [
	{
	"selector" : "all",
	"power": "off"
	}
	],
	"defaults": {
	"power": "on",
	"saturation": 0,
	"duration": 2.0
	}
	}
	response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)
	print(response.content)

power_off()

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/hello')
def hello():
	print("Hello!")
	return 'Hello!'



log = logging.getLogger()

ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


# @app.route('/backward')
# def backward():
# 	print("Backward!")
# 	gopigo.bwd()	# Send the GoPiGo Backward
# 	time.sleep(1)	# for 1 second
# 	gopigo.stop()	# and then stop the GoPiGo.
# 	return 'Backward!'

# @app.route('/left')
# def left():
# 	print("Left!")
# 	gopigo.left()
# 	time.sleep(1)
# 	gopigo.stop()
# 	return 'Left!'

# @app.route('/right')
# def right():
# 	print("Right!")
# 	gopigo.right()
# 	time.sleep(1)
# 	gopigo.stop()
# 	return 'Right!'

# @app.route('/dance')
# def dance():
# 	print("Dance!")
# 	for each in range(0,5):
# 		gopigo.right()
# 		time.sleep(0.25)
# 		gopigo.left()
# 		time.sleep(0.25)
# 		gopigo.bwd()
# 		time.sleep(0.25)
# 	gopigo.stop()
# 	return 'Dance!'

# @app.route('/coffee')
# def coffee():
# 	print("Coffee!")
# 	return 'coffee!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')




	## MB



