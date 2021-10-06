usersCREATE DATABASE login;

USE login;

CREATE TABLE users(
	id INT PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(250) NOT NULL
);

ALTER TABLE `login`.`users` 
ADD COLUMN `created_at` DATETIME NULL DEFAULT NOW() AFTER `password`,
ADD COLUMN `updated_at` DATETIME NULL DEFAULT NOW() AFTER `created_at`;

CREATE TABLE recipes(
	id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(250) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    updated_at DATETIME NOT NULL DEFAULT NOW(),
    user_id INT ,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

