import pymysql

def getStaff():
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = 'yuting1101'
    db = 'TESTDB'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor()

    # 好習慣: 寫出所有欄位名稱，即便要選取全部欄位 => 避免增加其他人閱讀code的成本
    sql = """
    SELECT ID, Name, DeptId, Age, Gender, Salary FROM Staff; 
    """
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

if __name__ == '__main__':
    for r in getStaff():
        print(r)