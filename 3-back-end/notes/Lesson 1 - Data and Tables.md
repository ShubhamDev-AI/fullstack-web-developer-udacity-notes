# Data and table

- Join
- Uniqueness and keys

**Every result from sql queries are table**

## Joins
```sql
select animals.name, animals.species, diet.food
       from animals join diet
       on animals.species = diet.species;
```