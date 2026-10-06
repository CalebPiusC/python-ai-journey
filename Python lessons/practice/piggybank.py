balance = 1000

running = True

print('''
Hello Caleb!
Welcome to PiggyBank ATM
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
        balance += amount
        print(f"Deposit successful. Balance: #{balance}")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Balance: #{balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid option.")