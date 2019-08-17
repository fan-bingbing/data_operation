import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# t = ('RHAT',) # use turple in python variable for security
# c.execute('SELECT * FROM stocks1 WHERE symbol=?', t)
# print(c.fetchone())

# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-03-28', 'BUY', 'IBM', 1000, 72.00),
#              ('2006-03-28', 'BUY', 'IBM', 1000, 53.00),
#             ]
# c.executemany('INSERT INTO stocks1 VALUES (?,?,?,?,?)', purchases)
# conn.commit()



for row in c.execute('SELECT * FROM stocks1 ORDER BY price'):
    print(row)
