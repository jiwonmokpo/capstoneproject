import cx_Oracle

conn = cx_Oracle.connect("c##capstone", "0000", "192.168.0.16/system", encoding="UTF-8")
cursor = conn.cursor()

in_data = "Hello World"
cursor.execute("INSERT INTO MEMBER(USERID) values(:1)", [in_data])
conn.commit()

cursor.execute("SELECT USERID FROM MEMBER")
out_data = cursor.fetchone()
print("=====>", out_data[0])

conn.close()
