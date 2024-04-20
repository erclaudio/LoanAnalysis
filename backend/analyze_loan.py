import datetime as dt
from dateutils import month_start, relativedelta
import matplotlib.pyplot as plt
import numpy_financial as npf 
import pandas as pd 

class Loan:

    def __init__(self, rate, term, loan_amount, start = dt.date.today().isoformat()):
         self.rate = rate/1200
         self.periods = term *12
         self.loan_amount = loan_amount
         self.start = month_start(dt.date.fromisoformat(start)) + dt.timedelta(31)
         self.pmt = npf.pmt(self.rate, self.periods, -self.loan_amount)
         self.pmt_str = f"{self.pmt:,.2f}"
         self.table = self.loan_table()

    def loan_table(self):
         periods = [self.start + relativedelta(months=x) for x in range(self.periods)]
         interest = [npf.ipmt(self.rate, month, self.periods, -self.loan_amount)
                     for month in range(1, self.periods+1)]
         principal = [npf.ppmt(self.rate, month, self.periods, -self.loan_amount)
                     for month in range(1, self.periods+1)]
         table = pd.DataFrame({'Payment' : self.pmt, 
                               'Interest': interest, 
                               'Principal': principal}, index = pd.to_datetime(periods))
         table['Balance'] = self.loan_amount - table['Principal'].cumsum()
         return table.round(2)
         
    def plot_balances(self):
         amort = self.table
         plt.plot(amort.Balance, label ='Balance')
         plt.plot(amort.Interest.cumsum(), label = 'Interest')
         plt.grid(axis = 'y', alpha = .5)
         plt.legend(loc = 8)
         plt.show()
        
         
    
    def summary(self):
         amort = self.table
         print('Summary')
         print('-' * 30)
         print(f'Payment: {self.pmt_str:>21}')
         print(f'{"Payoff Date:":19} {amort.index.date[-1]}')
         print(f'Total Interest:{amort.Interest.cumsum()[-1]:15,.2f}')
         print(f'{"New Term:":19}{self.extra_pmt(100)} years')
         print('-'*30)
    
    def extra_pmt(self, extra_amt):
         return round(npf.nper(self.rate, self.pmt + extra_amt, -self.loan_amount).round(2)/12,2)
    
    def preferred_term(self, requested_term):         
         added_pmt = 10
         while npf.nper(self.rate, self.pmt + added_pmt, -self.loan_amount)/12 > requested_term:
              added_pmt+=1
        
         new_loan = Loan(5.875, requested_term, self.loan_amount)
         new_loan.plot_balances()
         amort = new_loan.table
                 
         return (f'{"Original Amount:":22} {self.pmt:.2f}\n'
            f'{"New Payment:":22} {added_pmt+self.pmt:.2f}\n'
            f'{"Additional Cost:":22} {added_pmt:.2f}\n'
            f'{"New Term:":22}{requested_term} years\n'
            f'{"New Total Interest:":22}{amort.Interest.cumsum().iloc[-1]:.2f}'
            )
    
         
loan = Loan(5.875, 30, 360000)
#print(loan.table)
#loan.plot_balances()
#loan.summary()
#print(loan.preferred_term(10))