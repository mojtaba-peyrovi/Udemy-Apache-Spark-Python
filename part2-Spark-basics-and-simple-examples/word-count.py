from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("word-counter")
sc = SparkContext(conf= conf)
###
input = sc.textFile("book.txt")
words = input.flatMap(lambda x: x.split())
wordCounts = words.countByValue()
###
for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if(cleanWord):
        print(cleanWord, count)
