from microsetta_private_api.server import app
from microsetta_private_api.celery_utils import celery, init_celery
from microsetta_private_api.util.vioscreen import refresh_headers
from microsetta_private_api.admin.daklapack_polling import poll_dak_orders
init_celery(celery, app.app)

# Run any celery tasks that require initialization on worker start
refresh_headers.delay()  # Initialize the vioscreen task with a token
poll_dak_orders.delay()  # check for orders
