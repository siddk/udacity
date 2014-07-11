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
```

##How Computers Communicate##
A basic manner of communication is to treat the server making the requests like a browser, and make HTTP requests to another server, and get the HTML from the other server. This is suboptimal and error-prone, as it requires one to parse the HTML.

The best manner of communication, is through **XML**

###XML###
Structured with tags, like HTML, but a little more consistent, and easier to parse.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<results>
  <itinerary>
    <leg>
      <origin>CUS</origin>
      <dest>WAS</dest>
    </leg>
  </itinerary>
</results>
```

Essentially, all HTML can be expressed in XML, and XML and HTML share a common lineage.

###Parsing XML###
There are thousands of XML parsers, and we will be using the minidom (xml.dom)library in Python. 

**DOM** stands for *Document Object Model*, refers to the document as an object that you will be messing with programmatically.

**MINIDOM Example**
```python
from xml.dom import minidom
# minidom.parseString() --> Function that parses an XML string
x = minidom.parseString("<mytag>...</mytag>") # Returns an xml document object
x.getElementsByTagName("tagname")[0].childNodes[0].nodeValue
# ^-- This is how we parse XML... the above example gets the value of the first object of the first child of the tag "tagname." 
```

##RSS##
RDF Site Summary, where RDF stands for Resource Description Framework.
More popularly, RSS is referred to as Really Simple Syndication.

An RSS is a giant XML document, holding a series of items and descriptions.
