from importlib.resources import files

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key.
AUTHROCKET_PUB_KEY = (files('microsetta_private_api')
                      .joinpath("authrocket.pubkey")
                      .read_text())
CRONJOB_PUB_KEY = (files('microsetta_private_api')
                   .joinpath('cronjob.pubkey')
                   .read_text())
JWT_ISS_CLAIM_KEY = 'iss'
JWT_SUB_CLAIM_KEY = 'sub'
JWT_EMAIL_CLAIM_KEY = 'email'
ACCT_NOT_FOUND_MSG = "Account not found"
SRC_NOT_FOUND_MSG = "Source not found"
SRC_NO_DELETE_MSG = "A source cannot be deleted while samples are "\
    "associated with it"
INVALID_TOKEN_MSG = "Invalid token"
CONSENT_DOC_NOT_FOUND_MSG = "Consent not found"
