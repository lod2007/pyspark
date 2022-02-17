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

Run Hellow-world:

    docker run hello-world

## Приступая к работе (Getting started)

Для получения копии этого проекта необходимо клонировать проект к себе на машину командой:

    $git clone https://github.com/lod2007/pyspark.git your_project

после скачивания, в корне проекта создайте папку:

**work** - она понадобиться для передачи py-файлов внутрь контейнера. Туда поместите свой my_script.py для Spark.

## Запуск контейнера

В командной строке перейдите в каталог с проектом и запустите файл docker-compose.yml следующей командой:

    docker-compose up --build
  
## Example
  
  Для запуска командной строки внутри контейнера откройте терминал и запустите команду:
  
      docker exec -it pyspark bash
  
  В открывшемся терминале можете проверить:
  
      ls /home

 В результатом будет имя вашего файла /work/my_script.py

 В терминале контейнера перейдите в каталог с проектом

    cd /home

 и запустите свой скрипт командой:

    spark-submit my_script.py

 результат выполнения отобразится тут же в терминале.
