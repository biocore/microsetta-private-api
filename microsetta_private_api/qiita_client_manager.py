from qiita_client import QiitaClient
from microsetta_private_api.config_manager import SERVER_CONFIG

# This creates a global QiitaClient instance
# which we use to access the qiita api
qclient = QiitaClient(
    SERVER_CONFIG["qiita_endpoint"],
    SERVER_CONFIG["qiita_client_id"],
    SERVER_CONFIG["qiita_client_secret"]
)

# If qiita clients ever add a close/shutdown/dispose
# we can add an atexit annotated function here for cleanup.
