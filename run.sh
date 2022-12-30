# development mode, just run the flask app locally
# Need to change redis server to localhost in routes.py

export PASTA_ROOT="$PWD/pasta"
cd $PASTA_ROOT

export FLASK_APP=__init__.py
flask run --host=0.0.0.0

