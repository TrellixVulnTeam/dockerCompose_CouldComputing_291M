CREATE DATABASE IF NOT EXISTS rabbitmqdata;
USE rabbitmqdata;
CREATE TABLE IF NOT EXISTS message ( id INT AUTO_INCREMENT, message VARCHAR(30), PRIMARY KEY (id));

