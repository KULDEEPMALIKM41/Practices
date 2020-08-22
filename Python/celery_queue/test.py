from tasks import make_celery
from flask import Flask
import time
apps=Flask(__name__)

apps.config['CELERY_BROKER_URL']="amqp://localhost//"
apps.config['CELERY_RESULT_BACKEND']="mongodb://localhost:27017/request_db"

celery = make_celery(apps)

@apps.route("/reverse/<t>")
def reverse(t):
    result=reverse.delay(t)
    return result.get()

@apps.route("/add")
def add():
    result=add.delay(3,6)
    c = result.get()
    c=str(c)
    return c

@celery.task(name="reverse")
def reverse(string):
    time.sleep(5)
    return string[::-1]

@celery.task(name="add")
def add(a,b):
    time.sleep(5)
    c= a+b
    return c
if __name__ == "__main__":
    apps.run(port=1234)


# from tasks import *
# from flask import Flask
# apps=Flask(__name__)
#
# @apps.route("/reverse/<t>")
# def Task(t):
#     print(reverse.delay(t))
#     return reverse(t)
# apps.run(port=9639)