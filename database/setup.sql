CREATE DATABASE IF NOT EXISTS FoodTracker;
USE FoodTracker;

CREATE TABLE IF NOT EXISTS Ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    quantity VARCHAR(225),
    purchase_date DATE,
    expiry_date DATE
);
