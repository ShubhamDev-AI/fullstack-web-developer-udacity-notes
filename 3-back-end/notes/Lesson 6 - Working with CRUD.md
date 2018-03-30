# Working with CRUD
When we talk about CRUD, it means we talk about ORM

## What will we learn?
- ORM
- 

#### ORM
Translator between code and SQL statement

**SQLAlchemy** - Best ORM for python

4 major coding components:
- Configuration: import modules
- Class: represent data
- Table: table in database
- Mapper

## SQLAlchemy 
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
```

#### Create
```python
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
```

#### Read
```python
firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
    print item.name
```

#### Update
- Find Entry
- Reset value(s)
- Add to session
- Execute session.commit()

```python
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
```

#### Delete
- Find the entry
- Session.delete(Entry)
- Session.commit()

```sql
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 
```

