# Deeper in SQL

## What we will learn?
- Define new tables, and declare relationship between them
- Table structure
- Tricks SQL in python code to run code faster and more reliably

## Concepts

#### Normalized Design
> Normalized database means the relationship between tables match the relationship among the data

> Database normalization or simply normalization, is the process of restructuring a relational database with some rules called `norm forms` to reduce `data redundancy`, and improve `data integrety` - [wiki](https://en.wikipedia.org/wiki/Database_normalization)

**Properties of normalized design**
- Every row has the same number of columns
- There is a unique key (maybe one or more than one column), and everything in a row says something about the key
- Facts that don't relate to the key belong in different tables.
- Tables shouldn't imply relationships that don't exist. 
    - The example here was the job_skills table, where a single row listed one of a person's technology skills (like 'Linux') and one of their language skills (like 'French'). This made it look like their Linux knowledge was specific to French, or vice versa ... when that isn't the case in the real world. Normalizing this involved splitting the tech skills and job skills into separate tables.

**Document**
- [Normal Forms](http://www.bkent.net/Doc/simple5.htm)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)

#### Create table and types
- Create table
```
create table tablename (
    column1 type [constraints],
    column2 type [constraints],
    ...
    [row constraints]
);
```
- Datatype
    - In each database system, there are types exists in this one but not in other.
    - Some system supports abbreviations for long type name in SQL standard type name
    - [?] Where is the SQL official page? I mean standard query, standard data types
    
- Create database and tables should be in the initial setup, not in the app code.
![alt text](https://imgur.com/a/074KN)

    

