#!/usr/bin/env python
"""
main.py

Renders a webapp2 web application, for the Udacity Web Development Course CS 253.
Built on Google App Engine, with jinja2 templating, and a SQLite backend.
"""
import webapp2
from code.rot13 import ROT13Handler
from code.signup_error import SignupHandler, WelcomeHandler
from code.template import TemplateHandler, HardCodedTemplateHandler
from code.ascii import AsciiChanHandler
from code.handler import Handler
from code.blog import BlogHandler, PostHandler, PermalinkHandler, BlogSignupHandler
from code.cookie import CookieHandler

class MainHandler(Handler):
    def get(self):
        self.write("Welcome to Sidd's Site for the Udacity Web Development Course CS 253")

app = webapp2.WSGIApplication([('/', MainHandler), ('/unit2/rot13', ROT13Handler), ('/unit2/signup', SignupHandler), ('/unit2/welcome', WelcomeHandler), ('/unit3/hard_coded_templates', HardCodedTemplateHandler), ('/unit3/templates', TemplateHandler), ('/unit3/asciichan', AsciiChanHandler), ('/blog', BlogHandler), ('/blog/newpost', PostHandler), ('/blog/(\d+)', PermalinkHandler), ('/blog/signup', BlogSignupHandler), ('/cookies', CookieHandler)], debug=True)
