### Intro to Spark SQL:
---

It can extend RDD to a dataframe object and treat it like a normal relational database. We can run SQL queries on that.

It is a very powerfil API that makes data manipulation so much easier with easier code and faster time. For example, we don't need to do raw Spark to find out the number of the movies, or sorting movies by having the key-pair values twisted, then treated values as the key, sorting them, etc. 

With Spark SQL, you can make your own function in Python, and then use it in SQL syntax. Very interesting. 

(photo: make-funciton-in-sql.jpg)

For using this feature, we need to import SparkSession and Row from pyspark.sql. 

Then we build the session as we can see in the code.  

The mapper function just cuts each line of the csv file, and makes them as rows.

After this, we need to use SparkSession.createDateFrame() to officially make the dataframe as we see in the code.

createOrReplaceTempView() function, makes a temporary view of the dataframe so that it will be ready to run SQL on it.

The code popular-movies-dataset.py is another example of using spark sql.