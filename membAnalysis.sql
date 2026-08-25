create DATABASE membAnalysis;

USE membAnalysis;
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    email VARCHAR(255),
    member_since DATE,
    membership_status VARCHAR(20),
    membership_level VARCHAR(20)
);