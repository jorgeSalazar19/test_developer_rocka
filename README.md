# test_developer_rocka
This project is a test developer for apply to developer software in Rocka

## Instruction to run project

The project contain one file of docker-compose, this file can use to run project:

- add one file named .env with the following variables:
    DJANGO_SETTINGS_MODULE=config.settings.dev

    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_PORT=5432
    POSTGRES_HOST=db
    PGDATA=/var/lib/postgresql/data/pgdata

    REDIS_SERVER=redis
    REDIS_PORT=6379

- run the following command - docker-compose up --build



