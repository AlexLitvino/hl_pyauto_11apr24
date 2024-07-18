# Creating Database:
sqlite3 trades.db
.databases
.tables

# Prettify output
Enable headers in output
.headers ON
Align columns
.mode columns
Clear console
.shell cls

# Data types:
    NULL
    INTEGER
    REAL
    TEXT
    BLOB

https://www.sqlitetutorial.net/sqlite-date/    Date&Time
Time and date should be handled as TEXT
YYYY-MM-DD HH:MM:SS.SSS
SELECT datetime('now');
SELECT datetime('now','localtime');


# Creating table:
CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
	column_1 data_type PRIMARY KEY,
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	table_constraints
) [WITHOUT ROWID];

Column constraints:
PRIMARY KEY, UNIQUE, NOT NULL, CHECK

Table constraints:
PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK

CREATE TABLE Vendors(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);

# Constraints

# Primary key
A primary key is a column or group of columns used to identify the uniqueness of rows in a table. 
Each table has one and only one primary key.

CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
	column_1 data_type PRIMARY KEY,
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	table_constraints
) [WITHOUT ROWID];



CREATE TABLE table_name(
   column_1 INTEGER NOT NULL PRIMARY KEY,
   ...
);

CREATE TABLE table_name(
   column_1 INTEGER NOT NULL,
   column_2 INTEGER NOT NULL,
   ...
   PRIMARY KEY(column_1,column_2,...)
);

In SQL standard, the primary key column must not contain NULL values.
It means that the primary key column has an implicit NOT NULL constraint.


## AUTOMINCREMENT
to prevent re-use of used ids

## NOT NULL

## UNIQUE
SQLite treats all NULL values are different, therefore, a column with a UNIQUE constraint can have multiple NULL values.

## CHECK
SQLite CHECK constraints allow you to define expressions to test values whenever they are inserted into or updated within a column.

The following statement shows how to define a CHECK constraint at the column level:
```
    CREATE TABLE table_name(
        ...,
        column_name data_type CHECK(expression),
        ...
    );
```

and the following statement illustrates how to define a CHECK constraint at the table level:
```
    CREATE TABLE table_name(
        ...,
        CHECK(expression)
    );
```

# ALTER TABLE
ALTER TABLE statement to change the structure of an existing table.
By using an SQLite ALTER TABLE statement, you can perform two actions:
- Rename a table.
- Add a new column to a table.
- Rename a column (added supported in version 3.20.0)


## Using SQLite ALTER TABLE to rename a table
```
ALTER TABLE existing_table
RENAME TO new_table;
```

## Using SQLite ALTER TABLE to add a new column to a table
```
ALTER TABLE table_name
ADD COLUMN column_definition;
```

## Using SQLite ALTER TABLE to rename a column
```
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
```

ALTER TABLE NewData RENAME COLUMN index2 TO index3;

## How to delete column
https://www.sqlitetutorial.net/sqlite-alter-table/


## DROP TABLE
```
DROP TABLE [IF EXISTS] [schema_name.]table_name;
```

## Insert data into table
Inserting one line
```
INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);
```

Multiple lines
```
INSERT INTO table1 (column1,column2 ,..)
VALUES 
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);
```
Inserting default values
```
INSERT INTO artists DEFAULT VALUES;
```

It is possible insert data to table using SELECT from another table

When you create a table that has an INTEGER PRIMARY KEY column, this column is the alias of the rowid column.


# SELECT
```
SELECT DISTINCT column_list
FROM table_list
  JOIN table ON join_condition
WHERE row_filter
ORDER BY column
LIMIT count OFFSET offset
GROUP BY column
HAVING group_filter;
```

# SELECT - ORDER BY
```
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,
    column_2 DESC;
```

# SELECT - LIMIT
```
SELECT
	column_list
FROM
	table
LIMIT row_count;
```

```
SELECT
	column_list
FROM
	table
LIMIT row_count OFFSET offset;
```

The same result with other syntax:
```
SELECT
	column_list
FROM
	table
LIMIT offset, row_count;
```


# SELECT - WHERE
```
SELECT
	column_list
FROM
	table
WHERE
	search_condition;
```

WHERE column_1 = 100;
WHERE column_2 IN (1,2,3);
WHERE column_3 LIKE 'An%';
WHERE column_4 BETWEEN 10 AND 20;

SQLite comparison operators:
=, <> or !=, <, >, <=, >=
IS NULL and IS NOT NULL

SQLite logical operators
Operator	Meaning
ALL	returns 1 if all expressions are 1.
AND	returns 1 if both expressions are 1, and 0 if one of the expressions is 0.
ANY	returns 1 if any one of a set of comparisons is 1.
BETWEEN	returns 1 if a value is within a range.
EXISTS	returns 1 if a subquery contains any rows.
IN	returns 1 if a value is in a list of values.
LIKE	returns 1 if a value matches a pattern
NOT	reverses the value of other operators such as NOT EXISTS, NOT IN, NOT BETWEEN, etc.
OR	returns true if either expression is 1


