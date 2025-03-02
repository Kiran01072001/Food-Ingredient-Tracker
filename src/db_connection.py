# src/db_connection.py

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kiraN@321",
        database="FoodTracker"
    )
