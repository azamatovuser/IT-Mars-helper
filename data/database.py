import sqlite3


class Database:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_table()

    def setup_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions_answers (
            id INTEGER PRIMARY KEY,
            student_id TEXT NOT NULL,
            question TEXT NOT NULL,
            tutor_id TEXT,
            answer TEXT
        )
        ''')
        self.conn.commit()

    def insert_question(self, student_id, question):
        self.cursor.execute('''
        INSERT INTO questions_answers (student_id, question) VALUES (?, ?)
        ''', (student_id, question))
        self.conn.commit()

    def update_answer_by_id(self, id, tutor_id, answer):
        self.cursor.execute('''
        UPDATE questions_answers SET tutor_id=?, answer=? WHERE id=?
        ''', (tutor_id, answer, id))
        self.conn.commit()


    def get_all_entries(self):
        self.cursor.execute('''
        SELECT * FROM questions_answers
        ''')
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()