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

An RSS is a giant XML document, holding a series of items and descriptions. The following is an example of parsing out the number of items in an RSS XML document.

```python
import urllib2
from xml.dom import minidom

# Get number of elements at the following url
p = urllib2.urlopen("http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml")
xml_string = p.read()
parse = minidom.parseString(xml_string)

lst = parse.getElementsByTagName("item")
len(lst) # Returns 25
```

##JSON##
JSON, like XML, is an human-friendly and computer-friendly way to represent data. JSON stands for JavaScript Object Notation. Stores things in dictionaries (dicts like python), and everything is denoted with nesting pairs of curly braces, and key-value pairs. Anything you can express in XML can be expressed in JSON, without the unnecessary tags.

###Parsing JSON with Python###

```python
import json
j = '{"one": 1, "numbers": [1,2,3.5]}'
json.loads(j) # Returns a python dictionary

d = json.loads(j)
d['numbers'] # Returns [1, 2, 3.5]

# Reddit Example
reddit_front = ... # Json string
# Inside the JSON is a series of links, each with an "up" attribute. Find the total number of ups of all the links.

def total_ups():
    parsed = json.loads(reddit_front)
    x = parsed['data']
    x = x['children']
    count = 0
    for i in x:
        count += int(i['data']['ups'])
    return count
```
