"""
wiki.py

Final project for Udacity course CS 253. Implements a fully editable wiki, with page creation, and page editing fully available. Built with webapp2, deployed on Google App Engine, with SQLite backend.
"""
from code.cookie import make_secure_val, check_secure_val
from code.handler import Handler
from google.appengine.ext import db
from google.appengine.api import memcache
import cgi
import json
import hashlib
import math
import re
import time

class User(db.Model):
    user = db.StringProperty(required = True)
    pw = db.StringProperty(required = True)

class WikiMainPageHandler(Handler):
    def render_page(self):
        self.render("wiki.html")

    def get(self):
        self.render_page()

class WikiSignupHandler(Handler):
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
        self.redirect("/wiki")

class WikiLogin(Handler):
    def render_page(self, error = "", user_val = "", pass_val = ""):
        self.render("login.html", error = error, user_val = user_val, pass_val = pass_val)

    def get(self):
        self.render_page()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        if not (username and password):
            self.render_page(error = "Missing login info", user_val = username, pass_val = password)

        users = db.GqlQuery("SELECT * FROM User")
        for user in users:
            if user.user == username:
                pw = hashlib.sha256(password).hexdigest()

                if user.pw == pw:
                    u_key = user.put()
                    uid = str(u_key.id())
                    sts = make_secure_val(uid)
                    self.response.headers.add_header('Set-Cookie', 'visited=%s; Path=/' % sts)
                    self.redirect("/wiki")

                else:
                    self.render_page(error = "Invalid login", user_val = username, pass_val = password)

class WikiLogout(Handler):
    pass

class EditPage(Handler):
    pass

class WikiPageHandler(Handler):
    pass