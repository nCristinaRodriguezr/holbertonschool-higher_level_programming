-- a script that prints the following description of the
-- table first_table from the database hbtn_0c_0 in your MySQL server.
SET @db_name := DATABASE();

SET @desc_table_query = CONCAT('
    SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = ''', @db_name, ''' AND TABLE_NAME = ''first_table'';'
);
PREPARE stmt FROM @desc_table_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
