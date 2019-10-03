# Import yfinance
import yfinance as yf  
 
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('AAPL','2019-10-02','2019-10-03', interval="5m")
print(data.Close[0])
print(data.Close[1])
print(data.Close[30])
 
 
if data.Close[1]>data.Close[0] and data.Close[30]>data.Close[1]:
    profitPerStock = data.Close[30]-data.Close[1]
    print("Trade was profitable with " + str(profitPerStock) + "profit pr. stock")
else:
    print("Trade was not profitable.")
# Plot the close prices
#import matplotlib.pyplot as plt
#data.Close.plot()
#plt.show()