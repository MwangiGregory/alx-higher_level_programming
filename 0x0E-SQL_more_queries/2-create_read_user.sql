-- Creates the database hbtn_0d_2 and the user user_0d_2
-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';