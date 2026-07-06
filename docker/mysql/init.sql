-- TaskFlow DB Initialization Script
-- Run this manually on your local MySQL: mysql -u root < docker/mysql/init.sql

CREATE DATABASE IF NOT EXISTS taskflow_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
