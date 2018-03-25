# Forms and Inputs

## Forms

- To get data from web browser to web server
- Basic form
```angular2html
<form>
  <input name="name"/>
</form>
```
- What happened when enter text in a form?
```angular2html
The parameter in url will be change to value in form
```
- Instead of entering, we can create a button to click
```angular2html
<form>
  <input name="name"/>
  <input type="submit"/>
</form>
```
- To send text to some url, uses `action` attribute in `form` tag
```angular2html
<form action="http://www.google.com/search">
  <input name="name"/>
  <input type="submit"/>
</form>
```
- Url encoding
```
Browser's url accepts only ASSCI characters. So, If you type something non-ASSCI then browser will convert it into ASSCI.

For more detail, check this: https://www.w3schools.com/tags/ref_urlencode.asp
```
- Http request
```
In htp request, there is an intersting fact.
The referer show us which server sent the request.
But referer is a spell wrong, it should be referrer. But this typo error has existed for over 20 years.
```
- To use `post`
```angular2html
<form method="post" action="/url">
  <input name="name"/>
  <input type="submit"/>
</form>
```

#### Different between GET and POST

**GET**

- parameters in URL
- used for fetching document
- maximum URL length (<2000)
- Okay to cache (/kaSH/)

**POST**

- parameters in body
- used for updating data
- no max length
- not oke to cache

#### Why `POST` should be a form and never be a link?
An example about a to-do-list webapp. They allow user to login and create their to-do list. After creating a task, user can delete it by clicking a link beside.

At that time, google web accelerator - which will crawl all the link in the web to speed up when user clicks in that links later.

So, that bot click to 'Delete' links, and every tasks user created before are deleted. 

The problem will be solved if every post method is used `form` instead of url only

#### Other type of input in form
- checkbox
- radio
- dropdown
```angular2html
<select name="select">
    <option>one</option>
    <option>two</option>
    <option>three</option>
</select>
```

## Validation
We should validate value user send from web browser

## Html escaping
https://www.w3schools.com/html/html_entities.asp

```python
def escape_html(s):
    s = s.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;") \
        .replace('"', "&quot;")
    return s
```

## Why we need redirect?

Issues when server responses html directly when client `post` a form:

- user cannot share success link
- cannot reload the page without annoying message (browser always pop up)

So, instead of response a html page, server should response a redirect link to client, next, client request to that redirect link and get response a success page in different url.

