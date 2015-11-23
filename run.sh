#!/bin/bash

set -e
exec /usr/local/bin/uwsgi --processes 4 --threads 2 \
       --stats 0.0.0.0:9002 --http-socket 0.0.0.0:9000 \
       --chdir $APP_DIR --wsgi-file="$APP_DIR/app.py" \
       --callable app \
       $ADDITIONAL_ARGUMENTS $ADDITIONAL_USER_ARGUMENTS
