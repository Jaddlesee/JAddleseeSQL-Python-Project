CREATE DATABASE IF NOT exists membAnalysis ;
USE membAnalysis;

CREATE TABLE IF NOT exists members (
    member_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100) ,
    age INT NOT NULL,
    email VARCHAR(255),
    member_since DATE,
    membership_status VARCHAR(20),
    membership_level VARCHAR(20)
);
SELECT COUNT(*) FROM members;