'''
BY: Felipe Campelo
DATE: july 3, 2023

CODE: Single user banking script.
'''

# deposits a non negative amount to the balance
def deposit(amount):

    global balance

    # cannot deposit negative amounts
    if amount < 0:
        print("Deposits cannot be negative.")
    else:
        balance += amount
        transactions["Deposits"].append(amount) # appends to deposits[]

# withdraws an amount lesser than 500 to an maximun of 3 in a single run
def withdraw(amount):

    global balance

    # cannot exceed 3/day
    if len(transactions["Withdrawals"]) >= MAX_WITHDRAWALS:
        print("You cannot exceed the 3 withdrawals/day! Come back soon.")

    # cannot allow negative withdrawals
    elif amount < 0: 
        print("Cannot withdraw negative amounts.")
    
    # cannot exceed highest withdrawal
    elif amount > HIGHEST_WITHDRAWAL:
        print("Withdrawals cannot exceed $ 500.00")

    # cannot allow negative balance
    elif amount > balance: 
        print(f"Cannout withdraw amounts bigger than your balance, which is $ {balance:.2f}")
    
    else: 
        balance -= amount
        transactions["Withdrawals"].append(amount) # appends to withrawals[]

# displays the balances, the number and a list of each transaction type 
def statement():
    print(f'''
        CLIENT
        Balance: $ {balance:.2f}    Deposits: {len(transactions["Deposits"])}   Withdrawals: {len(transactions["Withdrawals"])}
 
        DEPOSITS:''', 
        "\n$ ".join([f"{deposit:.2f}" for deposit in transactions["Deposits"]]),
        '\n\tWITHDRAWALS:',
        "\n$ ".join([f"{withdrawal:.2f}" for withdrawal in transactions["Withdrawals"]]),
        sep="\n", end='\n')
    
# SCRIPT

menu_message = '''
[1] Deposit     [2] Withdraw    [3] Statement

[0] Exit
'''

balance = 0
transactions = {"Deposits":[], "Withdrawals":[]}
MAX_WITHDRAWALS = 3
HIGHEST_WITHDRAWAL = 500

# menu loop
option = 1
while option != 0:

    # MENU
    option = int(input(menu_message))

    if option == 1:
        amount = int(input("Which amount do you want to deposit: "))
        deposit(amount)
    if option == 2:
        amount = int(input("Which amount do you want to withdraw: "))
        withdraw(amount)
    if option == 3:
        statement()
