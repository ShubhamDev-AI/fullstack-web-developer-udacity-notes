# Notes of Postgresql syntax

#### Basic
- To open psql
```
> psql
```
- To quite psql
```
> \q
```
- List all existing database
```
> \list
```
- Connecting to database or switch to other database
```
> \connect database_name
```
- Create database
```
> CREATE DATABASE database_name
```
- Delete database
```
> DROP DATABASE database_name
```
- List tables in current database
```
\dt
```
- List all columns in a table
```
\d+ table_name
```

#### CRUD
- Create table
```sql
Create table table_name(
	col1 datatype constraint,
	col2 datatype constraint
);
```
- Insert data
```sql
INSERT INTO table_name(col1, col2, ..) 
VALUES (value1, value2, ..);
```

#### Constraint
- Primary key
    - Create table with primary key
    ```sql
    CREATE TABLE (
        id INTEGER PRIMARY KEY ,
        name text NOT NULL
    );
    ```
    - Modify after creating table
    ```
    ```
- Foreign key


#### Self joins
A table can be joined by itself 

#### Left join, Right join
In some case, when use join, some row will not be join because it doen't have common value on the column join. But we still want to count zero for the None. Thus, use `left join` or `right join` to keep both value and None.

## Sub queries
- Select on the result of other select queries
```
-> select -> Result table -> select -> Result table
```

E.g: Find the players having weight less than average weight
```sql
select name, weight from players,
        (select avg(weight) as av from players) as avtable
        where weight < avtable.av;
```

## View
- When we use a query a lot, then we can make a temporary table to store the result in order to reuse in the next time without quering again. That temporary table called `View`
- In each database system, we can update or delete the View, or cannot.

 
