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

- to remove the first row:

```
# to remove the first row
header = dataset.first()
dataset = dataset.filter(lambda x: x != header)
```
- good examples: [here](https://spark.apache.org/examples.html)

```
successfully found the most important providers at HQ within 1 million rows. (file: most-popular-hq=cnsumers.py
```
##### Super-heros degre e of separation:

There is an algorithm called __Breadth First Search__ that used to show the separation degree between the Heros in the heros datasset.

__Accumulators:__ It is a concept that makes different executors keep track of something together.

Basically we want to know how many connections we need to get through to get from sample A to sample B. 

check the photo called NFS.jpg that explains the algorithm. 

It starts with a node that we want to calculate the distance of other nodes from it we give it the value of zero and color of black. Then we find those directly connected to it. Then give them values of 1 and color of gray. Then for each of them run the algorithm and make them black and give the results 2 and color gray, and again for the results we run the algorithm and give the results value of 3 and color of gray. We will do it until all nodes have been reviewed which means all nodes get black.

- In the spark code first we need to make each row to be from
```
(5332 556 3235 6534 763 3 233)
```
to something like this:
```
(5332, (556, 3235, 6534, 763, 3, 233), 9999, white)
```

9999 is the default distance. (infinite)



