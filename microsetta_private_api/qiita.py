from microsetta_private_api.config_manager import SERVER_CONFIG
from qiita_client import QiitaClient, NotFoundError


if not SERVER_CONFIG['qiita_endpoint']:
    class _mock:
        def get(self, *args, **kwargs):
            raise NotFoundError("No qiita client")

        def post(self, *args, **kwargs):
            raise NotFoundError("No qiita client")

        def http_patch(self, *args, **kwargs):
            raise NotFoundError("No qiita client")

    qclient = _mock()
else:
    qclient = QiitaClient(
        SERVER_CONFIG["qiita_endpoint"],
        SERVER_CONFIG["qiita_client_id"],
        SERVER_CONFIG["qiita_client_secret"]
    )
