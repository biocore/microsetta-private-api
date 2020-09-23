from microsetta_private_api.server import app
from microsetta_private_api.celery_utils import celery, init_celery
init_celery(celery, app.app)
