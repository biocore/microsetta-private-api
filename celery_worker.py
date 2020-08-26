from microsetta_private_api.server import build_app
from microsetta_private_api.celery_utils import celery  # noqa
app = build_app()
