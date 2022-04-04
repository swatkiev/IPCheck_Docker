# IPCheck_Docker Проверка IP в Телеграмм боте

Создайте чат бота в телеграмме с помощью @BotFather с уникальным именем и идентификатором, который вставьте в переменную BOT_TOKEN в файле run.py

Установите на хосте Docker по официальной документации, выбрав необходимый дистрибутив: https://docs.docker.com/engine/install/

Выполните последовательно команды, находясь в директории с Dockerfile: "docker build -t ipbot ." и "docker run --name ipbot --restart="always" -d ipbot"
