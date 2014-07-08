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
    * You can fetch cookies in HTTP Request