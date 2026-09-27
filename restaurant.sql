CREATE DATABASE restaurant;

USE restaurant;

CREATE TABLE menu (
    item_no INT PRIMARY KEY,
    item_name VARCHAR(50),
    price INT
);

INSERT INTO menu VALUES
(1, 'Burger', 120),
(2, 'Pizza', 250),
(3, 'French Fries', 100),
(4, 'Pasta', 180),
(5, 'Sandwich', 100),
(6, 'Coke', 60),
(7, 'Milkshake', 120);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50),
    item_name VARCHAR(50),
    quantity INT,
    price INT,
    total INT
);
