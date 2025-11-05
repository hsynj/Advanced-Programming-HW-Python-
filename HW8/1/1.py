import sqlite3

conn = sqlite3.connect('1.db')
print("-> Opened database successfully")
cursor = conn.cursor()

# Create tables
try:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        DEPARTMENT_ID INT NOT NULL,
        SALARY REAL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DEPARTMENTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        LOCATION TEXT NOT NULL
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PROJECTS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        BUDGET REAL NOT NULL,
        DEPARTMENT_ID INT NOT NULL
    )''')
    # For Ex.2 audit_log
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_log (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ACTION TEXT NOT NULL,
        TABLE_NAME TEXT NOT NULL,
        RECORD_ID INT NOT NULL,
        TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS log_employee_deletion
    AFTER DELETE ON EMPLOYEES
    BEGIN
        INSERT INTO audit_log (ACTION, TABLE_NAME, RECORD_ID)
        VALUES ('DELETE', 'EMPLOYEES', OLD.ID);
    END;
    ''')
except sqlite3.Error as e:
    print(f"Error creating tables: {e}")
else:
    print("-> Tables created successfully")
finally:
    conn.commit()
    conn.close()
