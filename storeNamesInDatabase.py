#!/usr/bin/python
import psycopg2
import sys
con = None
con = psycopg2.connect(database='camuto-dev',user='dhamodaran')
cur = con.cursor()
cur.execute('SELECT * FROM stores')
cur.fetchall()
cur.execute("INSERT INTO images (id, name) VALUES (%s,%s);", (1, "test"))
con.commit()
con.close()
