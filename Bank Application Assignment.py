print('Welcome to Temitope Bank ATM')
restart=('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('Welcome!\n  ')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 To Check Balance: \n')
            print('Please Press 2 To Withdraw: \n')
            print('Please Press 3 To Deposit: \n')
            print('Please Press 4 To Exit: \n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is £',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \n 10, 20, 40, 60, 80, 100: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('\nSuccessful withdrawal! Your Balance is now £',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount: '))    

            elif option == 3:
                deposit = float(input('How Much Would You Like To Pay In? '))
                balance = balance + deposit
                print ('\nSuccessful deposit! Your Balance is now £',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for banking with us.ii')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nYour card has been blocked')
            break