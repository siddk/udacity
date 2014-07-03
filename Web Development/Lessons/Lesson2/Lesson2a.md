#Templates and Handlers#
##Handlers##
Handler class --> Use for ease of calling functions.

For example:
```python
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class Main(Handler):
    def get(self):
        self.write("Hello World")
```

- Other use cases for this as well, makes life easier.
- Can inherit same base class across multiple handlers.

##Templates##
+ A template library is a library to build complicated strings (html)
+ For this udacity course we will be using --> Jinja2.
+ Jinja2 is built into Google App Engine