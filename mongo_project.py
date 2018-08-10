import pymongo #Imports the Pymongo Library
import os

MONGODB_URI=os.getenv("MONGO_URI")
DBS_NAME="mytestdb"
COLLECTION_NAME="myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo DB. %s") % e
        
def show_menu():
    print("")
    print("1. Add record: ")
    print("2. Find record by Name: ")
    print("3. Edit a record: ")
    print("4. Delete a record: ")
    print("5. Exit ")
    
    option = input("Enter Option: ")
    return option
    
def get_record():
    print(" ")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database. ")
        
    if not doc:
        print(" ")
        print("Error, no results found! ")
        
    return doc

def add_record():
    print(" ")
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    dob = input("Enter DOB: ")
    gender = input("Enter gender: ")
    hair_colour = input("Enter hair colour: ")
    occupation = input("Enter occupation: ")
    nationality = input("Enter nationality: ")
    
    new_doc = {"fist": first.lower(), "last": last.lower(), "dob": dob.lower(), "gender": gender.lower(), "hair_colour": hair_colour.lower(), "occupation": occupation.lower(), "nationality": nationality.lower()} 
    
    try:
        coll.insert(new_doc)
        print(" ")
        print("Document inserted. ")
    except:
        print("Error accessing the database. ")
    
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2.")
        elif option == "3":
            print("You have selected option 3.")
        elif option == "4":
            print("You have selected option 4.")
        elif option == "5":
            print("You have selected option 5.")
            conn.close()
            break
        else: 
            print("Invalid option.")
            print("")
            
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop() 