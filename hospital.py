from datetime import datetime

class Hospital:

    def __init__(self, db):
        self.db = db

    # ========================================================
    # PATIENT METHODS
    # ========================================================

    def view_patients(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                patient_id,
                name,
                age,
                gender,
                phone,
                disease
            FROM patients
        """)

        patients = cursor.fetchall()

        conn.close()

        if not patients:

            print("\nNo patients found.")
            return

        print("\n" + "=" * 80)
        print("PATIENT LIST")
        print("=" * 80)

        for patient in patients:

            print(
                f"ID: {patient[0]} | "
                f"Name: {patient[1]} | "
                f"Age: {patient[2]} | "
                f"Gender: {patient[3]} | "
                f"Phone: {patient[4]} | "
                f"Disease: {patient[5]}"
            )

    # --------------------------------------------------------

    def search_patient(self):

        patient_id = int(input("\nEnter Patient ID: "))

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        conn.close()

        if patient:

            print("\n" + "=" * 50)
            print("PATIENT DETAILS")
            print("=" * 50)

            print("Patient ID :", patient[0])
            print("Name       :", patient[1])
            print("Age        :", patient[2])
            print("Gender     :", patient[3])
            print("Phone      :", patient[4])
            print("Disease    :", patient[5])

        else:

            print("\nPatient not found.")

    # --------------------------------------------------------

    def update_patient(self):

        patient_id = int(input("\nEnter Patient ID: "))

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        if not patient:

            print("\nPatient not found.")
            conn.close()
            return

        print("\nEnter new information")

        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        phone = input("Phone: ")
        disease = input("Disease: ")

        cursor.execute("""
            UPDATE patients
            SET
                name = ?,
                age = ?,
                gender = ?,
                phone = ?,
                disease = ?
            WHERE patient_id = ?
        """, (
            name,
            age,
            gender,
            phone,
            disease,
            patient_id
        ))

        conn.commit()
        conn.close()

        print("\nPatient updated successfully.")

    # --------------------------------------------------------

    def delete_patient(self):

        patient_id = int(input("\nEnter Patient ID: "))

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        if not patient:

            print("\nPatient not found.")
            conn.close()
            return

        confirmation = input(
            "Are you sure you want to delete this patient? (yes/no): "
        )

        if confirmation.lower() == "yes":

            cursor.execute("""
                DELETE FROM patients
                WHERE patient_id = ?
            """, (patient_id,))

            conn.commit()

            print("\nPatient deleted successfully.")

        else:

            print("\nDelete operation cancelled.")

        conn.close()

    # ========================================================
    # DOCTOR METHODS
    # ========================================================

    def view_doctors(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                doctor_id,
                name,
                specialization,
                phone
            FROM doctors
        """)

        doctors = cursor.fetchall()

        conn.close()

        if not doctors:

            print("\nNo doctors found.")
            return

        print("\n" + "=" * 80)
        print("DOCTOR LIST")
        print("=" * 80)

        for doctor in doctors:

            print(
                f"ID: {doctor[0]} | "
                f"Name: {doctor[1]} | "
                f"Specialization: {doctor[2]} | "
                f"Phone: {doctor[3]}"
            )

    # ========================================================
    # APPOINTMENT
    # ========================================================

    def book_appointment(self):

        patient_id = int(input("\nEnter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))
        appointment_date = input(
            "Enter appointment date (DD-MM-YYYY HH:MM): "
        )

        conn = self.db.connect()
        cursor = conn.cursor()

        # Check patient

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        if not patient:

            print("\nPatient does not exist.")
            conn.close()
            return

        # Check doctor

        cursor.execute("""
            SELECT *
            FROM doctors
            WHERE doctor_id = ?
        """, (doctor_id,))

        doctor = cursor.fetchone()

        if not doctor:

            print("\nDoctor does not exist.")
            conn.close()
            return

        # Create appointment

        cursor.execute("""
            INSERT INTO appointments
            (patient_id, doctor_id, appointment_date)
            VALUES (?, ?, ?)
        """, (
            patient_id,
            doctor_id,
            appointment_date
        ))

        conn.commit()

        appointment_id = cursor.lastrowid

        conn.close()

        print("\nAppointment booked successfully.")
        print("Appointment ID:", appointment_id)

    # --------------------------------------------------------

    def view_appointments(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                a.appointment_id,
                p.name,
                d.name,
                d.specialization,
                a.appointment_date,
                a.status

            FROM appointments a

            JOIN patients p
                ON a.patient_id = p.patient_id

            JOIN doctors d
                ON a.doctor_id = d.doctor_id

            ORDER BY a.appointment_date
        """)

        appointments = cursor.fetchall()

        conn.close()

        if not appointments:

            print("\nNo appointments found.")
            return

        print("\n" + "=" * 100)
        print("APPOINTMENTS")
        print("=" * 100)

        for appointment in appointments:

            print(
                f"Appointment ID: {appointment[0]} | "
                f"Patient: {appointment[1]} | "
                f"Doctor: {appointment[2]} | "
                f"Specialization: {appointment[3]} | "
                f"Date: {appointment[4]} | "
                f"Status: {appointment[5]}"
            )

    # --------------------------------------------------------

    def cancel_appointment(self):

        appointment_id = int(
            input("\nEnter Appointment ID: ")
        )

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM appointments
            WHERE appointment_id = ?
        """, (appointment_id,))

        appointment = cursor.fetchone()

        if not appointment:

            print("\nAppointment not found.")
            conn.close()
            return

        cursor.execute("""
            UPDATE appointments
            SET status = 'Cancelled'
            WHERE appointment_id = ?
        """, (appointment_id,))

        conn.commit()
        conn.close()

        print("\nAppointment cancelled successfully.")

    # ========================================================
    # VISIT / TREATMENT
    # ========================================================

    def add_visit(self):

        patient_id = int(input("\nEnter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))

        diagnosis = input("Enter diagnosis: ")
        medicine = input("Enter medicine: ")

        visit_date = datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )

        conn = self.db.connect()
        cursor = conn.cursor()

        # Check patient

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        if not patient:

            print("\nPatient not found.")
            conn.close()
            return

        # Check doctor

        cursor.execute("""
            SELECT *
            FROM doctors
            WHERE doctor_id = ?
        """, (doctor_id,))

        doctor = cursor.fetchone()

        if not doctor:

            print("\nDoctor not found.")
            conn.close()
            return

        cursor.execute("""
            INSERT INTO visits
            (
                patient_id,
                doctor_id,
                diagnosis,
                medicine,
                visit_date
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            patient_id,
            doctor_id,
            diagnosis,
            medicine,
            visit_date
        ))

        conn.commit()
        conn.close()

        print("\nVisit added successfully.")

    # --------------------------------------------------------

    def patient_history(self):

        patient_id = int(input("\nEnter Patient ID: "))

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                v.visit_id,
                p.name,
                d.name,
                v.diagnosis,
                v.medicine,
                v.visit_date

            FROM visits v

            JOIN patients p
                ON v.patient_id = p.patient_id

            JOIN doctors d
                ON v.doctor_id = d.doctor_id

            WHERE v.patient_id = ?

            ORDER BY v.visit_date DESC
        """, (patient_id,))

        history = cursor.fetchall()

        conn.close()

        if not history:

            print("\nNo medical history found.")
            return

        print("\n" + "=" * 80)
        print("PATIENT MEDICAL HISTORY")
        print("=" * 80)

        for visit in history:

            print("Visit ID   :", visit[0])
            print("Patient    :", visit[1])
            print("Doctor     :", visit[2])
            print("Diagnosis  :", visit[3])
            print("Medicine   :", visit[4])
            print("Visit Date :", visit[5])
            print("-" * 80)

    # ========================================================
    # BILLING
    # ========================================================

    def generate_bill(self):

        patient_id = int(input("\nEnter Patient ID: "))

        consultation_fee = float(
            input("Enter consultation fee: ")
        )

        medicine_cost = float(
            input("Enter medicine cost: ")
        )

        total = consultation_fee + medicine_cost

        bill_date = datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )

        conn = self.db.connect()
        cursor = conn.cursor()

        # Check patient

        cursor.execute("""
            SELECT *
            FROM patients
            WHERE patient_id = ?
        """, (patient_id,))

        patient = cursor.fetchone()

        if not patient:

            print("\nPatient not found.")
            conn.close()
            return

        cursor.execute("""
            INSERT INTO bills
            (
                patient_id,
                consultation_fee,
                medicine_cost,
                total,
                bill_date
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            patient_id,
            consultation_fee,
            medicine_cost,
            total,
            bill_date
        ))

        conn.commit()

        bill_id = cursor.lastrowid

        conn.close()

        print("\n" + "=" * 50)
        print("HOSPITAL BILL")
        print("=" * 50)

        print("Bill ID          :", bill_id)
        print("Patient ID       :", patient_id)
        print("Patient Name     :", patient[1])
        print("Consultation Fee :", consultation_fee)
        print("Medicine Cost    :", medicine_cost)
        print("-" * 50)
        print("TOTAL            :", total)
        print("Bill Date        :", bill_date)
        print("=" * 50)

    # --------------------------------------------------------

    def view_bills(self):

        conn = self.db.connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                b.bill_id,
                p.name,
                b.consultation_fee,
                b.medicine_cost,
                b.total,
                b.bill_date

            FROM bills b

            JOIN patients p
                ON b.patient_id = p.patient_id

            ORDER BY b.bill_id DESC
        """)

        bills = cursor.fetchall()

        conn.close()

        if not bills:

            print("\nNo bills found.")
            return

        print("\n" + "=" * 100)
        print("BILL HISTORY")
        print("=" * 100)

        for bill in bills:

            print(
                f"Bill ID: {bill[0]} | "
                f"Patient: {bill[1]} | "
                f"Consultation: ₹{bill[2]} | "
                f"Medicine: ₹{bill[3]} | "
                f"Total: ₹{bill[4]} | "
                f"Date: {bill[5]}"
            )