## Music App


## Задание:

Kаталог исполнителей и их альбомов с помощью Django и DRF с песнями такой структуры:
— Исполнитель
   Название
 
— Альбом
   Исполнитель
   Год выпуска

— Песня
    Название
    Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.
В качестве площадки для демонстрации АПИ используется Swagger. `http://localhost:8080/swagger/`

## Run project with docker:
    docker-compose -p music_app --file docker/docker-compose.yml up -d --build

## URL: [post:] `http://localhost:8080/albums/api/`

## Go to docker container:
docker exec -it music_app_web_1 bash

