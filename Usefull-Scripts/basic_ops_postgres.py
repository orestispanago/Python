import psycopg2

HOST = "YourServerIP"
DBNAME = "YourDatabaseName"
USER="YourUsername"
PASS= "YourPassword"

# Example
# HOST = "150.140.158.150"
# DBNAME = "udemy"
# USER="orestis"
# PASS= "Valemestivasi$#"
def create_table():
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,)) # the , is necessary!
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price,item))
    conn.commit()
    conn.close()

# create_table()
# insert("Beer can",100,1.20)
# delete("Beer bottle")
# update(20,14,"Wine bottle")

print(view())
