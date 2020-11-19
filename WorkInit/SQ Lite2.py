import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()

cur.execute("""SELECT *, users.fname, users.lname FROM orders 
LEFT JOIN users ON users.userid = orders.userid;""")
print(cur.fetchall())

cur.execute("SELECT * FROM users; ")
one_result = cur.fetchmany(3)



print(one_result)


