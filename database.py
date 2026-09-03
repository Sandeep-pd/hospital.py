import sqlite3

class Database:

    def __init__(self, db_name="hospital.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):

        conn = self.connect()
        cursor = conn.cursor()

        # Enable Foreign Keys in SQLite
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Patient table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                phone TEXT,
                disease TEXT
            )
        """)

        # Doctor table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                specialization TEXT NOT NULL,
                phone TEXT
            )
        """)

        # Appointment table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                appointment_date TEXT NOT NULL,
                status TEXT DEFAULT 'Scheduled',

                FOREIGN KEY(patient_id)
                REFERENCES patients(patient_id),

                FOREIGN KEY(doctor_id)
                REFERENCES doctors(doctor_id)
            )
        """)

        # Visits / treatment history
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                diagnosis TEXT NOT NULL,
                medicine TEXT,
                visit_date TEXT NOT NULL,

                FOREIGN KEY(patient_id)
                REFERENCES patients(patient_id),

                FOREIGN KEY(doctor_id)
                REFERENCES doctors(doctor_id)
            )
        """)

        # Bills
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bills (
                bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                consultation_fee REAL NOT NULL,
                medicine_cost REAL NOT NULL,
                total REAL NOT NULL,
                bill_date TEXT NOT NULL,

                FOREIGN KEY(patient_id)
                REFERENCES patients(patient_id)
            )
        """)

        conn.commit()
        conn.close()
