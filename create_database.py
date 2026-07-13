
import sqlite3

conn = sqlite3.connect("database/company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    designation TEXT,
    manager TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leave_policy (
    leave_type TEXT,
    days_allowed INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS holidays (
    holiday_date TEXT,
    holiday_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS office_info (
    office_location TEXT,
    working_hours TEXT,
    work_mode TEXT
)
""")

cursor.executemany(
    "INSERT INTO employees VALUES (?,?,?,?,?,?)",
    [
        (101, "John Smith", "Engineering", "Software Engineer", "Alice Johnson", "john@company.com"),
        (102, "Emma Davis", "HR", "HR Executive", "Michael Brown", "emma@company.com"),
        (103, "David Wilson", "Finance", "Financial Analyst", "Sarah Lee", "david@company.com"),
    ]
)

cursor.executemany(
    "INSERT INTO leave_policy VALUES (?,?)",
    [
        ("Casual Leave", 12),
        ("Sick Leave", 10),
        ("Earned Leave", 18),
        ("Maternity Leave", 180),
        ("Paternity Leave", 15)
    ]
)

cursor.executemany(
    "INSERT INTO holidays VALUES (?,?)",
    [
        ("2026-01-26", "Republic Day"),
        ("2026-08-15", "Independence Day"),
        ("2026-10-02", "Gandhi Jayanti"),
        ("2026-12-25", "Christmas")
    ]
)

cursor.execute(
    "INSERT INTO office_info VALUES (?,?,?)",
    (
        "Bangalore",
        "9:00 AM - 6:00 PM",
        "Hybrid"
    )
)

conn.commit()

conn.close()

print("Database created successfully.")
