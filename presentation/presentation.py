import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def intro():
	return question('Hi everybody, are you redy for presentation ?')

@ask.intent("YesIntent")
def presentation():
	return render_template("presentation")

@ask.intent("NoIntent")
def no_answer():
	return statement('Okay , i will start when you are ready.')



###

if __name__ == '__main__':
  app.run(debug=True)

# MB