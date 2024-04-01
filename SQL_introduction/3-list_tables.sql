-- a script that lists all the tables of a database in your MySQL server.
SELECT table_name AS 'Tables_in_mysql'
FROM information_schema.tables
WHERE table_schema = DATABASE();
