#!/bin/bash
docker build . -t localhost:32000/django-falcon:1.0.0.dev0
docker run -p 8000:8000 --env-file=.env localhost:32000/django-falcon:1.0.0.dev0
