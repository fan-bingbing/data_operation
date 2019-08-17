import visa
import sqlite3

class SpecAn(object):

    def __init__(self, address, dbfile):
        self.rm = visa.ResourceManager()
        self.SP = self.rm.open_resource(address) # Spec An
        self.conn = sqlite3.connect(dbfile)

    def FEP_Setup(self, freq):
        self.conn.execute('''update FEP set content = ? where parameter = ? ''',
                         (freq, Centre_frequency)
                         )
        self.conn.commit()

        list = [row[0] for row in self.conn.execute("select content from FEP")]

        self.SP.write(f"*RST") # write all paramaters to SpecAn
        self.SP.write("SYST:DISP:UPD ON")
        self.SP.write(f"FREQ:CENT {list[0]}MHz")
        self.SP.write(f"FREQ:SPAN {list[1]}Hz")
        self.SP.write(f"BAND {list[2]}Hz")
        self.SP.write(f"BAND:VID {list[3]}Hz")
        self.SP.write(f"DISP:TRAC:Y:RLEV:OFFS {list[4]}")
        self.SP.write(f"DISP:TRAC:Y:RLEV {list[5]}")
        self.SP.write(f"INP:ATT {list[6]}")
        self.SP.write(f"{list[7]}")
        self.SP.write(f"{list[8]}")
        self.SP.write(f"CORR:TRAN:SEL '{list[9]}'")
        self.SP.write(f"CORR:TRAN {list[10]} ")
        self.SP.write(f"CORR:TRAN:SEL '{list[11]}'")
        self.SP.write(f"CORR:TRAN {list[12]}")
        self.SP.write(f"CORR:TRAN:SEL '{list[13]}'")
        self.SP.write(f"CORR:TRAN {list[14]}")
        self.SP.write(f"CALC:LIM:NAME '{list[15]}'")
        self.SP.write(f"CALC:LIM:UPP:STAT {list[16]}")
        self.SP.write(f"CALC:LIM:NAME '{list[17]}'")
        self.SP.write(f"CALC:LIM:UPP:STAT {list[18]}")
        self.SP.write(f"SWE:POIN {list[19]}")
