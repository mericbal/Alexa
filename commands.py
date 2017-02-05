from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import time
import json
import requests
import logging

# API KEY

response = requests.get('https://api.lifx.com/v1/lights/all', auth=(token, ''))

headers = {
    "Authorization": "Bearer %s" % token,
}

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


def lower_by(num)
	payload = {
	  "states": [
	    {
	        "selector" : "all",
	        "hue": 200,
	        "brightness": 0.6,
	        "kelvin": 6700
	    }
	  ],
	  "defaults": {
	    "power": "on",
	    "saturation": 0,
	    "duration": 1.0
		}
	}
	












if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

# MB