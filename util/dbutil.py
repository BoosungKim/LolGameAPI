import psycopg2

# Create Table

conn = psycopg2.connect("dbname=lol user=postgres")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, key integer, title serial);")

conn.commit()

cur.close()
conn.close()

