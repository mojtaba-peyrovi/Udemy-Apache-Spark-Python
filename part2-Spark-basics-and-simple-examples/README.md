### Part 2: Spark basics and simple examples:
---
#### Why Spark is so popular?
- Scalability: Spark can run big data analysis tasks by dividing the tasks between multiple nodes and get it faster and cheaper. It uses "Cluster Manager" system. It has its own built-in cluster manager or we can use YARN with Hadoop or cloud services like AWS, which has a service called EMR (Elastic MapReduce)
- Fastness: It is upto 100x faster than hadoop MapReduce.
- It is easy to code because it uses Python, Java , or Scala. Also, it is built around one main concept which is RDD (Resilient Distributed Dataset)

#### Libraries on the top of Spark:

There are several libraries that are built on the top of Spark:

  - Spark Streaming: To process real time data.
  - Spark SQL: used to run sql queries on the top of big datasets.
  - MLLib: To run machine learning algorithms on big data
  - GraphX: It is Apache Spark's API for graphs and graph-parallel computation.

__IMPORTANT:__ Scala is the native language of Spark, So it is a bit faster to use Scala on Spark compared to Python, but Python is more handy asn easy to use.
Also, Scala python and scala Scala are so similar. 

#### RDD: 
First the RDD's are Datasets, which are objects made by Spark and they are distributable and run along multiple cores, and also they are resilient, which means they can keep running if some of the cores fail to deliver their task.

#### SparkContext(SC):

- It is responsible for making RDD's. 

#### Creating RDD's:
- it can be made by sc.textFile() from local machine, or s3n://, and hdfs:// ptotocols.
- we can make RDD's using HiveContext()
- HDBC database, Cassandra, HBase, ElasticSearch, JSON, csv, etc.

#### Transforming RDD's:

- map(): simila to lambda.
```
rdd = sc.parallelize([1,2,3,4])
rdd.map(lambda x:x*x)
it returns 1,4,9,16
```
- flatmap(): similar to map, transforms one RDD to another, but the RDD's don't need to be of the same size like map(). they can have different sizes.
- filter(): you can filter the data we need to work on and cut out others.
- sample(): runs samples from the main dataset.
- union(), intersection(), subtract(), and cartesian(): similar to SQL.

#### RDD actions:

- collect(): to dump all the data inside the RDD
- count(): counts all values in RDD
- countByValue(): counts the number of each values.
- take(), top(): to take some samples of your data
-  reduce(): making some sort of aggregation on your data

##### The most important charcteristic of Spark:
It is lazy, which means nothing actually happens in the driver program, until an action is called.

