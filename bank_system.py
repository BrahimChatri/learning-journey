"""
    I make this to practice classes in python 
    Just a simple bank system using classes and func 
    And store user data in json file 
"""


import json
import os
import time

# class to handle all bank Features
class Bank:
    def __init__(self, name: str) -> None:
        self.name = name
        self.data_file = "info.json"
        self.user_data = self.load_user_data()
        if self.name not in self.user_data:
            self.user_data[self.name] = {"balance": 0}
            self.save_user_data()

    def deposit(self, amount: int) -> None:
        self.user_data[self.name]["balance"] += amount
        self.save_user_data()
        print(f"{self.name} successfully deposited ${amount} to their account.")

    def withdraw(self, amount: int) -> None:
        if self.user_data[self.name]["balance"] >= amount:
            self.user_data[self.name]["balance"] -= amount
            self.save_user_data()
            print(f"{self.name} successfully withdraw ${amount} from their account.")
        else:
            print(f"Insufficient funds to withdraw ${amount}. Current balance is ${self.user_data[self.name]['balance']}.")
    
    def check_balance(self) -> None:
        balance = self.user_data[self.name]["balance"]
        print(f"Your current balance is ${balance}.")

    #save user data from json file 
    def save_user_data(self) -> None:
        with open(self.data_file, 'w') as f:
            json.dump(self.user_data, f, indent=4)

    #load user data from json file 
    def load_user_data(self) -> dict:
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

#function to print slow 
def print_slow(*, text: str, delay=0.04)-> None:
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


def main() -> None:
    print_slow(text="Hello Welcome to the bank \nplease enter ur name: ")
    user = input().strip()
    while True:
        user_account = Bank(f"{user}")
        print_slow(text="1- Deposit \n2- Check balance \n3- Withdraw \n4- Exit \n Enter ur choise: ",delay=0.03)
        user_choise = int(input())

        if user_choise == 1 :
            print_slow(text="Enter amount to deposit: ",delay=0.03)
            user_input = float(input())
            user_account.deposit(user_input)
            time.sleep(1)

        elif user_choise == 2:
            user_account.check_balance()
            time.sleep(1)


        elif user_choise == 3:
            print_slow(text="Enter amount to withdraw: ", delay=0.03)
            withdraw_amouth = float(input())
            user_account.withdraw(withdraw_amouth)
            time.sleep(1)

        elif user_choise == 4:
            exit()

if __name__ == "__main__":
    main()