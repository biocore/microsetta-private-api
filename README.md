[![Coverage Status](https://coveralls.io/repos/github/biocore/microsetta-private-api/badge.svg?branch=master)](https://coveralls.io/github/biocore/microsetta-private-api?branch=master)

# microsetta-private-api
A private microservice to support The Microsetta Initiative

## Installation
Create a new `conda` environment containing `flask` and other necessary packages:

`conda create -n microsetta-private-api flask psycopg2 natsort pycryptodome`

Once the conda environment is created, activate it:

`conda activate microsetta-private-api`

Install connexion version 2.0 (which supports the OpenAPI Specification 3.0) as well as the Swagger UI:

`pip install connexion[swagger-ui]`

Install the JSON Web Tokens library with cryptography support:

`pip install pyjwt[crypto]`

Install redis:

`sudo pip install redis`

Then install the microsetta-private-api in editable mode:

`pip install -e .`
 
## Test Usage

In the activated conda environment, start the microservice using flask's built-in server by running, e.g., 

`python ./microsetta_private_api/server.py`

which will start the server on http://localhost:8082 . Note that this usage is suitable for 
**development ONLY**--real use of the service would require a production-level server. 

The Swagger UI should now be available at http://localhost:8082/api/ui .

Currently the `/account` `get` interface (only) requires oath2 authentication, but this is currently mocked to return
the same token info no matter what bearer token value is passed in.  This dummy-authenticated method can be tested from 
the command line using the following command to examine an account record added by `repo_test_scratch.py`

`curl -H 'Authorization: Bearer dummy' http://localhost:8082/api/accounts/aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff`


