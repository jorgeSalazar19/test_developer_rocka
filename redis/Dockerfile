FROM        ubuntu:latest
RUN         apt-get update && apt-get install -y redis-server
RUN         apt-get update && apt-get install -y gettext libgettextpo-dev
RUN apt-get update && apt-get install -y gettext && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE      6379
ENTRYPOINT [ "redis-server", "--protected-mode", "no" ]
