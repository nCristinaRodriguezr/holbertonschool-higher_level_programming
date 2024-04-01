-- Establecer el nombre de la base de datos como una variable de usuario
SET @db_name := DATABASE();

-- Construir la consulta para listar las tablas
SET @query = CONCAT('SELECT table_name AS `Tables_in_', @db_name, '` FROM information_schema.tables WHERE table_schema = "', @db_name, '"');

-- Ejecutar la consulta
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
