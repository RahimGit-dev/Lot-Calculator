# Rahim Abdulmalik
# Lot Calculator using Risk and Pips
# Python 3.7.4

'''
the second method creates an endless loop in the terminal which asks the
user for the risk amount and pip count (similar to the first method), then
prints out the proper lot size to be traded. In order to exit the loop, simply
type "exit".
'''

def loop_input():
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

def main():
    print(loop_input())

if __name__ == "__main__":
    main()
