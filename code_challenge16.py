
b_accounts = {}

while True:
    print("Welcome to our bank, choose a number to proceed:")
    print("\n1. Create Bank Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter account name: ")
        if name in b_accounts:
            print("Account already exists.")
        else:
            deposit = float(input("Enter initial deposit: "))
            b_accounts[name] = deposit
            print(f"Account created for {name} with balance: {deposit}")
    
    elif choice == '2':
        name = input("Enter account name: ")
        if name in b_accounts:
            deposit = float(input("Enter deposit amount: "))
            b_accounts[name] += deposit
            print(f"Deposited {deposit}. Current balance: {b_accounts[name]}")
            balance = b_accounts[name]
            print("Denomination breakdown:")
            for d in [1000, 500, 200, 100, 50, 20, 10, 5, 1]:
                if balance >= d:
                    print(f"{d} PHP: {int(balance // d)}")
                    balance %= d
        else:
            print("Account does not exist.")
    
    elif choice == '3':
        name = input("Enter account name: ")
        if name in b_accounts:
            withdraw = float(input("Enter withdrawal amount: "))
            if withdraw > b_accounts[name]:
                print("Insufficient balance!")
            else:
                b_accounts[name] -= withdraw
                print(f"Withdrew {withdraw}. Current balance: {b_accounts[name]}")
                balance = b_accounts[name]
                print("Denomination breakdown:")
                for d in [1000, 500, 200, 100, 50, 20, 10, 5, 1]:
                    if balance >= d:
                        print(f"{d} PHP: {int(balance // d)}")
                        balance %= d
        else:
            print("Account does not exist.")
    
    elif choice == '4':
        name = input("Enter account name: ")
        if name in b_accounts:
            print(f"Current balance for {name}: {b_accounts[name]}")
        else:
            print("Account does not exist.")
    
    elif choice == '5':
        print("Thank you for choosing our bank, goodbye")
        print("PROGRAM TERMINATED")
        break
    
    else:
        print("Invalid option. Please try again.")
