### Apache Spark Tutorial with Frank Kane @ Udemy:
---
The full name of the course: "Taming big data with Apache Spark and Python"

##### Part 1: Getting Started:
I followed the steps to download Spark and all dependencies. It should be good to go.

- to prevent future confusion: He mentions a directory has has made called "SparkCourse". Instead of that, I made one inside my "tutorials" folder under this course and called it "my-spark-walkthrough". Also it is my root directory in my Github repo.

- I'm going to use Jupyter notebooks instead of Py files.
- Because the datafiles will be big and can't push them to Github I have to put them somewhere outside my walkthrough folder, so I made myDataFiles folder right next to walkthrough in my main tutorial folder.

##### Running Spark code to make a histogram on MovieLens data:

- What is new here, is a library called Collections. Here is the official definition:
```
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
```        
- In the code made in "ratings-counter.ipynb" there is an error for using iteritems() with collections.OrderedDict(). So I made the following change and it worked:
```
instead of sortedResults.iteritems()   said   sortedResults.items()
``` 



