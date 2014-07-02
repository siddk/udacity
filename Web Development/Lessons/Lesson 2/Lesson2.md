#Forms and Input#
HTML Form - manages input

######Example:######
```HTML
<form>
    <input name="name">
</form>
```

Input tag in the middle has attributes, one of which is "name"

##Form HTML##
```HTML
<input type="text" name="name"> - Creates a text field, with name=store
<input type="submit"> - Creates a button for submission
<form action="url"></form> - Sends results to specified url
<form method="post"></form> - Sends a POST (default GET)
```

Types - text, submit, password, checkbox, radio (same name), dropdown menu

##GET vs. POST##
######GET######
+ Parameters in URL
+ Used for fetching documents
+ Maximum URL length
+ OK to cache
+ Shouldn't change the server

######POST######
+ Parameters in body of request
+ Used for updating data
+ No max length
+ Not ok to cache
+ Ok to change the server

