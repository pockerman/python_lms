sudo uwsgi --plugins http,python3 --http 127.0.0.1:80 --module ustdy.wsgi.application --env=DJANGO_SETTINGS_MODULE=ustdy.settings --uid david
