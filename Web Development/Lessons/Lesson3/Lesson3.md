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

| id   | name    | date    | password |
| ---  | ---     | ---     | ---      |
| *21* | user123 | 12/1/12 | password |

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


##SQL
**Structured Query Language**

SQL was invented in the 1970. It was built to solve some of the problems with computer datastores of the time, and has now adapted to become a mainstay of web applications and industry.

SQL is a way of structuring a query, or a command/question, for a relational databases (Postgres, MySQL, etc.). Like a programming language, it has it's own keywords, syntax, and structure.

Here is a basic SQL query.
```SQL
SELECT * FROM table WHERE id = 5;
```

The above query breaks down in the following manner:

1. **SELECT** *: Fetch all the column data for the following conditional
2. **FROM** table: Specifies which table you are querying
3. **WHERE** id = 5: Conditional statement --> Only select the data where id=5

###Other SQL Commands###

1. **ORDER BY** field **ASC**/**DESC** (ascending or descending)
2. **Join Query** - a type of SQL query across multiple tables that allows a cross-table conditional.
    + Example: ```SELECT * FROM table1, table2 WHERE table1.field = table2.field AND table2.field = something;```
3. **COUNT** --> ```SELECT COUNT(*) FROM table```
4. **EXPLAIN** QUERY --> Provides a description of search process during execution of query.
5. **ANALYZE** QUERY --> Gets fetch time, and necessary statistics

###Indices###
An index basically hashes a field, for a quicker lookup time. Works like a python dictionary (hash table). The command for building an index on a column in a SQL table is as follows:

```SQL
CREATE INDEX index_name on table.field;
```

##Scaling Databases##
There are really two reasons to scale a database.

1. Too much load -> A lot of reads hitting the same database at the same time
    + To remedy this, you can replicate your database, however many times
    + Issues:
        * No increase in write speed
        * Replication lag
2. Too much data -> Database is too big
    + Shard the data -> store some data on each database, with multiple databases
    + Essentially hash the keys in the key-value pairs, and store them in ranges in separate databases
    + Issues:
        * Complex queries
        * Database joins become difficult

For this Udacity course, the Google App Engine Datastore has the same limitations as the second Database scale. Complex queries, and joins are difficult/impossible to perform with the Datastore, though there is a provided SQL interface.

##ACID##

1. **Atomicity** - all parts of a transaction succeed or fail together
    + A transaction is a set of command
    + Basically, there will be no halfway in the execution of a transaction.
2. **Consistency** - The database will always remain consistent (linked fields)
3. **Isolation** - No transaction can interfere with another
4. **Durability** - Once a transaction is committed, it won't be lost
