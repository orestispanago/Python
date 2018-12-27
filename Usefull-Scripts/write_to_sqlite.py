import sqlite3


temp = '156.2'
sizes = ['temp', 'hum','ws','max_ws','precip','press','press_asl']
values = ['11.5','62','2','5','0','1013','1015']

conn = sqlite3.connect('values.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS random_values(dt DATETIME DEFAULT CURRENT_TIMESTAMP, 
                                                 {} TEXT, {} TEXT, 
                                                 {} TEXT, {} TEXT, 
                                                 {} TEXT, {} TEXT, 
                                                 {} TEXT)'''.format(*sizes))

c.execute('''INSERT INTO r_values VALUES(CURRENT_TIMESTAMP, 
                                       {}, {}, {}, 
                                       {}, {}, {}, {})'''.format(*values))
conn.commit()
conn.close()
