from pyspark import SparkConf, SparkContext
import collections
import os



conf = SparkConf().setMaster("local").setAppName("popular-movies")
sc = SparkContext(conf = conf).getOrCreate()

def most_popular():
    # importing the datafile with absolute path
    filename = os.path.abspath("C:\\Users\\mojiway\\Desktop\\tutorials\\Udemy - Taming Big Data with Apache Spark and Python - Hands On!0\\myDataFiles\\ml-100k\\u.data")
    lines = sc.textFile(filename)
    movies = lines.map(lambda x: (x.split()[1]))
    moviesCounts = movies.countByValue()
    sorted_movies = sorted(moviesCounts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_movies
