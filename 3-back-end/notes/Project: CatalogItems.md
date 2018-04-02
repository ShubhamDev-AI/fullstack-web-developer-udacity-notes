# Catalog Items

## Step 1: Mockups
First step, we should define all pages we will create and its url

For this Catalog Items, I can list them here:

- `/`, `/catalogs`: Show all categories and 10 newest items
- `/catalog/new`: Create new catalog, redirect to `/catalog/<int:catalog_id>`
- `/catalog/<int:catalog_id>`: Catalog detail
- `/catalog/<int:catalog_id>/edit`: Update the catalog
- `/catalog/<int:catalog_id>/delete`: Delete the catalog
- `/catalog/<int:catalog_id>/items`: Show all items in list
- `/catalog/<int:catalog_id>/item/new`: Create new item
- `/catalog/<int:catalog_id>/item/<int:item_id>`/edit: Edit item
- `/catalog/<int:catalog_id>/item/<int:item_id>`/delete: Delete item


## Step 2: Add routes
In this step, we will define all routes in the mockups in Flask project. After finishing this, we can access all the link above without error

## Step 3: Add templates and render mockup data
Create templates for each route in `templates` folder. In each page need data, we can create mockup data.

## Step 4: CRUD
- First, Create class to implement ORM `SQLalchemy`. In this project, these are `Catalog` and `Item`


