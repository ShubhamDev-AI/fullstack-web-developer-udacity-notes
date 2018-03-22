# Bootstrap and other framework

## Grid in bootstrap

- Use `container` for center grid
- Use `row` for each row
- Use `col-md-<number>` to split into columns
- Use `img-responsive` to fit image to width of browser

## Bootstrap typography

To beautify the typography, using some classes like:

- `text-right` : to align right
- `text-uppercase` : to capitalize all characters

## Watch a front end transform a mockup into real web page

Lesson 17: 13-14

## Pop up an image and other information?
Using `modal`, `data-toggle` and `data-target`
```angular2html
<div class="modal fade" id="project1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="myModalLabel">Favorite App Page</h4>
      </div>
      <div class="modal-body">
        <img class="img-responsive" src="http://www.placepuppy.net/555/300">
        This was my first project in this class. I learned a lot about HTML and CSS.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
```

