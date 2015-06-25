import sqlite3
from yahoo_finance import Share
f = open('tick.txt','r')
con=sqlite3.connect('stocks.db')
c = con.cursor()



##historical data using yahoo
# sh = ['FB', 'INTC']
sh = f.readlines()

for tick in sh:
	print(tick)
	equity = Share(tick)
	equity.refresh()
	lst = equity.get_historical('2000-04-25', '2015-09-29')
	for x in lst:
		print(type(x))
		close = x.get('Adj_Close')
		date = x.get('Date')
		hi = x.get('High')
		lo = x.get('Low')
		tck = x.get('Symbol')
		vol = x.get('Vol')
		opn = x.get('Open')
		c.execute("INSERT INTO price VALUES (?,?,?,?,?,?);",(tck,date,opn,hi,lo,close))

con.commit()
con.close()
##real time data using google
