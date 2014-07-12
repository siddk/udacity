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