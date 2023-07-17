'''
                BY: Felipe Campelo
                DATE: july 17, 2023

                CODE: Single user banking script.
'''

def deposit(amount, deposits):
    '''deposits a non negative amount to the balance'''

    global balance

    # cannot deposit negative amounts
    if amount < 0:
        print("Deposits cannot be negative.")
    else:
        balance += amount
        deposits.append(amount) # appends to deposits[]
def withdraw(amount, withdrawals):
    ''' withdraws an amount lesser than 500 to an maximun of 3 in a single run '''

    global balance

    # cannot exceed 3/day
    if len(withdrawals) >= MAX_WITHDRAWALS:
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
        withdrawals.append(amount) # appends to withrawals[] 
def statement(deposits, withdrawals):
    """
    Print a statement of the client's account balance, deposits, and withdrawals.

    Args:
        balance (float): The client's account balance.
        deposits (list): A list of the client's deposits.
        withdrawals (list): A list of the client's withdrawals.

    Returns:
        str: A string containing the statement.
    """

    global balance

    header = f"""
        \033[32m. === CLIENT === .\033[0m
        Balance: $ {balance:.2f}    Deposits: {len(deposits)}   Withdrawals: {len(withdrawals)}
    """
    deposits = "\n".join([f"$ {deposit:.2f}" for deposit in deposits])
    withdrawals = "\n".join([f"$ {withdrawal:.2f}" for withdrawal in withdrawals])
    return f""" {header} 
    DEPOSITS:
{deposits}
    WITHDRAWALS:
{withdrawals}"""

#           === SCRIPT ===

MENU = '''
        \033[34m. == WELCOME TO PY BANK == .\033[0m

[1] Deposit     [2] Withdraw    [3] Statement

[0] Exit

>>> '''
MAX_WITHDRAWALS = 3
HIGHEST_WITHDRAWAL = 500

balance = 0
deposits, withdrawals = [], []

# menu loop
option = 1
while option != 0:

    option = int(input(MENU))

    if option == 1:
        amount = int(input("Which amount do you want to deposit? $ "))
        deposit(amount, deposits)
    elif option == 2:
        amount = int(input("Which amount do you want to withdraw? $ "))
        withdraw(amount, withdrawals)
    elif option == 3:
        print(statement(deposits, withdrawals))
    elif option == 0:
        print("Until next time!")
    else:
        print("\033[91m", "\t\tInvalid option!", "\033[0m", sep="\n")



