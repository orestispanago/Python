import psycopg2
import pandas as pd


HOST="150.140.158.150"
DBNAME="orestis"
USER="orestis"
PASS="Valemestivasi$#"



def view():
    conn = psycopg2.connect(host=HOST,database=DBNAME, user=USER, password=PASS)
#    cur = conn.cursor()
    df = pd.read_sql_query(
        "SELECT * FROM testing3 where time between '2019-01-14' and '2019-01-31'",
        con=psycopg2.connect(host=HOST, database=DBNAME, user=USER,
                             password=PASS),parse_dates=True,index_col='time')

    conn.close()
    return df
df1=view()

df1.index = df1.index.round('min')
df1 = df1.resample('min').mean()