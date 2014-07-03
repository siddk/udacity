#Databases#

A **database** is a program that stores and retrieves large amounts of structured data.

The web development hierarchy is as follows (in order):

1. **User** (Browser)
2. **Internet**
3. **Servers**, which consist of two parts.
    1. **Web Application Servers**, the servers that host the code for the website. In this case, this is our AppEngine python code.
    2. **Databases**, which can run on one machine, or across multiple machines.

Web Application Servers will communicate with the database. This means that all database requests are routed through the Web Application.

##Tables##
Essentially, a database acts as a series of tables, with multiple rows and columns. 

Here is an example of a database for the website reddit.com, with tables for links and users:

**Link Table**

id | votes | user | date | title | url
--- | --- | --- | --- | --- | ---
3 | 74 | *21* | 1213 | Zombie Apocalypse | zombieapocalypse.com

**User Table**

id | name | date | password
--- | --- | --- | ---
*21* | user123 | 12/1/12 | password

Notice how the **User** field in the first table is a number. Basically, it is referring to the ID of a User in the User table. A lot of fields in databases are essentially references to IDs in other tables, and that is how relationships are stored, and easily found.

Table columns will have an associated type. For example, here are the types for the **Link Table** above:

1. id: Int
2. votes: Int
3. User: Int
4. Date: Int (Type MMDD)
5. Title: String
6. URL: URL 

Here is a sample implementation of our Link Table in Python:

```python
# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.", 
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html")]

# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is 
# a Link.
```

###Downsides of Databases###
A Database **Query** is essentially a statement that has the database look for a value. For example, a query for our links database above is ```"Find the number of votes for the link with id = 23."```

But, querying databases by hand has its downsides:

1. Error-prone
2. Tedious
3. Slow - especially with more data

##Types of Databases##

1. Relational (SQL)
    - Postgresql - reddit, hipmunk
    - MySQL - Facebook, everybody
    - SQLite (Lightweight and simple)
    - Oracle 
2. Google App Engine's Datastore
    - Similar to SQL databases
3. Amazon's Dynamo
    - Completely different from SQL
4. NoSQL Databases
    - Tries to solve limitations of SQL databases
    - MongoDB
    - CouchDB



