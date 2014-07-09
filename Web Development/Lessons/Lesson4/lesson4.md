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

