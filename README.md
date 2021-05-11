# Pyspark from Ubuntu

 ![Docker pulls build](https://img.shields.io/docker/pulls/lod2007/pyspark)
 ![Docker Automated build](https://img.shields.io/docker/automated/lod2007/pyspark)
 ![Docker Image Version (latest by date)](https://img.shields.io/docker/v/lod2007/pyspark)

В данном проекте решена задача по развертыванию на Докере образ Ubuntu с установленным Pyspark  2.4.7.
В результате вы получите готовую среду для запуска скриптов Python для Spark.

Ссылка на репозиторий:

https://github.com/lod2007/pyspark

Версии программ:
![WordPress Plugin Version](https://img.shields.io/badge/python-3.7-green)
![WordPress Plugin Version](https://img.shields.io/badge/spark-2.4.7-orange)
![WordPress Plugin Version](https://img.shields.io/badge/hadoop-2.7-blue)
![WordPress Plugin Version](https://img.shields.io/badge/jdk-1.8.0_292-red)

## Приступая к работе (Getting started)


Предварительно вы должны скачать и установить у себя Docker Engine и Docker Compose.
Для установки на Linux Mint можно воспользоваться инструкцией:

https://tuxrider.ru/guide/ustanovka-docker-compose-linux-mint-19/

Для получения копии этого проекта необходимо клонировать проект к себе на машину командой:

    $ git clone https://github.com/lod2007/pyspark.git your_project

после скачивания, в корне проекта создайте папку: 

**work** - она понадобиться для передачи py-файлов внутрь контейнера. Туда поместите свой my_script.py для Spark.

## Запуск контейнера

В командной строке перейдите в каталог с проектом и запустите файл docker-compose.yml следующей командой:

    docker-compose up --build
  
## Example
  
  Для запуска командной строки в нутри контейнера откройте терминал и запустите команду:
  
      docker exec -it pyspark bash
  
  В открывшемся терминале можете проверить:
  
      ls /home
  В результатом будет имя вашего файла /work/my_script.py 
 
 В терминале проекта перейдите в каталог с проектом
 
    cd /home
    
 и запустите свой скрипт командой:
 
    spark-submit my_script.py
    
 результат выполнения отобразится тут же в терминале.
   
      
