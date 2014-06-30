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
import re
import cgi

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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Welcome to Sidd's Web Development Test Site for Udacity Course CS 253")

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

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.out.write("Welcome, %s!" % username)

app = webapp2.WSGIApplication([('/', MainHandler), ('/unit2/rot13', ROT13Handler), ('/unit2/signup', SignupHandler), ('/unit2/welcome', WelcomeHandler)], debug=True)
