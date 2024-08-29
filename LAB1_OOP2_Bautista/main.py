import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456,account_firstname = "Jhon",account_lastname = "Bautista",current_balance = 5000,address = "New York Quezon City", email = "jhbautista@gmail.com")

print("Account 1")


Account1.Account_check()


user1_serialnumber = 12345
ATM1 = ATM.ATM(user1_serialnumber,500,"deposit")
ATM1.deposit(Account1)
ATM1.check_currentbalance(Account1)
ATM1.check_serialnumber()
ATM1.view_transactionsummary()

print('\n')
print("Account 2")

Account2 = Accounts.Accounts(account_number=789123, account_firstname = "Joshua",account_lastname = "Santos",current_balance = 2000,address = "Aurora Blvd Quezon City",email = "josantos@yahoo.com")

Account2.Account_check()

user2_serialnumber = 67891
ATM2 = ATM.ATM(user2_serialnumber,300,"deposit")
ATM2.deposit(Account2)
ATM2.check_currentbalance(Account2)
ATM2.check_serialnumber()
ATM2.view_transactionsummary()

