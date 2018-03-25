# Databases

## What we will learn?
- Learn about SQL, and fundamental concepts of database
- Learn how to deploy database on google app engine's data store

## What is the databases?
> A program that stores and retrieves amounts structure data

## Why Database?
When the data is so big, we cannot load data in the memory to write function to extract information.

So `database` is here to take a big chunk of data and provide us functions to interact with that data.

## Types of database
- Relational databases (SQL)
    - Postgresql (Reddit, Skype, Instagram)
    - MySql (Facebook, everybody, )
    - SQLite (lightweight, simple, not use for huge system)
    - Oracle (acquired MySQL in 2010, the super huge and old system like banks, and aircraft)
    
    FYI, ["why oracle bought MySQL even they don't make money from it?"](https://www.quora.com/Why-did-Oracle-buy-MySQL-if-they-dont-even-make-money-out-of-it)
- NoSQL
    - MongoDB
    - Couch
- Cloud database
    - Google App Engine's Datastore
    - Dynamo (Amazon)
    
## SQL (Structure Query Language)
- Invented in 1970 - even before web's stuffs existed

#### Order by (default ASC -ascending, or DESC - descending)
```sql
select * from links where id=123 
order by time DESC 
```

#### Joins
Shouldn't use this

#### Indexes
Instead of scanning all records to find the correct row, databases use hash table to jump directly to the row that match the key.

**Tradeoff**
- Indexes *increases* speed of reading data
- But, decreases speed of inserting new data. Because database has to reindex data.

Watch [this](https://www.youtube.com/watch?v=31XAKJmp0sk) for real-world indexes, and proof how fast indexes is!

**Tree**

hashtable is not the only type of data stucture using in indexes. tree is other choice.

**Compare tree and hash table**

Hash table
- Faster look up 
- No sorted

Tree
- Sorted
- Slower look up (log n)

In many database, when we create index for a table, it allows us to choose what type of indexes (tree/hashtable) we want. It depends on what we want to use that table for. If that table will be used for query votes frequently, then tree is the best choice.  

Another cool example, [how Reddit ranking works](https://youtu.be/XkuT8x6Y94A)

## ACID
- **Atomicity**: all parts of a *transaction* (literally means *multiple commands*. For example, when user clicks vote for a post, the the post itself should be increased score, and the post's owner should be added reputation) succeed or fail together
- **Consistency**: the database will always be consistent
- **Isolation**: each transaction cannot effect other transaction
- **Durability**: once the transaction is commited, it wont't be lost

## Google App Engine Datastore
In Google App Engine Datastore, *tables* is called *entities*. Adding a new column in existing entity is quite troublesome in some popular databases but with Google App Engine DataStore, it's normal and handy.

## GQL
- GQL is a simplified version of SQK works only in DataStore
- Properties:
    - all queries begin with SELECT *
    - no joins
    - all queries must be indexed

## DataStore's Type
There are many types in DataStore like: integer, float, string, date, time, datetime, email, link, postal address

- String
    - < 500 characters
    - can be indexed
- Text
    - can be larger than 500 characters
    - can not be indexed