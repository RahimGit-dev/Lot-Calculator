# Rahim Abdulmalik
# Lot Calculator using Risk and Pips

class TradingCalc:
    '''
    the first method "man_input" requires the user to insert a risk amount
    in dollars and the pip count from entry to stop loss. These 2 variables
    must be called when using this method.
    '''
    def man_input(self,risk,pips):
        lot = 0.1 / (pips/risk)  #The actual conversion equation
        if lot < 0.008:  #used to determine if risk is too low
            return 'Risk amount is too low'
        lot = round(lot,2)
        return f'Your lot size should be roughly {lot}\n'

    '''
    the second method creates an endless loop in the terminal which asks the
    user for the risk amount and pip count (similar to the first method), then
    prints out the proper lot size to be traded. In order to exit the loop, simply
    type "exit".
    '''
    def loop_input(self):
        while True:
            try:
                risk = input('Enter risk amount (in dollars): ')
                if risk == 'exit': break
                risk = float(risk)
                pips = input('Enter pips to stop loss value: ')
                if pips == 'exit': break
                pips = float(pips)

                lot = 0.1 / (pips/risk)
                if lot < 0.008:
                    print('==================================')
                    print('Risk amount is too low')
                    print('==================================\n')
                    continue
                lot = round(lot,2)
                print('==================================')
                print(f'Your lot size should be roughly {lot}')
                print('==================================\n')
            except:
                print('Numeric values only\n')
                continue


trade = TradingCalc() #creating the object
# uncomment the entire method that is desired to be used

# Method 1:
# Insert your risk and pips amount to be used in for the
# following variables, then print the statement.
# 100 and 70 are there by default

dollar_amount = 100
pips_sl = 70
print(trade.man_input(dollar_amount,pips_sl))

# # ====================================================

# # Method 2:
# # Print the following function to start the loop in a
# # terminal. In order to exit the loop, type the word exit
#
# print(trade.loop_input())



