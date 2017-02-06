from celery import Celery

app = Celery()

@app.task
def hello():
	return 'LET THERE BE LIGHT'

@app.task
def add(x,y):
	return x + y