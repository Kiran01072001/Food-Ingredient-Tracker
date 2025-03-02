# src/ingredient_manager.py
from db_connection import connect_db
from datetime import datetime

conn = connect_db()
cursor = conn.cursor()

def add_ingredient(name: str, quantity: int, purchase_date: str, expiry_date: str):
    query = "INSERT INTO Ingredients (name, quantity, purchase_date, expiry_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, quantity, purchase_date, expiry_date))
    conn.commit()
    print(f"Added {name} ({quantity} units, expires on {expiry_date})")

def view_ingredients():
    cursor.execute("SELECT * FROM Ingredients")
    return cursor.fetchall()

def check_expiry():
    today = datetime.today().date()
    cursor.execute("SELECT name, purchase_date, expiry_date FROM Ingredients")
    ingredients = cursor.fetchall()
    for ing in ingredients:
        name, purchase_date, expiry_date = ing
        expiry_date = datetime.strptime(str(expiry_date), '%Y-%m-%d').date()
        purchase_date = datetime.strptime(str(purchase_date), '%Y-%m-%d').date()
        days_left = (expiry_date - today).days
        if expiry_date < today:
            print(f"❌ {name} has expired! (Expired on: {expiry_date})")
        else:
            print(f"✅ {name} is still good for {days_left} days.")

def search_ingredient(name: str):
    cursor.execute("SELECT * FROM Ingredients WHERE name = %s", (name,))
    return cursor.fetchall()

def remove_ingredient(name: str):
    cursor.execute("DELETE FROM Ingredients WHERE name = %s", (name,))
    conn.commit()
    print(f"Removed {name} from inventory.")

def list_unique_ingredients():
    cursor.execute("SELECT DISTINCT name FROM Ingredients")
    return [item[0] for item in cursor.fetchall()]