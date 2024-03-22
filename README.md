"# expertMetatrader" 

Run project :

    pip install -r requirements.txt

    "and create .env file"

    python3 manage.py migrate

    python3 manage.py runsevrer

Run celery :

    celery -A celeryMetaTrader worker -l info -P gevent

    celery -A celeryMetaTrader beat -l INFO