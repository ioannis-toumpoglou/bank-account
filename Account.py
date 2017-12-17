class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
            
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

account = Account('balance.txt')

while True:
    print('Current balance: '+str(account.balance)+'€')
    choice = input('Please press [1] to deposit, [2] to withdraw or [q] to quit: ')

    try:
        if choice != 'q':
            if int(choice) == 1:
                account.deposit(int(input('Please enter the amount you wish to deposit: ')))
                print('\nNew balance: '+str(account.balance)+'€')
                account.commit()
                print('\nThank you! Have a nice day!\n')
                break
                
            elif int(choice) == 2:
                amount = (int(input('Please enter the amount you wish to withdraw: ')))
                if account.balance < amount:
                    print('\nSorry! The amount you entered exceeds the available amount..\n')  
                else:
                    account.withdraw(amount)
                    print('\nNew balance: '+str(account.balance)+'€')
                    account.commit()
                    print('\nThank you! Have a nice day!\n')
                    break
            else:
                print('\nThis is not a valid choice. Please try again...\n')
        else:
            print('\nThank you! Have a nice day!\n')
            break
    except:
        print('\nThis is not a valid choice. Please try again...\n')
        continue
