"""
signup_error.py

Simple web application that creates an HTML form with four inputs, and implements basic
escaping and error handling.
"""
import webapp2

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