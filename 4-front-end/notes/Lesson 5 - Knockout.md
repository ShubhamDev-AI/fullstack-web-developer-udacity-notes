# Knockout
Knockout.js is a library/framework to support MCV becomes MVVM

## Sugar syntax
#### Observable
To observe an element, use `ko.Obserable`

In html:
```html
<div data-bind="text: someText"></div>
```

In js:
```js
someText = "a text";
ko.applyBindings(someText);
someText = "other text"
```

#### Computed observable
```js
var ViewModel = function() {
    this.firstName = ko.observable("Jerry");
    this.lastName = ko.observable("Le");
    
    this.fullName = ko.computed(function(){
        return this.firstName() + " " + this.lastName();
    }, this);
}
```
