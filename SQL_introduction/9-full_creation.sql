-- script that creates a table and adds multiple rows --
CREATE TABLE IF NOT EXISTS second_table (id int, name VARCHAR(256), score int);
INSERT INTO second_table (id, name) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name) VALUES (4, 'George', 8);
