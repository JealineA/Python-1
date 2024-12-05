
Currency_USD = float(input('Enter USD currency amount: '))

#Fixed Exchange Rate
Euro_Exchange_Rate = 1.05
MXN_Exchange_Rate = 20.32

#calculate exchange rate
Currency_Euro = Currency_USD * Euro_Exchange_Rate
Currency_MXN = Currency_USD * MXN_Exchange_Rate

print('Exchange Amount is: $', Currency_Euro, "Eur" )
print('Exchange Amount is: $', Currency_MXN, "MXN" )