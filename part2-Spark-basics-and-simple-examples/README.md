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

RDD's can hold key-value pairs as well as single values. For example: number of friends by age.

the key is age and the value is the number of friends.

##### Spark's special operations with key-value pairs:

- ReduceByKey(): combine values with the same key using some function. example: rdd.reduceByKey(lambda x,y: x+y)
- groupByKey(): group values with the same key
- sortByKey(): sort rdd values by key
- keys(), values(): create an RDD of just the keys, or just the values.
- with value-key pairs, we use mapValues() and faltMapValues() instead of map() and flatMap() if the transformation doesn't affect the keys.

__Friends by age example:__ 

we make value pairs for age and friends for each line. Then we convert the values to another pair that the second value is 1. we do it becuase later we want to count the occurance of each line.
for example: (33, 385) => (33,(385,1))

Then next step is, with reduceByKey() for each value pair like (385, 1) in the example above, we sum up the first, and second number to see how many friends each person has, and how many times the age repeats.

And because we want the average for each age, we write another lambda, to divide first value to the second which is the sum divided by count. Don't forget when we don't want the keys to be touched, we have to use mapValues().

__Filtering RDD example:__

It uses the concept of key-pair values in RDD and filter() functionality that means we get rid of the data we don't care about and just return the data we need. here is the code:

```
minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
```

It says for each row, if the field no 1 (which is the status) equals "TMIN", then keep it, otherwise drop it.
