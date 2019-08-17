import sqlite3
conn = sqlite3.connect('SpecAn.db')

FEPs = [('Centre_frequency', '459.075', 'MHz'),
       ('Span_frequency', '300', 'Hz'),
       ('RBW', '10', 'Hz'),
       ('VBW', '30', 'Hz'),
      ]


# conn.execute("create table FEP(parameter, content, unit)")
conn.executemany("insert into FEP(parameter, content, unit) values (?,?,?)", FEPs)
for row in conn.execute("select parameter, content, unit from FEP"):
    print(row)
conn.commit()
conn.close()

# c = conn.cursor()
#
# c.execute(''' CREATE TABLE stocks1(
# date text, trans text, symbol text, qty real, price real
# ) ''')
#
# c.execute("INSERT INTO stocks1 VALUES('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")
#
# conn.commit()
#
# conn.close()
