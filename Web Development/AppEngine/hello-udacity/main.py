#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import re
import cgi
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
        self.write("Welcome to Sidd's Site for the Udacity Web Development Course CS 253")

class ROT13Handler(webapp2.RequestHandler):
    def rot13(self, cipher_text):
        return_string = ""
        for character in cipher_text:
            if character.isalpha():
                int_char = ord(character) + 13
                if character.isupper():
                    if int_char > ord('Z'): int_char -= 26
                else:
                    if int_char > ord('z'): int_char -= 26
                return_string += chr(int_char)
            else:
                return_string += character
        return return_string

    def write_form(self, input_text=""):
        input_text = self.rot13(input_text)
        self.response.out.write(rot_13_form % {"textarea": input_text})

    def get(self):
        self.write_form()

    def post(self):
        input_text = self.request.get('text')
        self.write_form(input_text)
rot_13_form = """
<form method="post">
    Enter text to be ROT13 Encrypted:
    <br>

    <textarea name="text">%(textarea)s</textarea>

    <br>
    <br>
    <input type="submit">
</form>
"""

class SignupHandler(webapp2.RequestHandler):

    def write_form(self, user_error="", pass_error="", verify_error="", email_error="",
                    user_val="", pass_val="", verify_val="", email_val=""):
        self.response.out.write(signup_form % ({"user_error": user_error,
                                                "pass_error": pass_error,
                                                "verify_error": verify_error,
                                                "email_error": email_error,
                                                "user_val": user_val,
                                                "pass_val": pass_val,
                                                "verify_val": verify_val,
                                                "email_val": email_val}))

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_password = self.request.get('verify')
        email = self.request.get('email')

        write_dict = {}
        if not (username and password and verify_password):
            self.write_form(user_error="Missing some fields", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        #Check if username is valid
        if not (re.compile(r"^[a-zA-Z0-9_-]{3,20}$")).match(username):
            self.write_form(user_error="Invalid username", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if not (re.compile(r"^.{3,20}$")).match(password):
            self.write_form(pass_error="Invalid password", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if not (password == verify_password):
            self.write_form(verify_error="Passwords do not match", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if email:
            if not (re.compile(r"^[\S]+@[\S]+\.[\S]+$")).match(email):
                self.write_form(email_error="Invalid email", user_val=cgi.escape(username, quote=True),
                    pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                    email_val=cgi.escape(email, quote=True))
                return

        self.redirect("/unit2/welcome?username=%s" % cgi.escape(username, quote=True))
signup_form = """
<form method="post">
    <h1>Signup</h1>
    <label>Username <input type="text" name="username" value="%(user_val)s"></label>
    <span style="color: red">%(user_error)s</span> <br>
    <label>Password <input type="password" name="password" value="%(pass_val)s"></label>
    <span style="color: red">%(pass_error)s</span> <br>
    <label>Verify Password <input type="password" name="verify" value="%(verify_val)s"></label>
    <span style="color: red">%(verify_error)s</span> <br>
    <label>Email (optional) <input type="text" name="email" value="%(email_val)s"></label>
    <span style="color: red">%(email_error)s</span> <br>
    <input type="submit">
</form>
"""

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.out.write("Welcome, %s!" % username)

class HardCodedTemplateHandler(Handler):
    def get(self):
        output = template_form
        output_hidden = ""
        output_items = ""

        items = self.request.get_all("food")
        if items:
            for item in items:
                output_hidden += template_hidden % item
                output_items += template_item % item

            output_shopping = template_shopping_list % output_items
            output += output_shopping

        output = output % output_hidden

        self.write(output)
template_form = """
<form>
<h2>Add a Food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

template_hidden = """
<input type="hidden" name="food" value="%s">
"""

template_item = """
<li>%s</li>
"""

template_shopping_list = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</u
"""

class TemplateHandler(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render('shopping_list.html', items = items)

# ASCII Chan Project
class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class AsciiChanHandler(Handler):
    def render_page(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("ascii.html", title = title, art = art, error = error, arts = arts)

    def get(self):
        self.render_page()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(title = title, art = art)
            a.put()

            self.redirect("/unit3/asciichan")
        else:
            error = "We need both a title and some artwork!"
            self.render_page(title, art, error)

# Blog
class Post(db.Model):
    subject = db.StringProperty(required = True)
    post = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class BlogHandler(Handler):
    def render_page(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
        self.render("blog.html", posts = posts)

    def get(self):
        self.render_page()

class PostHandler(Handler):
    def render_page(self, subject="", post="", error=""):
        self.render("post.html", subject = subject, post = post, error = error)

    def get(self):
        self.render_page()

    def post(self):
        subject = self.request.get("subject")
        post = self.request.get("content")

        if subject and post:
            p = Post(subject = subject, post = post)
            p_key = p.put()

            self.redirect("/blog/%d" % p_key.id())
        else:
            error = "We need both a subject and a post!"
            self.render_page(subject, post, error)

class PermalinkHandler(BlogHandler):
    def get(self, post_id):
        s = Post.get_by_id(int(post_id))
        self.render("blog.html", posts = [s])

class CookieHandler(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = self.request.cookies.get('visits', '0')

        if visits.isdigit():
            visits += 1
        else:
            visits = 0

        self.response.headers.add_header('Set-Cookies', 'visits=%s' % visits)

        self.write("You've been here %s times!" % visits)

app = webapp2.WSGIApplication([('/', MainHandler), ('/unit2/rot13', ROT13Handler), ('/unit2/signup', SignupHandler), ('/unit2/welcome', WelcomeHandler), ('/unit3/hard_coded_templates', HardCodedTemplateHandler), ('/unit3/templates', TemplateHandler), ('/unit3/asciichan', AsciiChanHandler), ('/blog', BlogHandler), ('/blog/newpost', PostHandler), ('/blog/(\d+)', PermalinkHandler), ('/cookies', CookieHandler)], debug=True)
