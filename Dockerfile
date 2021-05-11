FROM ubuntu

# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk openjdk-8-jre \
    software-properties-common \
    wget && \
    rm -rf /var/lib/apt/lists/*

# Add repository
RUN add-apt-repository ppa:deadsnakes/ppa
    
# Install pyhton3.7
RUN apt-get update && apt-get install -y python3.7

#Install Spark 2.4.7
RUN wget -c -N https://apache-mirror.rbc.ru/pub/apache/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz && \
    cd / && tar xvz -f spark-2.4.7-bin-hadoop2.7.tgz -C / && \
    rm -f /spark-2.4.7-bin-hadoop2.7.tgz


#Environment variable -- переменные среды
ENV JAVA_HOME "/usr/lib/jvm/java-8-openjdk-amd64"
ENV SPARK_HOME /spark-2.4.7-bin-hadoop2.7
ENV PATH $PATH:$SPARK_HOME/bin
ENV PYTHONPATH $SPARK_HOME/python:$PYTHONPATH
ENV PYSPARK_PYTHON python3.7
ENV PATH $PATH:$JAVA_HOME/jre/bin
