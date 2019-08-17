import sqlite3
conn = sqlite3.connect('SpecAn.db')

FEPs = [('Centre_frequency', '459.075', 'MHz'),
       ('Span_frequency', '300', 'Hz'),
       ('RBW', '10', 'Hz'),
       ('VBW', '30', 'Hz'),
       ('RF_level', '50', 'None'),
       ('Attenuation', '35', 'None'),
       ('RefLev_offset', '30.3', 'None'),
       ('Trace_peak', 'DET POS', 'None'),
       ('Transducer1', 'HSA029914302', 'None'),
       ('Trans1_ON?', 'ON', 'None'),
       ('Transducer2', 'PE7388-30-30DB', 'None'),
       ('Trans2_ON?', 'OFF', 'None'),
       ('Transducer3', 'NHP-700', 'None'),
       ('Trans3_ON?', 'OFF', 'None'),
       ('Limit_line_1', 'ASNZS4365_CONSPUR_TX', 'None'),
       ('Limit_line_1_ON?', 'OFF', 'None'),
       ('Limit_line_2', 'ASNZS4295_CONSPUR_TX', 'None'),
       ('Limit_line_2_ON?', 'OFF', 'None'),
       ('Sweep_points', '10001', 'None'),
      ]

conn.execute("create table FEP(parameter, content, unit)")


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
