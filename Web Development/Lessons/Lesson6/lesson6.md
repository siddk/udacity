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