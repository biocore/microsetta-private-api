![microsetta-private-api CI](https://github.com/biocore/microsetta-private-api/workflows/microsetta-private-api%20CI/badge.svg)

# microsetta-private-api
A private microservice to support The Microsetta Initiative

## Installation
The private microservice depends on Postgres 9 or higher. For OSX users, we recommend installing [Postgres.app](https://postgresapp.com/) and  ensuring that path has been configured to allow use of the command line tools delivered with the app. For Linux users, please consult documentation for the Linux distribution in use. 

Create a new `conda` environment containing `flask` and other necessary packages: 

`conda create --yes -n microsetta-private-api python=3.7`

Once the conda environment is created, activate it:

`conda activate microsetta-private-api`

Ensure that the `conda-forge` channel has been added to the conda install and run:

`conda install --yes --file ci/conda_requirements.txt`

Install additional requirements using pip:

`pip install -r ci/pip_requirements.txt`

Then install the microsetta-private-api in editable mode:

`pip install -e . --no-deps`
 
## Test Usage

In the activated conda environment, initialize a test database:

`python microsetta_private_api/LEGACY/build_db.py`

To run unittests:

`make test`

Then we'll initiate a Celery worker (Example shown is with embedded Celery Beat scheduler):

`celery -A microsetta_private_api.celery_worker.celery worker -B --loglevel=info`

*** OR (Allowing for multiple workers)***

`celery -A microsetta_private_api.celery_worker.celery worker --loglevel=info` (Start 1 worker)
`celery -A microsetta_private_api.celery_worker.celery beat --loglevel=info` (Start the Celery Beat scheduler)


Next, start the microservice using flask's built-in server by running, e.g., 

`python ./microsetta_private_api/server.py`

which will start the server on http://localhost:8082 . Note that this usage is suitable for 
**development ONLY**--real use of the service would require a production-level server. 

The Swagger UI should also be available at http://localhost:8082/api/ui .
