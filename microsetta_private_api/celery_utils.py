from celery import Celery

from microsetta_private_api.config_manager import SERVER_CONFIG

PACKAGE = __name__.split('.')[0]
CELERY_BACKEND_URI = 'celery_backend_uri'
CELERY_BROKER_URI = 'celery_broker_uri'


# derived from
# https://medium.com/@frassetto.stefano/flask-celery-howto-d106958a15fe
def init_celery(celery, app):
    celery.conf.update(app.config)
    celery.conf.task_default_queue = 'microsetta-private-api'
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    celery.autodiscover_tasks([PACKAGE])

    # Set up "Celery Beat", events that run on a fixed time interval
    celery.conf.beat_schedule = {
        # Vioscreen tokens are good for an hour, refresh every 55 minutes
        "refresh_vioscreen_token": {
            "task": "microsetta_private_api.util.vioscreen.refresh_headers",
            "schedule": 55 * 60
        },
        "update_vioscreen_sessions": {
            "task": "microsetta_private_api.util.vioscreen.update_session_detail",  # noqa
            "schedule": 60 * 60 * 24  # every 24 hours
        },
        "poll_daklapack_orders": {
            "task": "microsetta_private_api.admin.daklapack_polling.poll_dak_orders",  # noqa
            "schedule":  60 * 60 * 24  # every 24 hours
        },
        "update_qiita_metadata": {
            "task": "microsetta_private_api.tasks.update_qiita_metadata",  # noqa
            "schedule":  60 * 60 * 24  # every 24 hours
        },
        # "fetch_ffqs": {
        #     "task": "microsetta_private_api.util.vioscreen.fetch_ffqs",
        #     "schedule":  60 * 60 * 24  # every 24 hours
        # },
        # "geocode_accounts": {
        #     "task": "microsetta_private_api.tasks.geocode_accounts",
        #     "schedule": 60
        # }
    }


def make_celery(app_name):
    celery_backend = SERVER_CONFIG[CELERY_BACKEND_URI]
    celery_broker = SERVER_CONFIG[CELERY_BROKER_URI]
    return Celery(app_name, backend=celery_backend, broker=celery_broker)


celery = make_celery(PACKAGE)
