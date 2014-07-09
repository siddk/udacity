#User Accounts and Security#

##Cookies##
+ Small piece of data stored in the browser by a website
+ Temporary information that a browser wants to store (User_ID, info, etc.)
    * Example: Cookie holds user_id, to know that you are currently logged in
+ Cookie is locked to a domain --> udacity.com 

###Cookie-Headers###
+ Cookies are instantiated in the HTTP Response, as a **Cookie-Header**
+ Set-Cookie: user-id = 12345 --> Response header
    * Note that Set-Cookie happens in HTTP Response
    * You can fetch cookies in HTTP Request: One header, with all cookie vals
+ Cookies also may have an Expiration parameter, which sets an expiration date
    * A "Session" Cookie has no expires

###Cookie-Domains###
Format of a Set-Cookie header is as follows:
```
Set-Cookie: name = Steve; Domain = www.reddit.com; Path=/
```

The domain is always key to handling cookies. In the above code, the domain is www.reddit.com. The browser will only store cookies from the specified domain. For example, the browser will only accept the (Receive) Set-Cookies from the following domains (Which domains could receive a Set-Cookie?):

+ www.reddit.com
+ something.www.reddit.com

(Received) Set-Cookie will work with the specified domain, and any parent domain (that is to say, a domain of which the specified domain is a subdomain)

If the question were which of these domains could actually set a cookie, the same would apply.

##Hashing##
A Hash is a function such that H(x) -> y. In this function, the parameter x is data (in our case, a string), but the output y is always a fixed length bit string (32 - 256 bits).

**Properties of a Hashing Function:**

+ Difficult to generate a specific y
+ Infeasible to find x for a given y
+ Can't modify x without modifying y

###Hash Algorithms###
Note: For security purposes, don't write your own!

1. crc32 - checksums, fast --> creates a hash of a large file
    + Prone to collisions (two things hash to the same value)
    + Main use-case is when speed is necessary
2. md5 - fast, secure (not anymore)
    + Very easy to reverse... given a y, you can find an input x that works very easily (collisions).
3. sha1 - Secure(ish)
4. sha256 - Pretty good 
    + Comparatively pretty slow

###Hashing in Python###
```python
import hashlib

x = hashlib.md5("foo!")
print x # Returns <md5 HASH object @ memloc>

x.hexdigest() # Returns the hex string '35a....737'
```

###Hashing Cookies###
Here is the basic procedure of hashing a cookie:

1. Set-Cookie: visits = 5, *hash* --> to browser 
2. From browser --> Check that Hash of the value (5) == *hash*

Sample implementation of creating the hashed cookie:

```python
import hashlib

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return s + "," + hash_str(s)
```

We then feed the result of make_secure_val into our Set-Cookie function. On checking the hashed cookie, we can use the following function:

```python
def check_secure_val(h):
    splitr = h.split(',')
    if (hash_str(splitr[0]) == splitr[1]): 
        return splitr[0]
    else:
        return None
```

The issue with this is that this still is not secure. If a hacker can guess which hash we are using, it is trivial for them to get around this.

In order to remedy this, we should do the following. Rather than hashing just the cookie string, and storing it as (string, hash(string)), we should instead store it as (string, hash(secret_string+string)), where secret_string is a special phrase that only we are privy to. Therefore, a hacker would have to know our password to get around this.

We will be using the Python HMAC (Hash-based Message Authentication Code) Library, which has a constructor of the form ```hmac(secret, key, hash)```

####Hashing with HMAC####
This is the implementation for our new Hashing function.

```python
import hmac

SECRET = 'imsosecret'
def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val
```

####Password Hashing with Salts####
Here is an implementation of Password hashing with Salts:

```python
import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)

h = make_pw_hash('spez', 'hunter2')
print valid_pw('spez', 'hunter2', h)
```