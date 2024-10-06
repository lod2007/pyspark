from pyspark.sql import SparkSession
import json
from pyspark.sql.functions import col



warehouse_location = "/db_home/warehouse"

def init_spark() -> SparkSession:
    return SparkSession \
        .builder \
        .appName("main") \
        .config("spark.sql.warehouse.dir", warehouse_location) \
        .enableHiveSupport() \
        .getOrCreate()


def main():

    spark = init_spark()    
    spark.sparkContext.setLogLevel("WARN")
    sc = spark.sparkContext

    # Create local database "newdb"
    spark.sql("CREATE DATABASE IF NOT EXISTS newdb COMMENT 'comment' LOCATION '/db_home/warehouse/newdb' WITH DBPROPERTIES (ID=001, Name='John') ")
    
    # Create data and save into table
    if not spark._jsparkSession.catalog().tableExists('newdb', 'adress_age'):
  
        jsonStrings = ['{"name":"Andrey","age":23,"city":"Tyumen","state":"Tyumen region"}',
                        '{"name":"Ivan","age":18,"city":"Tobolsk","state":"Tyumen region"}',
                        '{"name":"Ivan","age":42,"city":"Moscow","state":"Moscow"}']
        otherPeopleRDD = sc.parallelize(jsonStrings)
        otherPeople = spark.read.json(otherPeopleRDD)
        # Save table with partition 'name' & 'age'
        # repartition(1) - "save as..." single parquet-file
        otherPeople.repartition(1).write.mode("overwrite").partitionBy("name","age").saveAsTable("newdb.adress_age")

    otherPeople = spark.table("newdb.adress_age")
    otherPeople.printSchema()
    otherPeople.show()

if __name__=="__main__":
    main()