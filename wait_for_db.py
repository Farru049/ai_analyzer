import time
import psycopg2
import os

DATABASE_URL = os.environ["DATABASE_URL"]  # ← Railway injects this automatically

print(f"Connecting to: {DATABASE_URL}")
print("Waiting for database...")

retries = 0
while retries < 30:
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        print("Database ready!")
        break
    except psycopg2.OperationalError as e:
        print(f"Not ready yet: {e}")
        retries += 1
        time.sleep(2)
else:
    print("Could not connect after 30 retries. Exiting.")
    exit(1)