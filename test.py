# 데이터베이스에 접속해서 데이터 처리하는 테스트 코드

import mysql.connector

from mysql_connection import get_connection

# 변수 저장
name = "순두부"
description = "순두부찌개 만드는법"
cook_time = 45
directions = "물넣고 두부넣고 조개넣고 끓인다"

try :
    # 데이터 insert
    # 1. DB에 연결
    connection = get_connection()

    # 2. 쿼리문 만들기
    query = '''insert into recipe
            (name, description, cook_time, directions)
            values
            (%s, %s, %s, %s);'''

    # %s에 맞게 튜플로 작성한다.
    record = (name, description, cook_time, directions)
    
    # 3. 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서를 이용해서 실행한다.
    cursor.execute(query, record)

    # 5. 커넥션을 커밋해줘야 한다. -> DB에 영구적으로 반영하라는 뜻
    connection.commit()

    # 6. 자원 해제
    cursor.close()
    connection.close()

# 예외처리
except mysql.connector.Error as e :
    print(e)
    cursor.close()
    connection.close()