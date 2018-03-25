# Templates

## Hidden input
When use hidden input in a form. All value from text box and value from *hardcore* value will be represented in the url parameters.

E.g.
```angular2html
<form>
    <h2>Add a food</h2>
    <input type="text" name="food">
    <input type="hidden" name="food" value="eggs">
    <button>Add</button>
</form>
``` 

Both value from text box and `eggs` is going to present in url

## Templates

> A template library is a library to build complicated strings

`jinja2` is a library which is supported by Google App Engine for templates
