# Elements of SQL

## Data types
- text
    - text — a string of any length, like Python str or unicode types.
    - char(n) — a string of exactly n characters.
    - varchar(n) — a string of up to n characters.
- integer
    - integer — an integer value, like Python int.
    - real — a floating-point value, like Python float. Accurate up to six decimal places.
    - double precision — a higher-precision floating-point value. Accurate up to 15 decimal places.
    - decimal — an exact decimal value.
- date: must put into single quotes, unless SQL treats it like an expression 
    - date — a calendar date; including year, month, and day.
    - time — a time of day.
    - timestamp — a date and time together.
    
```sql
`2012-02-03`
```

[PostgreSQL's DataTypes](https://www.postgresql.org/docs/9.4/static/datatype.html)

## Select where
```sql
SELECT name FROM animals 
WHERE species != 'gorillas' and name != 'Max'
```

[**(not X) and (not Y) == not(X or Y)**](http://en.wikipedia.org/wiki/De_Morgan%27s_laws)

## List tables in this database in this lesson
```sql
create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);
```

## The Onething SQL Suck
In each database, it has its own ways to show tables in database, columns in table. It's suck!

## New keyword
- offset: position of the row to take query
- limit: limitation of number of rows

## Select clauses
1. xx_x_
2. ___x_
3. x___x 

- `limit count`: return the first count rows if the result table
- `limit count offset skip`: return count rows starting after the first skip rows
- `group by columns`: change the behavior of aggregations such as max, count, sum. With group by, the aggregation will return one row for each distinct value in columns

How many of each species we have?
```sql
```

## Insert

```sql
INSERT INTO Table(col1, col2) VALUE (value1, value2)
```

## After aggregating
**The value of `count(*) as num` comes from `count` and `group by`. But where always run before aggregation**

So, if we make query like below then it's wrong:
```sql
select name, count(*) as num from animals
group by species
where num == 1
```

Solution: using 'having'
```sql
select name, count(*) as num from animals
group by species
having num == 1
```

```sql
select name, food, count(*) as num from animals join diet on animals.species == diet.species
group by food
having num=1;
```

## Install virtual machine
- Install virtual box
- Install vagrant
- Download VM configuration 
https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip
- Unzip and `vagrant up`
- Login vagrant `vagrant ssh`
- Install conda








