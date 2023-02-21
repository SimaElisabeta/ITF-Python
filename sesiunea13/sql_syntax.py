"""
SQL (Structured Query Language) is the standard language used for managing and manipulating relational databases.
It allows users to insert, update, delete and retrieve data stored in a db.


1) CREATE - used to create a new table

    * CREATE TABLE table_name (
        column1 datatype1,
        column2 datatype2
        ...
    );

2) SELECT - used to retrieve data from db

    * SELECT column1, column2, ... FROM table_name;

3) INSERT - used to insert new data into a table

    * INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

4) UPDATE - used to modify existing data in a table

    * UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition (some_column = some_value);

5) DELETE - used to delete data from a table

    * DELETE FROM table_name
    WHERE condition (some_column = some_value);

"""