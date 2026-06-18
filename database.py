import sqlite3

DB_PATH = "attendance.db"


# ==========================
# DATABASE CONNECTION
# ==========================

def get_connection():

    return sqlite3.connect(DB_PATH)


# ==========================
# CREATE TABLES
# ==========================

def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Users Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Students Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        class_name TEXT,
        email TEXT
    )
    """)

    # Attendance Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id)
        REFERENCES students(id)
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# USER FUNCTIONS
# ==========================

def register_user(
        username,
        password,
        role
):

    try:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password,
                role
            )
            VALUES (?,?,?)
            """,
            (
                username,
                password,
                role
            )
        )

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:

        return False


def validate_user(
        username,
        password
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?
        """,
        (
            username,
            password
        )
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================
# STUDENT FUNCTIONS
# ==========================

def add_student(
        roll,
        name,
        class_name,
        email
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (
            roll,
            name,
            class_name,
            email
        )
        VALUES (?,?,?,?)
        """,
        (
            roll,
            name,
            class_name,
            email
        )
    )

    conn.commit()
    conn.close()


def get_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        ORDER BY roll
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def search_students(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE roll LIKE ?
        OR name LIKE ?
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%"
        )
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def total_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================
# ATTENDANCE FUNCTIONS
# ==========================

def attendance_exists(
        student_id,
        date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attendance
        WHERE student_id=?
        AND date=?
        """,
        (
            student_id,
            date
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_attendance(
        student_id,
        date,
        status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attendance
        (
            student_id,
            date,
            status
        )
        VALUES (?,?,?)
        """,
        (
            student_id,
            date,
            status
        )
    )

    conn.commit()
    conn.close()


def get_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        attendance.id,
        students.roll,
        students.name,
        attendance.date,
        attendance.status
    FROM attendance
    INNER JOIN students
    ON attendance.student_id = students.id
    ORDER BY attendance.date DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def attendance_by_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT status
        FROM attendance
        WHERE student_id=?
        """,
        (student_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def attendance_by_date(date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            attendance.id,
            students.roll,
            students.name,
            attendance.date,
            attendance.status
        FROM attendance
        INNER JOIN students
        ON attendance.student_id = students.id
        WHERE attendance.date=?
        """,
        (date,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_attendance_percentage(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id=?
        """,
        (student_id,)
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE student_id=?
        AND status='Present'
        """,
        (student_id,)
    )

    present = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        return 0

    return round(
        (present / total) * 100,
        2
    )


def attendance_summary():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM attendance
    GROUP BY status
    """)

    data = cursor.fetchall()

    conn.close()

    return data