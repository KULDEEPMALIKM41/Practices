# from celery import Celery
# import time
# app = Celery("tasks", broker="amqp://localhost//" ,backend='mongodb://localhost:27017/request_db')
#
# @app.task
# def reverse(string):
#     time.sleep(10)
#     return string[::-1]


from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery