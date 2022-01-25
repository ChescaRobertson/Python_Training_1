accounts = {
    1234: {
        "number": 1234,
        "name": "Smith",
        "balance": 500.0
    },
    2345: {
        "number": 2345,
        "name": "Jones", 
        "balance": -150.0
    },
    3456: {
        "number": 3456, 
        "name": "Wilson", 
        "balance": 2000.0
    },
    4567: {
        "number": 4567,
        "name": "Thompson", 
        "balance": 275.0
    },
    5678: {
        "number": 5678,
        "name": "Davis",
        "balance": 100.0
    }
}

while True:
    acc_num = int(input("Please enter an account number: "))
    #acc = accounts[acc_num]
    acc = accounts.get(acc_num)
    if acc:
        print(f"Name: {acc['name']}, Balance: {acc['balance']}")
    else:
        print('Account not found')
        
    more = input("Type 'y' to continue searching or 'n' to stop: ")
    if more == 'n':
        print("Program terminating, thank you")
        break