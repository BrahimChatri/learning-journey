# user_authentication.py

"""
This project is part of my Python learning journey and features a simple user authentication 
system. It includes user registration and login functionalities. The program ensures unique usernames 
and provides clear user prompts. This project showcases file handling, data persistence, and input validation skills. 
Sharing it on GitHub highlights my progress in applying core programming concepts.
"""
# pip install json
import os
import time
import json

# Print slow text 
def print_slow(text: str, delay=0.03)-> None:
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Save user data
def save_user_data(name: str, user_info: dict)-> None:
    existing_user_data = load_user_data()
    existing_user_data[name] = user_info

    with open('user_info.json', 'w') as f:
        json.dump(existing_user_data, f, indent=4)

# Load user data
def load_user_data()-> dict:
    if os.path.exists('user_info.json'):
        with open('user_info.json', 'r') as f:
            return json.load(f)
    return {}

# Check if name exists
def name_exists(name: str)->bool:
    user_data = load_user_data()
    return name in user_data

def register_user():
    while True:
        name = input("Enter your name: ").strip()
        if name_exists(name):
            print("Name already exists. Please enter another one!")
            continue
        username = input("Enter your username: ").strip()
        email = input("Enter your email (to recover your account if password is forgotten): ").strip()
        password = input("Enter your password: ").strip()
        confirm_password = input("Confirm your password: ").strip()
        while confirm_password != password:
            confirm_password = input("Passwords do not match. Please confirm your password: ").strip()
        
        user_data = {
            "Username": username,
            "Email": email,
            "Password": password  # Store as plain text
        }
        save_user_data(name, user_data)
        print("Your account has been created successfully!")
        break

def login():
    user_data = load_user_data()
    name = input("Enter your name: ").strip()
    if not name_exists(name):
        print("Name does not exist. Please register first.")
        return
    user_name = input("Enter your Username: ")
    stored_username = user_data[name]["Username"]
    if user_name != stored_username :
        print("username is not correct for name you entered !")
        return
    
    password = input("Enter your password: ").strip()

    stored_password = user_data[name]["Password"]
    
    if password == stored_password:
        print("Login successful!")
    else:
        print("Incorrect password.")

def main():
    while True:
        print_slow("Hello and welcome to our program!!\n1- Login\n2- Register\n3- Exit.\n")
        try:
            user_input = int(input("Please enter your choice: ").strip())
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue

        if user_input == 1:
            login()
        elif user_input == 2:
            register_user()
        elif user_input == 3:
            exit()
        else:
            print("Please enter a valid number (1, 2, or 3).")

if __name__ == "__main__":
    main()
