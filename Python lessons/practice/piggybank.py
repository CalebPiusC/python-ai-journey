balance = 1000

running = True

print('''
Hello Caleb!
Welcome to PiggyBank ATM

----MENU----
''')

while running:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        running = False
    elif choice == "1":
        print(f"Balance: #{balance}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        # Deposit: reject fake money
        if amount <= 0:
            print("Amount must be positive!")
        else:
            balance += amount
            print(f"Deposit successful. Balance: #{balance}")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        # Withdraw: needs BOTH conditions true at once
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Balance: #{balance}")
        else:
            print("Insufficient funds.")
    elif choice == "4":
        print("Transfer coming soon! 🚧")
    else:
        print("Invalid option.")