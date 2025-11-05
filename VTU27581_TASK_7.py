balance=0

def deposit (amount):

global balance

balance + = amount

print(f" ${amount}deposited successfully.")

def withdraw Comount):

global balance

if amount <= balance:

balance-=amount

print(f"${amount} withdraw successfully. ")

else:

print("Insufficient balance!")

def display():

print (f" Available balance: $(balance}")

while True:

print("\n 1. Deposit \n 2. withdraw \n 3. Display Balance \n Exit")

Choice=int (input("Enter your choice:"))

if choice = = 1:

amt=float (input("Enter amount to deposit: "))

deposit (amt)

elit choice==2:

amt=float(input("Enter amount to withdrow:"))

withdraw(amt)

elit choice==3:

display()

elif choice==4:

print("Thank you for using our banking system")

break

else:

print("Invalid choice.")
