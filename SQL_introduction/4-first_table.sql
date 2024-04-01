-- a script that creates a table called first_table in the current database in your MySQL server.
USE DATABASE();
CREATE TABLE IF NOT EXISTS DATABASE_NAME.first_table (
    ID INT,
    NAME VACHAR(256),
);
