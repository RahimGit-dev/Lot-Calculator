# Lot Calculator
'''
For my fellow traders out there that use Metatrader as a platform and potentially trade Forex.
I have created a calculator that determines what your lot size should be based on how much you are willing to lose,
and the amount of pips from entry in which you would exit a trade.

For example, lets say you wanted to sell USD/JPY at 107.20 and you determine that your stop loss will be at 108.20.
You also decide that you are not willing to lose more than $200 per trade. From entry to stop loss is 100 pips,
so with the calculator your inputs would be 200 for the risk amount and 100 for the amount of pips,
giving you the lot size that you should trade with.

I have created 2 simple methods under the TradingCalc class in Python, in order to execute this program.
One of the methods can be continuously ran by opening the ".py" python file in a command line.
To exit the program type "exit" for one of the inputs.
The 2nd method can be used in an IDE/text editor by adjusting the risk and pips amount accordingly. Enjoy!
'''

