import psycopg2.extras
from psycopg2 import connect
import pandas as pd

conn = connect("postgres://postgres:qwerty@localhost:5432/postgres")

cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

cur.execute("SELECT * from hotels")
res = cur.fetchall()

df = pd.DataFrame(res)
del df["id"]
df.to_csv("hotels.csv", sep=";", index=False)

cur.execute("SELECT * from rooms")
res = cur.fetchall()

df = pd.DataFrame(res)
del df["id"]
df.to_csv("rooms.csv", sep=";", index=False)

cur.execute("SELECT * from bookings")
res = cur.fetchall()

df = pd.DataFrame(res)
del df["id"]
del df["total_cost"]
del df["total_days"]
df.to_csv("bookings.csv", sep=";", index=False)
