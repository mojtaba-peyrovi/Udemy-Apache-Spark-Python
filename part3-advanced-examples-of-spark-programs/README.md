### Advanced spark Examples:
---

#### Finding the most popular movie:

__Pipelinedrdd:__ PipelinedRDD is just special type of RDD which is created when you run a map function on an RDD.

In order to see the contents of the pipelinedrdd, we need to call collect() function. like this:
```
movies.collect()
```
- what if we want the name of each movie to be transferred with the movie id to each executor in the cluster?

There is a funcitons called __boradcast()__ that will ship information we want with the results.

- after calling the broadcast() we need to add .value() to retrieve the values.

__Broadcast Variables:__ When we want a variable to be accessible for all executors and clusters all the time, we can have it broadcasted. THis is so handy because imagine if data volume is so massive, anytime any executor needs some variables, the whole dataset has to be loaded for them.


__IMPORTANT:__ Python dictionaries are also called __map__, __hashmap__, __lookup table__, and __associative array__.

In order to see the values inside the broadcasted variable we say:
```
<variable_name>.value
```
__IMPORTANT:__ 

In the video, he showed somehting else for flipped variable calculation:
```
flipped = movieCounts.map( lambda (x, y): (y,x))
```
This doesn't work. Later in his files he has changed it to this:
```
flipped = movieCounts.map( lambda x : (x[1], x[0]))
```
and it works.


