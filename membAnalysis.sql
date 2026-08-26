CREATE DATABASE IF NOT exists membAnalysis ;
USE membAnalysis;
SET SQL_SAFE_UPDATES = 1;
CREATE TABLE IF NOT exists membTiers (
	tier_id INT PRIMARY KEY auto_increment,
    tier_name VARCHAR(50),
    monthly_price DECIMAL(10,2) NOT NULL,
    content_access boolean,
    discount_access boolean,
    app_access boolean,
    helper_access boolean
    
);


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

SELECT * FROM members