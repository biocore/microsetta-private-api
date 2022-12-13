from importlib import resources as pkg_resources

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key.
AUTHROCKET_PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    "authrocket.pubkey")
CRONJOB_PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    'cronjob.pubkey')
JWT_ISS_CLAIM_KEY = 'iss'
JWT_SUB_CLAIM_KEY = 'sub'
JWT_EMAIL_CLAIM_KEY = 'email'
ACCT_NOT_FOUND_MSG = "Account not found"
SRC_NOT_FOUND_MSG = "Source not found"
SRC_NO_DELETE_MSG = "A source cannot be deleted while samples are "\
    "associated with it"
INVALID_TOKEN_MSG = "Invalid token"
