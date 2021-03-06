import sqlite3
import random
import time

def main():
    n = 1440
    
    conn = sqlite3.connect(":memory:")

    conn.execute("CREATE TABLE a (row INTEGER, col INTEGER, val REAL);")
    conn.execute("CREATE TABLE b (row INTEGER, col INTEGER, val REAL);")

    with conn:
        for i in range(n):
            for j in range(n):
                conn.execute("INSERT INTO a (row, col, val) VALUES (?, ?, ?)", (i, j, random.random()))
                conn.execute("INSERT INTO b (row, col, val) VALUES (?, ?, ?)", (i, j, random.random()))
    
    start = time.time()
    conn.execute("SELECT b.row, a.col, SUM(a.val*b.val) FROM a INNER JOIN b on a.row = b.col GROUP BY a.col, b.row ;")
    end = time.time()
    print(f"took {end-start}s")

if __name__ == "__main__":
    main()