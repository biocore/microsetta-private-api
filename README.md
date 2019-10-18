# microsetta-private-api
A private microservice to support The Microsetta Initiative

## Installation
Create a new `conda` environment containing `flask`:

`conda create -n microsetta-private-api flask`

Once the conda environment is created, activate it:

`conda activate microsetta-private-api`

Install connexion version 2.0 (which supports the OpenAPI Specification 3.0) as well as the Swagger UI:

`pip install connexion[swagger-ui]`

Then copy the project files into the directory of your choice.
 
## Test Usage

In the activated conda environment, start the microservice using flask's built-in server by running, e.g., 

`./api/server.py`

which will start the server on http://localhost:8082 . Note that this usage is suitable for 
**development ONLY**--real use of the service would require a production-level server. 

The Swagger UI should now be available at http://localhost:8082/api/ui .

Currently the `/account` `get` interface (only) requires oath2 authentication.  This can be tested from the command line
 using the following two commands to see two different (authorized) responses:

`curl -H 'Authorization: Bearer 123' http://localhost:8082/api/account`

`curl -H 'Authorization: Bearer 456' http://localhost:8082/api/account`

