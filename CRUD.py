import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")  

db = client["sample_db"]

collection = db["sample_collection"]

def add_data(data):
    collection.insert_one(data)
    print("Data added successfully.")

def delete_data(query):
    result = collection.delete_many(query)
    print(f"{result.deleted_count} documents deleted.")

def update_data(query, new_data):
    result = collection.update_one(query, {"$set": new_data})
    if result.modified_count > 0:
        print("Data updated successfully.")
    else:
        print("No matching document found for update.")

def display_data():
    # Retrieve and display all documents in the collection
    for doc in collection.find():
        print(doc)

while True:
    print("\nDatabase Navigation Operations:")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. Update Data")
    print("4. Display Data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = {
            "name": input("Enter name: "),
            "age": int(input("Enter age: "))
        }
        add_data(data)

    elif choice == "2":
        key = input("Enter the key to delete by (e.g., name or age): ")
        value = input(f"Enter the {key} to delete: ")

        query = {}
        if key == "age":
            query[key] = int(value)  # Convert to integer for age
        else:
            query[key] = value

        delete_data(query)

    elif choice == "3":
        key = input("Enter the key to update by (e.g., name or age): ")
        value = input(f"Enter the {key} to update: ")
        new_value = input(f"Enter the new {key}: ")

        query = {}
        if key == "age":
            query[key] = int(value)  # Convert to integer for age
        else:
            query[key] = value

        new_data = {key: int(new_value) if key == "age" else new_value}  # Convert to integer for age

        update_data(query, new_data)

    elif choice == "4":
        display_data()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

# Close the database connection
client.close()