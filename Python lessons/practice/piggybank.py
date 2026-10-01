balance = 100000000
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
        print(f"Your balance is: ${balance}")
    else:
        print("Invalid option.")