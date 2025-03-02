# src/main.py
from ingredient_manager import add_ingredient, view_ingredients, search_ingredient, remove_ingredient, list_unique_ingredients, check_expiry

def main():
    while True:
        print("\n📌 Food Ingredient Tracker")
        print("1️⃣ Add Ingredient")
        print("2️⃣ View Ingredients")
        print("3️⃣ Search Ingredient")
        print("4️⃣ Remove Ingredient")
        print("5️⃣ List Unique Ingredients")
        print("6️⃣ Check Expiry")
        print("7️⃣ Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            add_ingredient(name, quantity, purchase_date, expiry_date)

        elif choice == "2":
            ingredients = view_ingredients()
            for ing in ingredients:
                print(f"📌 {ing[1]} - {ing[2]} units (Purchased: {ing[3]}, Expires: {ing[4]})")

        elif choice == "3":
            name = input("Enter ingredient name to search: ")
            result = search_ingredient(name)
            if result:
                print(f"✅ Found: {result}")
            else:
                print("❌ Ingredient not found!")

        elif choice == "4":
            name = input("Enter ingredient name to remove: ")
            remove_ingredient(name)

        elif choice == "5":
            unique_items = list_unique_ingredients()
            print("📌 Unique Ingredients:", unique_items)

        elif choice == "6":
            check_expiry()

        elif choice == "7":
            print("🚀 Exiting program!")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
