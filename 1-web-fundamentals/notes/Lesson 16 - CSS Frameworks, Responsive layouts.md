# CSS Framework

## Screen
- The size of screen size, view port size and the HTML size
```javascript
// returns screen size (your laptop screen size)
screen.width
screen.height

// Return size of the view port
window.innerHeight
window.innerWidth

// returns the size of HTML Document
docment.documentElement.scrollHeight
docment.documentElement.scrollWidth
```
- When we talk about the *different size screen*, it means we're talking about the resolution of screen, not the physical size
- Nowadays, there are many screen size width: 2560px , 1024px, 960px
- We can still use a fullHD browser size (1920x1080) on the screen 1280x800 by resize the browser

## Grid
- We need to create 
    - `.row of 100% page width`
    - `columns of 1/12 - 12/12 page width` 
- Each tags have a default margin, padding or display.
    - Find here: https://www.w3schools.com/cssref/css_default_values.asp
    
## Some note
- `em`: Relative to the font-size of the element (2em means 2 times the size of the current font) 
- `display: block`: Take whole width of page
- `display: flex` to make columns in a same row
- negative space: 

## Negative space
Between 2 column, there needs to exit a space to view easier

## Overflow
A long texts are wrapped in a small area and use scroll.

## Media queries
When the width of web page changes to smaller than a specific pixels, we need to change CSS to adapt new width. 

Use `@media` to do this
```css
@media only screen and (max-width: 300px) {
    p {
        background-color: blue;
    }
}
```

## CSS Resetting
CSS normalize

## Place image
We can use some of this website to use sameple images with specific size

- placehold.it
- placepuppy.it
- placekitten.com