LIKE
SQLite wildcart symbols:
1. The percent sign % wildcard matches any sequence of zero or more characters.
2. The underscore _ wildcard matches any single character.
```
SELECT
	column_list
FROM
	table_name
WHERE
	column_1 LIKE pattern;
```
Note that SQLite LIKE operator is case-insensitive. It means "A" LIKE "a" is true.

`PRAGMA case_sensitive_like = true;`

SQLite LIKE with ESCAPE clause

`column_1 LIKE pattern ESCAPE expression;`

`column_1 LIKE '%10\%%' ESCAPE '\';`
  
# Agregate functions
AGREGATE_FUNCTION([ALL | DISTINCT] expression);  
- AVG
- COUNT
- MAX
- MIN
- SUM


# GROUP BY
The GROUP BY clause a selected group of rows into summary rows by values of one or more columns.  
The GROUP BY clause returns one row for each group. For each group, you can apply an aggregate function such as MIN, MAX, SUM, COUNT, or AVG
```
SELECT 
    column_1,
    aggregate_function(column_2) 
FROM 
    table
GROUP BY 
    column_1,
    column_2;
```

# HAVING
Having has sense to use with agregate function
```
SELECT
	column_1, 
        column_2,
	aggregate_function (column_3)
FROM
	table
GROUP BY
	column_1,
        column_2
HAVING
	search_condition;
```

# Subquery
Subquery could return one or several values. Several values could be used in 'IN'
You can use a subquery in the SELECT, FROM, WHERE, and JOIN clauses.
```
SELECT column_1
FROM table_1
WHERE column_1 = (
   SELECT column_1 
   FROM table_2
);
```

# UNION/EXCEPT/INTERSECT
UNION - A & B
EXCEPT - A - B
INTERSECT - A ^ B
The following are rules to union data:
- The number of columns in all queries must be the same.
- The corresponding columns must have compatible data types.
- The column names of the first query determine the column names of the combined result set.
- The GROUP BY and HAVING clauses are applied to each individual query, not the final result set.
- The ORDER BY clause is applied to the combined result set, not within the individual result set.
```
query_1
UNION [ALL]
query_2
UNION [ALL]
query_3
...;
```

# JOINS
SQLite directly supports INNER JOIN, LEFT JOIN, or CROSS JOIN
Note that SQLite doesn’t directly support the RIGHT JOIN and FULL OUTER JOIN.

## INNER JOIN
Combines all rows from the first and the second table where condition is met.
```
SELECT 
    Title,
    Name
FROM 
    albums
INNER JOIN artists 
    ON artists.ArtistId = albums.ArtistId;
```

SELECT Vendors.name, Vendors.deal, Customers.deal, Customers.name FROM Vendors INNER JOIN Customers on Vendors.deal=Customers.deal;


## LEFT JOIN
Combines all rows from the first and the second table where condition is met.
Adds all rows from the first table  with adding NULL to the data of the second table. 
```
SELECT
    Name, 
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
ORDER BY Name;
```

SELECT Vendors.name, Vendors.deal, Customers.deal, Customers.name FROM Vendors LEFT JOIN Customers on Vendors.deal=Customers.deal;


## CROSS JOIN
The CROSS JOIN clause creates a Cartesian product of rows from the joined tables.
```
SELECT
    select_list
FROM table1
CROSS JOIN table2;
```
Select * from Vendors Cross Join Customers;


## SQLite Self-Join
Use alias for table to perform join of table with itself 
Select * from Vendors v INNER JOIN Vendors v2 ON v.deal=v2.deal;

## SQLite FULL OUTER JOIN Emulation
https://www.sqlitetutorial.net/sqlite-full-outer-join/


# Updating data in table
```
UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition 
ORDER BY column_or_expression
LIMIT row_count OFFSET offset;
```

# Deleting data
```
DELETE FROM table
WHERE search_condition;
```

```
DELETE FROM table
WHERE search_condition
ORDER BY criteria
LIMIT row_count OFFSET offset;
```

Delete all rows:  
`DELETE FROM table;`



# Foreign keys
PRAGMA foreign_keys;
The command returns an integer value: 1: enable, 0: disabled. 
If the command returns nothing, it means that your SQLite version doesn’t support foreign key constraints

To disable foreign key constraint:
PRAGMA foreign_keys = OFF;

To enable foreign key constraint:
PRAGMA foreign_keys = ON;

What it is?
Problem if we have some data reference in other table and will delete we will have some orphan reference. 
We need them to update synchroniously.

Example:
CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER NOT NULL,
    FOREIGN KEY (group_id)
       REFERENCES supplier_groups (group_id) 
);

CREATE TABLE supplier_groups (
	group_id integer PRIMARY KEY,
	group_name text NOT NULL
);


#### SQLite foreign key constraint actions

FOREIGN KEY (foreign_key_columns)
   REFERENCES parent_table(parent_key_columns)
      ON UPDATE action 
      ON DELETE action;

SQLite supports the following actions:
    SET NULL
    SET DEFAULT
    RESTRICT
    NO ACTION
    CASCADE


