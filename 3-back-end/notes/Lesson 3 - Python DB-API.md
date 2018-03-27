# Python DB-API

## What is Python DB-API?
Python DB-API is a **standard** to Python's libs to implement and connect to database system.

[Pep 249 - Python Database API Specification v2.0](https://www.python.org/dev/peps/pep-0249/)

With each database system, it has its own Python Client (implemented Python DB-API)
- SQLite - sqlite3
- PostgreSQL - psycopg2
- ODBC - pyodbc
- MySQL - mysql.connector

## Transaction when insert data to database
When we make *changes* such as: insert, delete, create, update -> a `transaction`

The transaction actually takes effect when call `commit`. If connection closes without committing, then the changes will get `rolled back`

E.g. Without `db.commit()`, new data will not be written in the database
```python
db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()
```

=> Make sure "Atomicity"

## Hello Postgresql
- Login vagrant
`vagrant ssh`
- Login postgres forum database
```
cd /vagrant/forum
psql forum
```

```
select * from posts;
```

```sql
update table set column = value where restriction ;
```

```sql
delete from posts where content like '%spam%';
```