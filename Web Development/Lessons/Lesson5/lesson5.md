#APIs#
##HTTP Clients##
So far, we have been dealing with a very simple system. We have a user, who on his browser navigates to our website, and sends a request over HTTP to our servers.

Now, we will be discussing how to manage the connection between servers and other servers (over HTTP), through the use of an API. This allows for more flexibility and more functionality. 

###HTTP Requests in Python###
```python
import urllib2

p = urllib2.urlopen("http://www.google.com") # Creates a file object (can read)
c = p.read() # HTTP Response

# Example: Find the server www.example.com uses
x = urllib2.urlopen("http://example.com")
# x -> <addinfourl at 4339525968 whose fp = <socket._fileobject object at 0x102a66450>>
headers = x.headers
# headers -> <httplib.HTTPMessage instance at 0x102a7e830>
server = headers['server']
# server -> ECS (rhv/818F)