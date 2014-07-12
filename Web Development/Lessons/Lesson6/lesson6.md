#Caching#

So far, we have been dealing with a small user base, and as such, we have been using a fairly small scale web design process. We have a single user base, with singular requests, and a single database. In this lesson, we will be learning how to scale, and serve multiple requests concurrently.

**Why do we Scale?**
1. Serve more requests concurrently
2. So we can store more data
3. SO we're more resilient to failure (redundancy)
4. So we can serve requests faster

**What do we Scale?**
1. Bandwidth
2. Computers (memory, CPU)
3. Power
4. Storage

We can scale across all four of these objects, though the scale-case varies depending on individual need.

##Techniques for Scaling##

1. The first option is to always look at optimizing your code. (Opportunity cost between developer time, and the cost of a machine).
2. **Cache Complex Operations** --> This is what we should do
3. Upgrade Machines
    + More memory
    + More disk space
    + Faster CPU
4. **Add more machines** --> In addition to caching, this is another go-to

##Caching##
Caching refers to storing the result of an operation so that future requests return faster. 

**When do we Cache?**
1. Computation is slow
2. Computation will run multiple times
3. When the output is the same for a particular input
4. Your hosting provider charges for Database access.

###Basic Cache algorithm###
A cache is basically a large hash-table (dictionary), with keys and values.

Here is the algorithm in pseudocode:

```python
if request in cache: --> Cache hit
    return cache[request] 
else: --> Cache miss
    r = db-read()
    cache[request] = r
    return r
```

And an actual implementation of the algorithm:

```python
import time

# complex_computation() simulates a slow function. time.sleep(n) causes the
# program to pause for n seconds. In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
    time.sleep(.5)
    return a + b

# QUIZ - Improve the cached_computation() function below so that it caches
# results after computing them for the first time so future calls are faster
cache = {}
def cached_computation(a, b):
    if ("(%d,%d)" % (a, b)) in cache:
        return cache["(%d,%d)" % (a, b)]
    else:
        c = complex_computation(a, b)
        cache["(%d,%d)" % (a, b)] = c
        return c

start_time = time.time()
print cached_computation(5, 3)
print "the first computation took %f seconds" % (time.time() - start_time)
```

##Scaling ASCIIChan##
When a user submits a request ot ASCIIChan, the following happens:

1. Our web application processes the request (HTTP, URL, Handler)
2. Query the database --> This is the redundancy we can cut out
3. Collate the results (sort)
4. Render the HTML (also a stop-gap)