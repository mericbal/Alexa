from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def presentation():
	return statement('Made it')

if __name__ == '__main__':
  app.run(debug=True)

# MB