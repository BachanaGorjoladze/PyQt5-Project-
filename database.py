import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise


def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email VARCHAR(75) NOT NULL UNIQUE, 
                username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY,
                password VARCHAR(75) NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                username VARCHAR(50) NOT NULL,
                question_number INTEGER NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                FOREIGN KEY (username) REFERENCES users (username),
                UNIQUE(username, question_number),
                UNIQUE(username, question)
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        raise


if __name__ == "__main__":
    connection = create_connection("users.db")
    create_tables(connection)
    connection.close()
