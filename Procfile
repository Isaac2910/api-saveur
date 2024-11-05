
//web: gunicorn saveur.wsgi --log-file - --bind 0.0.0.0:$PORT
web: gunicorn saveur.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT

