# Pyspark from Ubuntu

 ![Docker pulls build](https://img.shields.io/docker/pulls/lod2007/pyspark)
 ![Docker Automated build](https://img.shields.io/docker/automated/lod2007/pyspark)
 ![Docker Image Version (latest by date)](https://img.shields.io/docker/v/lod2007/pyspark)

В данном проекте решена задача по развертыванию на Докере образ Ubuntu с установленным Pyspark  2.4.7.
В результате вы получите готовую среду для запуска скриптов Python для Spark.

Ссылка на репозиторий:

[https://github.com/lod2007/pyspark]

Ссылка на Docker conteiner:

[https://hub.docker.com/r/lod2007/pyspark]

Версии программ:
![WordPress Plugin Version](https://img.shields.io/badge/python-3.7-green)
![WordPress Plugin Version](https://img.shields.io/badge/spark-2.4.7-orange)
![WordPress Plugin Version](https://img.shields.io/badge/hadoop-2.7-blue)
![WordPress Plugin Version](https://img.shields.io/badge/jdk-1.8.0_292-red)

## Установка Docker Engine и Docker Compose на Linux Mint

Для установки на Linux Mint можно воспользоваться инструкцией.
Предварительно вы должны скачать и установить у себя Docker Engine и Docker Compose.

    sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common

Импортитруем PGP-ключи

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Добавляем нужный репозиторий

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(. /etc/os-release; echo "$UBUNTU_CODENAME") stable"

Обновляем списки репозиториев:

    sudo apt-get update

Устанавливаем Docker

    sudo apt-get -y  install docker-ce docker-compose

После установки добавляем нашего текущего пользователя в группу docker
    
    sudo usermod -aG docker $USER

Проверяем, что Docker установился. Для этого запустим **Hello-world**:

    docker run hello-world

## Приступая к работе (Getting started)

Для получения копии этого проекта необходимо клонировать проект к себе на машину командой:

    $git clone https://github.com/lod2007/pyspark.git your_project

В проекте уже созданы каталоги:
  - **work** предназначена для скриптов вашего проекта. От сюда будут запускаться скрипты для работы в Spark.
  - **db_home** предназначена для хранения метаданных Spark и сохранения БД и таблиц даже после остановки контейнера.

## Запуск контейнера

В командной строке перейдите в каталог с проектом и запустите файл docker-compose.yml следующей командой (запуск контейнера в фоновом режиме):
```
docker-compose up -d
```
Посмотреть запущенные контейнеры можно командой:
```
docker ps
```
Чтобы остановить контенер, нужно из каталога проекта (где находитьс docker-compose.yml) выполнить команду:
```
docker-compose down
```


## Example
В проекте уже есть пример скрипта для запуска в Spark
> /work/hello.py

Из командной строки выполните команду:
```
docker exec -it pyspark spark-submit /work/hello.py
```
результат:
```bash
root
 |-- city: string (nullable = true)
 |-- state: string (nullable = true)
 |-- name: string (nullable = true)
 |-- age: long (nullable = true)

+-------+-------------+------+---+
|   city|        state|  name|age|
+-------+-------------+------+---+
|Tobolsk|Tyumen region|  Ivan| 18|
| Tyumen|Tyumen region|Andrey| 23|
| Moscow|       Moscow|  Ivan| 42|
+-------+-------------+------+---+
```

Чтобы провалиться внутрь контейнера выполните команду:
``` 
docker exec -it pyspark /bin/bash
```
Для запуска pyspark c поддержкой локальных баз данных, внутри контейнера выполните:
```
pyspark -c spark.sql.warehouse.dir=/db_home/warehouse
```
Посмотреть список баз данных:
```
spark.sql("Show databases").show()
```
```bash
+------------+
|databaseName|
+------------+
|     default|
|       newdb|
+------------+
```
посмотреть данные в таблице:
```bash
>>> spark.table("newdb.adress_age").show()
```
Для выхода из консоли pyspark используйте **ctrl+d**.

Выйти из doker контейнера:
```
exit
```

Для получения прав root внутри контейнера используйте комманду:
``` 
docker exec -it -u root:root pyspark /bin/bash
```  
