Lesson 1 - How the Web Works
============================
HTML - Hyper Text Markup Language

Browser --> Internet --> HTTP Requests --> Servers
    -Servers will serve HTML files that will be rendered in your browser

HTML tags and syntax
--------------------
The following are some common HTML tags, with set behaviors

Bold, Italics - <b>Boldface content</b>, <em>Italicized content</em>
Hyperlinks - <a href="http://url.com">Link text</a>
Images - <img src="http://imgsrc" alt="Alt text">
    - Inline element
Whitespace - <br>
    - Inline element
Paragraph - <p>Paragraph content</p>
    - Line breaks between paragraphs
    - Block element
Span - <span>span inline content</span>
    - Inline element wrapper (for CSS)
Div - <div>div block content</div>
    - Block element wrapper (for CSS)

Structure of an HTML document
------------------------------
<!DOCTYPE HTML> - Document type
<html> - HTML tag, surrounds the document

<head> - Metadata tag, has CSS, JS scripts
    <title>TITLE!</title> - Title of page
</head>

<body> - Wraps the content
    <b>Content...</b>
</body>

</html>

URLS
------
Uniform Resource Locator
http://udacity.com/src/something = Protocol://Host.com//Path

Query Parameters (GET parameters)
    http://examplel.com/foo?p=1&q=neat
                            Name = value
    Format: After URL path, ? designates query, & tacks on additional queries

Fragment (reference a part of a page)
    http://example.com/foo#fragment
                          Designates a location on a page, stays in browser (not a server request)
                          Goes after Queries

Localhosting
    http://localhost:8000/path
                    Port - default is 80
                    Specify port in between host and path


HTTP
------
Hypertext Transfer Protocol
http://www.example.com/foo --> GET /foo HTTP/1.1 (request line) --> format: METHOD /path http-version
    - No hostname, because hostname makes connection

GET / POST --> potential methods

GET Example
    http://example.com/foo/logo.png?p=1#tricky
    --> GET /foo/logo.png?p=1 HTTP/1.1
    - Ignore fragments


HTTP Requests
---------------
Structure: Request line, then headers
    - Headers:
              - Name: Value

Example:
    GET /foo?p=1 HTTP/1.1
    Host: www.example.com
    User-Agent: Chrome


HTTP Responses
--------------
Request              <-------------------->     Response
GET /foo HTTP/1.1                               HTTP/1.1 200 OK

Structure of a Response: HTTP/Version# StatusCode ReasonPhrase

Sample Status Codes
    - 200 OK
    - 302 Found
    - 404 Not found
    - 500 Server Error

Sample Response with Headers:
    HTTP/1.1 200 OK
    Date: Tue Mar 2012 04:33:33 GMT
    Server: Apache/2.2.3
    Content-Type: text/html;
    Content-Length: 1539


TELNET
---------
Way to watch/make HTTP requests to a console

Example (in terminal):
    telnet iana.org 80 (command, host, port)
    GET /domains/example HTTP/1.0 ---> GET request w/ Header
    Host: iana.org


Servers
---------
Purpose: respond to HTTP requests

Two key responses to HTTP requests:
    - Static
        - pre-written files
        - image
    - Dynamic
        - Made on the fly (programatically)
        - Web application
