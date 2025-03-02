                   Food Ingredient Tracker

# Description

The Food Ingredient Tracker is a simple inventory management system designed to help users track food ingredients, their quantities, purchase dates, and expiry dates. This project is useful for households, restaurants, and food businesses to ensure proper food management, avoid wastage, and maintain freshness.

🚀 Features

✅ Add Ingredients – Add new ingredients with quantity, purchase date, and expiry date.

✅ View Ingredients – Display all stored ingredients.

✅ Search Ingredients – Look up ingredients by name.

✅ Remove Ingredients – Delete ingredients from the inventory.

✅ List Unique Ingredients – View distinct ingredient names in stock.

✅ Check Expiry – Identify expired and soon-to-expire ingredients.

🛠️ Tech Stack

Python (Backend Logic)

MySQL (Database)

MySQL Connector (Database Connection)

# Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/yourusername/food-ingredient-tracker.git  
cd food-ingredient-tracker

2️⃣ Install Dependencies

pip install mysql-connector-python

3️⃣ Set Up MySQL Database

Run the following SQL commands in MySQL:

CREATE DATABASE IF NOT EXISTS FoodTracker;
USE FoodTracker;

CREATE TABLE IF NOT EXISTS Ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    quantity VARCHAR(225),
    purchase_date DATE,
    expiry_date DATE
);

4️⃣ Configure Database Connection

Modify src/db_connection.py with your MySQL credentials:

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="FoodTracker"
    )


🙌 Contributing

Want to contribute? Feel free to fork the repository and submit a pull request!
