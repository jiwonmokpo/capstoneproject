import cx_Oracle

conn = cx_Oracle.connect("c##capstone", "0000", "192.168.0.16/system", encoding="UTF-8") #db 연결
cursor = conn.cursor()

in_data1 = "Userid test" #테스트 값 1
in_data2 = "Password test" #테스트 값 2
cursor.execute("INSERT INTO MEMBER(userid, userpassword) VALUES(:1, :2)", [in_data1, in_data2])
#Member 테이블의 userid, userpassword에 in_data값을 1번 2번 자리에 넣음.
conn.commit() #commit

#값이 제대로 들어갔는지 조회하는 구문
cursor.execute("SELECT * FROM MEMBER")
out_data = cursor.fetchone()
print("=====>", out_data[0:2])

conn.close() #DB종료
