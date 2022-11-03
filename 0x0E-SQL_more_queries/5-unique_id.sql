-- Script that creats the table unique_id on my SQL server.
CREATE TABLE IF NOT EXISTS  unique_id (id INT DEFAULT VALUE 1 UNIQUE, name VARCHAR(256) NOT NULL);
