import sqlite3

class Doctor:

    def __init__(
        self,
        db,
        doctor_id,
        name,
        specialization,
        phone
    ):
        self.db = db
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.phone = phone

    def add_doctor(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO doctors
                (doctor_id, name, specialization, phone)
                VALUES (?, ?, ?, ?)
            """, (
                self.doctor_id,
                self.name,
                self.specialization,
                self.phone
            ))

            conn.commit()

            print("\nDoctor added successfully.")

        except sqlite3.IntegrityError:

            print("\nDoctor ID already exists.")

        finally:

            conn.close()
