-- Establecer el nombre de la base de datos como una variable de usuario
SET @db_name := DATABASE();

-- Construir la consulta para crear la tabla si no existe
SET @create_table_query = CONCAT('CREATE TABLE IF NOT EXISTS ', @db_name, '.first_table (id INT, name VARCHAR(256));');

-- Ejecutar la consulta
PREPARE stmt FROM @create_table_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;