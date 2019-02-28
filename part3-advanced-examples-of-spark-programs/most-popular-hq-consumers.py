from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setMaster("local").setAppName("most-popular-consumers")
sc = SparkContext(conf = conf).getOrCreate()


filePath = os.path.abspath("C:\\Users\\mojiway\\Desktop\\tutorials\\Udemy - Taming Big Data with Apache Spark and Python - Hands On!0\\myDataFiles\\log-1M.csv")

logFile = sc.textFile(filePath)

def parse_customer_code(line):
    line_values = line.split(",")
    return (line_values[3],1)
code_pairs = logFile.map(parse_customer_code)

# to remove the first row
header = code_pairs.first()
code_pairs = code_pairs.filter(lambda x: x != header)

counts = code_pairs.reduceByKey(lambda x,y: x+y)
countsFlipped = counts.map(lambda x: (x[1],x[0]))

countsFinal = countsFlipped.sortByKey(ascending=False)

final = countsFinal.map(lambda x:(x[1], x[0])).collect()

print(final)
