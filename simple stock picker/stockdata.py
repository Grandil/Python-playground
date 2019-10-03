# Import yfinance
import yfinance as yf  
 
interval = "1m"
priceAtOpenIndex = 0
priceToCompareIndex = 1
priceAtSellpointIndex = 15
 
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('AAPL','2019-09-05','2019-09-06', interval=interval)
print(data.Close[priceAtOpenIndex])
print(data.Close[priceToCompareIndex])
print(data.Close[priceAtSellpointIndex])
 
if data.Close[priceToCompareIndex]>data.Close[priceAtOpenIndex]:
    print("Price had risen at compare point.")
if data.Close[priceToCompareIndex]>data.Close[priceAtOpenIndex] and data.Close[priceAtSellpointIndex]>data.Close[1]:
    profitPerStock = data.Close[priceAtSellpointIndex]-data.Close[priceToCompareIndex]
    print("Trade was profitable with " + str(profitPerStock) + " profit pr. stock")
else:
    print("Trade was not profitable.")
# Plot the close prices
#import matplotlib.pyplot as plt
#data.Close.plot()
#plt.show()