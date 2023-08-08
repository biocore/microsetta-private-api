# from microsetta_private_api.server import app
from microsetta_private_api.celery_utils import celery, init_celery
from microsetta_private_api.util.vioscreen import refresh_headers
from microsetta_private_api.admin.daklapack_polling import poll_dak_orders
from microsetta_private_api.util.fundrazr import get_fundrazr_transactions
from microsetta_private_api.util.perk_fulfillment import check_shipping_updates
# from microsetta_private_api.tasks import update_qiita_metadata
init_celery(celery)

# Run any celery tasks that require initialization on worker start
refresh_headers.delay()  # Initialize the vioscreen task with a token
poll_dak_orders.delay()  # check for orders
get_fundrazr_transactions.delay()  # check for new transactions
check_shipping_updates.delay()  # check for tracking updates
# update_qiita_metadata.delay()  # run Qiita metadata push

# Disabling Qiita metadata push until we have survey changes in place and
# are ready to test. - Cassidy 2022-12-01
