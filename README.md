# test_developer_rocka
This project is a test developer for apply to developer software in Rocka

## Instruction to run project

The project contain one file of docker-compose, this file can use to run project:

- add one file named .env with the following variables:
    DJANGO_SETTINGS_MODULE=config.settings.dev

    - POSTGRES_DB=postgres
    - POSTGRES_USER=postgres
    - POSTGRES_PASSWORD=postgres
    - POSTGRES_PORT=5432
    - POSTGRES_HOST=db
    - PGDATA=/var/lib/postgresql/data/pgdata

    - REDIS_SERVER=redis
    - REDIS_PORT=6379

- run the following command - docker-compose up --build


## Endpoint to execute logic

- url_project/api/order/movies/

    - Method GET
    - parameter: ordering_method, this parameter has 3 different values (average, same_movie, actors), each para is used for different sort

- url_project/api/upload/movies/

    - Method POST
    - Parameter : movies (list of json objects)
    - This endpoint upload the data of movies in the models project, before thi action you can execute the endpoint order for show data sort

## Execute Migrations

- run the following command: docker-compose run --rm web  python manage.py migrate --settings=config.settings.dev

- run the following command: docker-compose run --rm web  python manage.py makemigrations domain --settings=config.settings.dev

- run the following command: docker-compose run --rm web  python manage.py migrate domain --settings=config.settings.dev


## Execute Tests

- run the following command: docker-compose run --rm web  python manage.py test web --settings=config.settings.dev

- the test folder is into path (web/api/tests)

