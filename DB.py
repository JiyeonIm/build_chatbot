import sqlite3

def connect_db(data):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    table_name = "chatbot_log"

    cursor.execute(f'''
            SELECT COUNT(*)
              FROM sqlite_master
             WHERE type = 'table'
               AND name = '{table_name}'
        ''')
    
    table_exist = cursor.fetchone()[0]

    if not table_exist:
        print("iloveyou")
        cursor.execute(f'''
            CREATE TABLE '{table_name}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT,
                latency TEXT
            )
        ''')

    # 필요한 데이터 추출 및 변수에 저장
    question = data['question']
    answer = data['answer']
    latency = data['latency']

    # 데이터 삽입
    cursor.execute(f"INSERT INTO '{table_name}' (question, answer, latency) VALUES (?, ?, ?)", (question, answer, latency))

    # 변경 사항 저장
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_db("There are 9 planets.")