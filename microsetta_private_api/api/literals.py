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
INVALID_TOKEN_MSG = "Invalid token"
DUPLICATE_SOURCE_AND_EMAIL = "It looks like you're creating a new source " \
                             "that may be similar or the same as an " \
                             "existing source. If this is the same " \
                             "person as an existing source, please " \
                             "consider " \
                             "providing new samples or survey responses" \
                             " under that source. "
