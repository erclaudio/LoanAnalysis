from backend.analyze_loan import Loan
import sys
from time import sleep

def display_menu():
    print("""
    MENU
    --------------------
    1. Start a new loan
    2. Show Payment
    3. Show Amortization table
    4. Show Loan Summary
    5. Plot Balances
    6. Change Loan duration
    7. Change monthly payment
    8. Exit
    """)



def pmt():
    pass

def amort():
    pass

def summary():
    pass

def plot():
    pass

def pay_faster():
    pass

def pay_early():
    pass

action = {'2' : pmt, '3' : amort, '4' : summary, '5' : plot, '6' : pay_faster, '7' : pay_early}


def main():
    while True:
        display_menu()
        choice = input("Enter your selection: ")
        if choice == '1':
            rate = float(input("Enter Interest Rate: "))
            term = int(input("Enter term: "))
            pv = float(input("Enter Amount: "))
            loan = Loan(rate,term,pv)
            print("Loan Initialised")
            sleep(1)

        elif choice == '8':
            print("Goodbye!")



#if __name__=="__main__":
#    main()  