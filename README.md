# minimal-flask-docker
Example flask web app, with a redis data store. Add mysql or postgres if desired.

```docker-compose up -d && docker-compose logs -f```

Mounts the project directory as a volume so we can hotpatch it.

View the website at ```[hostname]:3141``` (e.g ```0.0.0.0:3141``` if run locally).


