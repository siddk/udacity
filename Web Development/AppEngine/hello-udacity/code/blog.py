"""
blog.py

Pinnacle project of the Udacity Web Development Course CS 253. Implements a fully
functional blog using webapp2, built on Google App Engine, with a SQLite backend.
"""
from code.cookie import make_secure_val, check_secure_val
from code.handler import Handler
from google.appengine.ext import db
import cgi
import hashlib
import re

class Post(db.Model):
    subject = db.StringProperty(required = True)
    post = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class User(db.Model):
    user = db.StringProperty(required = True)
    pw = db.StringProperty(required = True)

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

class BlogSignupHandler(Handler):

    def render_page(self, user_error="", pass_error="", verify_error="", email_error="",
                    user_val="", pass_val="", verify_val="", email_val=""):
        self.render("signup.html", user_error = user_error, pass_error = pass_error, verify_error = verify_error, email_error = email_error, user_val = user_val, pass_val = pass_val, verify_val = verify_val, email_val = email_val)

    def get(self):
        self.render("signup.html", )

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify_password = self.request.get('verify')
        email = self.request.get('email')

        write_dict = {}
        if not (username and password and verify_password):
            self.render_page(user_error="Missing some fields", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        #Check if username is valid
        if not (re.compile(r"^[a-zA-Z0-9_-]{3,20}$")).match(username):
            self.render_page(user_error="Invalid username", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if not (re.compile(r"^.{3,20}$")).match(password):
            self.render_page(pass_error="Invalid password", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if not (password == verify_password):
            self.render_page(verify_error="Passwords do not match", user_val=cgi.escape(username, quote=True),
                pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                email_val=cgi.escape(email, quote=True))
            return

        if email:
            if not (re.compile(r"^[\S]+@[\S]+\.[\S]+$")).match(email):
                self.render_page(email_error="Invalid email", user_val=cgi.escape(username, quote=True),
                    pass_val=cgi.escape(password, quote=True), verify_val=cgi.escape(verify_password, quote=True),
                    email_val=cgi.escape(email, quote=True))
                return

        u = User(user = username, pw = hashlib.sha256(password).hexdigest())
        u_key = u.put()
        u_id = str(u_key.id())


        sts = make_secure_val(u_id)
        self.response.headers.add_header('Set-Cookie', 'visited=%s; Path=/' % sts)
        self.redirect("/blog/welcome")

class BlogWelcomeHandler(Handler):

    def render_page(self, user = ""):
        self.render("welcome.html", user = user)

    def get(self):
        hash_input = self.request.cookies.get("visited", '0')
        if hash_input:
            cookie_val = check_secure_val(hash_input)

