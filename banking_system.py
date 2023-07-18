'''
                BY: Felipe Campelo
                DATE: july 18, 2023

                CODE: Single user banking script.
'''
def print_error(msg):
    ''' prints error message in red '''
    print("\033[91m", msg, "\033[0m", sep="\n")
def deposit(amount):
    '''deposits a non negative amount to the balance'''

    global balance, deposits

    # cannot deposit negative amounts
    if amount < 0:
        print("Deposits cannot be negative.")
    else:
        balance += amount
        deposits.append(amount) # appends to deposits[]
def withdraw(amount):
    ''' withdraws an amount lesser than 500 to an maximun of 3 in a single run '''

    global balance, withdrawals


    # cannot withdraw from an empty account
    if balance == 0:
        print_error("Cannot withdraw from an empty account.")

    # cannot exceed 3/day
    elif len(withdrawals) >= MAX_WITHDRAWALS:
        print_error(f"Cannot exceed {MAX_WITHDRAWALS} withdrawals per day.")

    # cannot allow negative withdrawals
    elif amount < 0: 
        print_error("Withdrawals cannot be negative.")
    
    # cannot exceed withdrawal limit
    elif amount > WITHDRAWAL_LIMIT:
        print_error(f"Cannot withdraw amounts bigger than {WITHDRAWAL_LIMIT}.")

    # cannot allow negative balance
    elif amount > balance: 
        print_error("Cannot withdraw more than the current balance. Which is $ {balance:.2f}")
    
    else: 
        balance -= amount
        withdrawals.append(amount) # appends to withrawals[] 
def statement():
    """
    Print a statement of the client's account balance, deposits, and withdrawals.

    Args:
        balance (float): The client's account balance.
        deposits (list): A list of the client's deposits.
        withdrawals (list): A list of the client's withdrawals.

    Returns:
        str: A string containing the statement.
    """

    global balance, deposits, withdrawals

    header = f"""
        \033[32m. === CLIENT === .\033[0m
        Balance: $ {balance:.2f}    Deposits: {len(deposits)}   Withdrawals: {len(withdrawals)}
    """
    deposits_str = "\n".join([f"$ {deposit:.2f}" for deposit in deposits])
    withdrawals_str = "\n".join([f"$ {withdrawal:.2f}" for withdrawal in withdrawals])
    return f""" {header} 
    DEPOSITS:
{deposits_str}
    WITHDRAWALS:
{withdrawals_str}"""

#           === SCRIPT ===

MENU = '''
        \033[34m. == WELCOME TO PY BANK == .\033[0m

[1] Deposit     [2] Withdraw    [3] Statement

[0] Exit

>>> '''
MAX_WITHDRAWALS = 3
WITHDRAWAL_LIMIT = 500

balance = 0
deposits, withdrawals = [], []

# menu loop
option = 1
while option != 0:

    option = int(input(MENU))

    if option == 1:
        amount = int(input("Which amount do you want to deposit? $ "))
        deposit(amount)
    elif option == 2:
        amount = int(input("Which amount do you want to withdraw? $ "))
        withdraw(amount)
    elif option == 3:
        print(statement())
    elif option == 0:
        print("Until next time!")
    else:
        print("\033[91m", "\t\tInvalid option!", "\033[0m", sep="\n")
