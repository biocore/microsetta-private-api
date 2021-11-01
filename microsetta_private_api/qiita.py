from microsetta_private_api.config_manager import SERVER_CONFIG
from qiita_client import QiitaClient


qclient = QiitaClient(
    SERVER_CONFIG["qiita_endpoint"],
    SERVER_CONFIG["qiita_client_id"],
    SERVER_CONFIG["qiita_client_secret"]
)
