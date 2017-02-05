import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

###########

@ask.launch

def welcome() :
	welcoming = 'Hello Merich, do you wanna start?'
	return question(welcoming)

@ask.intent('YesIntent')

def leagues() :
	leagues = ['English Premier League', 'La Liga', 'Turkish Super League', 'Bundes Liga']
	alexa = "Your favourite league is {}".format(leagues[0])
	return statement(alexa)

#####

if __name__ == '__main__':
  app.run(debug=True)

## Intents

# { "intents": [{ "intent": "YesIntent" }] }

# MB