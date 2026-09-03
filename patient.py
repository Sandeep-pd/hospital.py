import sqlite3

class Patient:

    def __init__(
        self,
        db,
        patient_id,
        name,
        age,
        gender,
        phone,
        disease
    ):
        self.db = db
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.disease = disease

    def add_patient(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO patients
                (patient_id, name, age, gender, phone, disease)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.patient_id,
                self.name,
                self.age,
                self.gender,
                self.phone,
                self.disease
            ))

            conn.commit()

            print("\nPatient added successfully.")

        except sqlite3.IntegrityError:

            print("\nPatient ID already exists.")

        finally:

            conn.close()
