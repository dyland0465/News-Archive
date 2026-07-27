from datetime import datetime
import mysql.connector
from mysql.connector import Error
from src.config import DB_CONFIG


def init_db():
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute("""

                CREATE TABLE IF NOT EXISTS headlines(
                id INT AUTO_INCREMENT PRIMARY KEY,
                fetch_date DATE NOT NULL,
                headline VARCHAR(500) NOT NULL,
                url_link VARCHAR(1000) NOT NULL,
                UNIQUE KEY unique_story(fetch_date, headline(255))
                )
        """)
        connection.commit()

    except Error as e:
        print(f"[DB Error] Initialization failed: {e}")
        raise e
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def SaveToDB(articles):
    if not articles:
        print("[DB INFO] No headlines provided for database insertion.")
        return
    connection = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        today_str = datetime.now().strftime("%Y-%m-%d")

        insert_query = """
                INSERT IGNORE INTO headlines (fetch_date, headline, url_link)
                VALUES (%s, %s, %s)
            """

        records_to_insert = []
        for article in articles:
            title = article.get("title")
            link = article.get("url")
            if title and link and "[Removed]" not in title:
                records_to_insert.append((today_str, title, link))

        cursor.executemany(insert_query, records_to_insert)
        connection.commit()

        print(f"Processed {cursor.rowcount} new headlines successfully")

    except Error as e:
        print(f"Error: Insertion failed: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
