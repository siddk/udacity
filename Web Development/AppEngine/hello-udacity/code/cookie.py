"""
cookie.py

Sample web application to demonstrate basic cookie usage, hashing, and password
protection.
"""

SECRET = 'imsosecret'

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

class CookieHandler(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        visits = 0
        visit_cookie_str = self.request.cookies.get('visits', '0')
        if visit_cookie_str:
            cookie_val = check_secure_val(visit_cookie_str)
            if cookie_val:
                visits = int(cookie_val)

        visits += 1

        new_cookie_val = make_secure_val(str(visits))
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        # You can cheat this, by using the JS console, and just setting the cookie
        # Update: With new Hash, this is no longer the case
        if visits > 100000:
            self.write("You are the best ever!")
        else:
            self.write("You've been here %s times!" % visits)