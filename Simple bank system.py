# This is the simple bank system

print("\n ==============================================================")
print("                           BANKING SYSTEM                      ")
print(" ==============================================================\n")
print("1. Create an account")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Check balance")
print("5. Exit")
print(" ==============================================================\n")

def create_account():
    print("Enter your name: ")
    name = input()
    print("Enter your account number: ")
    account_number = input()
    print("Enter your balance: ")
    balance = float(input())
    return {"name": name, "account_number": account_number, "balance": balance}

def deposit_money():
    print("Enter your account number: ")
    account_number = input()
    print("Enter the amount to deposit: ")
    amount = float(input())
    return {"account_number": account_number, "amount": amount}

def withdraw_money():
    print("Enter your account number: ")
    account_number = input()
    print("Enter the amount to withdraw: ")
    amount = float(input())
    return {"account_number": account_number, "amount": amount}

def check_balance():
    print("Enter your account number: ")
    account_number = input()
    return {"account_number": account_number}

def exit():
    print("Thank you for using our banking system")
    exit()

def main():
    while True:
        print("Enter your choice: ")
        choice = int(input())
        if choice == 1:
            account = create_account()
            print(account)
        elif choice == 2:
            deposit = deposit_money()
            print(deposit)
        elif choice == 3:
            withdraw = withdraw_money()
            print(withdraw)
        elif choice == 4:
            balance = check_balance()
            print(balance)
        elif choice == 5:
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
