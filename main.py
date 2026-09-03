from database import Database
from patient import Patient
from doctor import Doctor
from hospital import Hospital


def main():

    db = Database()
    hospital = Hospital(db)

    while True:

        print("\n")
        print("=" * 60)
        print("        HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 60)

        print("""
1. Add Patient
2. View Patients
3. Search Patient
4. Update Patient
5. Delete Patient

6. Add Doctor
7. View Doctors

8. Book Appointment
9. View Appointments
10. Cancel Appointment

11. Add Patient Visit
12. View Patient History

13. Generate Bill
14. View Bills

0. Exit
""")

        choice = input("Enter your choice: ")

        # ====================================================
        # PATIENT
        # ====================================================

        if choice == "1":

            try:

                patient_id = int(
                    input("Enter Patient ID: ")
                )

                name = input("Enter Name: ")

                age = int(
                    input("Enter Age: ")
                )

                gender = input("Enter Gender: ")

                phone = input("Enter Phone: ")

                disease = input("Enter Disease: ")

                patient = Patient(
                    db,
                    patient_id,
                    name,
                    age,
                    gender,
                    phone,
                    disease
                )

                patient.add_patient()

            except ValueError:

                print("\nPlease enter valid numeric values.")

        elif choice == "2":

            hospital.view_patients()

        elif choice == "3":

            try:
                hospital.search_patient()

            except ValueError:
                print("\nInvalid Patient ID.")

        elif choice == "4":

            try:
                hospital.update_patient()

            except ValueError:
                print("\nInvalid input.")

        elif choice == "5":

            try:
                hospital.delete_patient()

            except ValueError:
                print("\nInvalid Patient ID.")

        # ====================================================
        # DOCTOR
        # ====================================================

        elif choice == "6":

            try:

                doctor_id = int(
                    input("Enter Doctor ID: ")
                )

                name = input("Enter Doctor Name: ")

                specialization = input(
                    "Enter Specialization: "
                )

                phone = input("Enter Phone: ")

                doctor = Doctor(
                    db,
                    doctor_id,
                    name,
                    specialization,
                    phone
                )

                doctor.add_doctor()

            except ValueError:

                print("\nPlease enter valid values.")

        elif choice == "7":

            hospital.view_doctors()

        # ====================================================
        # APPOINTMENT
        # ====================================================

        elif choice == "8":

            try:
                hospital.book_appointment()

            except ValueError:
                print("\nInvalid input.")

        elif choice == "9":

            hospital.view_appointments()

        elif choice == "10":

            try:
                hospital.cancel_appointment()

            except ValueError:
                print("\nInvalid Appointment ID.")

        # ====================================================
        # VISIT
        # ====================================================

        elif choice == "11":

            try:
                hospital.add_visit()

            except ValueError:
                print("\nInvalid input.")

        elif choice == "12":

            try:
                hospital.patient_history()

            except ValueError:
                print("\nInvalid Patient ID.")

        # ====================================================
        # BILL
        # ====================================================

        elif choice == "13":

            try:
                hospital.generate_bill()

            except ValueError:
                print("\nInvalid input.")

        elif choice == "14":

            hospital.view_bills()

        # ====================================================
        # EXIT
        # ====================================================

        elif choice == "0":

            print("\nThank you for using Hospital Management System.")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
