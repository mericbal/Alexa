# celery worker -A tasks -l INFO
# rabbitmq-server

from celery import Celery

app = Celery()

@app.task
def hello(string):
	return string

@app.task
def add(x,y):
	return x + y

@app.task
def counter(x):
	while x >= 1:
		print	"Number is -> %d " % x
		x-=1

# @app.task
# def loop():
# 	x=1
# 	while True:
# 		print	"Infinity number %d " % x
# 		x += 1