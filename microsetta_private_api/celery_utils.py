from celery import Celery

from microsetta_private_api.config_manager import SERVER_CONFIG


# derived from
# https://medium.com/@frassetto.stefano/flask-celery-howto-d106958a15fe


def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


def make_celery(app_name):
    celery_backend = SERVER_CONFIG['celery_backend_uri']
    celery_broker = SERVER_CONFIG['celery_broker_uri']
    return Celery(app_name, backend=celery_backend, broker=celery_broker)


celery = make_celery(__name__.split('.')[0])
