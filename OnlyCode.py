import random
from time import sleep

balance = random.randint(0,17002)
balance = balance - balance % 5
print(f"Your Balance Is: {balance}")

while True:
    try:
        amount = float(input("Please Enter The Amount You Want To Withdraw: "))
        if amount <= 0:
            print("Please Enter A Positive Number")
        elif amount > balance:
            print("Insufficient Balance.")
        else:
            balance -= amount
            print("Processing Your Transmission Please Wait")
            sleep(3)
            print(f"Withdrawal Completed,Your New Balance Is {balance}")
            break
    except ValueError:
        print("Please Enter A Valid Amount")
