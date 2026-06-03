

class Patient:
    def __init__(self, unique_patient_id, name, age, disease):
        self.patient_id = int(unique_patient_id)
        self.name = name
        self.age = age
        self.disease = disease
        self.history = []

    def visit_patient(self, disease, doctor, date, medicine, bill):
        visit_details = {
            'disease': disease,
            'doctor': doctor,
            'date': date,
            'medicine': medicine,
            'bill': bill.calculate_total()

        }
        self.history.append(visit_details)

        # store data
        print('visit added')

    def get_patient_details(self):
        print('Id: ', self.patient_id)
        print('Name: ', self.name)
        print('Age: ', self.age)

        print('\n----patient history----')

        for visit in self.history:
            print("Disease :", visit['disease'])
            print("Doctor  :", visit['doctor'])
            print("Date    :", visit['date'])
            print("Medicine:", visit['medicine'])
            print("Bill    :", visit['bill'])


            print('----------------')

# --------------------Doctor___________________________________#
class Doctor:
    def __init__(self, unique_id, name, specialization, schedule):
        self.unique_id = unique_id
        self.name = name
        self.specialization = specialization
        self.schedule = schedule


        self.available_slots = [
            '9am',
            '10am',
            '12pm'

        ]

    def get_doctor_details(self):
        print("id: ", self.unique_id)
        print("name: ", self.name)
        print("specialization: ", self.specialization)
        print("schedule: ", self.schedule)


        print('\nAvailable slots')

        for slot in self.available_slots:
            print(slot)


# ________________hospital  System_______________________#

class HospitalSystem:

    def request_appointment(self, patient, doctor, date,time):

        if time in doctor.available_slots:

            print('Appointment Confirmed')
            print(f'patient: {patient.name}')
            print(f'doctor: {doctor.name}')
            print(f'date: {date}')
            print(f'time: {time}')


            # doctor.available._slots.remove(time)
        else:

            print('\nAppointment Not Available')


# -----------------BILL_________________________________________#
class Bill:
    def __init__(self, doctor_fee, medicine_charge, lab_charge):
        self.doctor_fee = doctor_fee
        self.medicine_charge = medicine_charge
        self.lab_charge = lab_charge

    def calculate_total(self):
        total = (self.doctor_fee + self.medicine_charge + self.lab_charge)
        return total

    def bill(self):

        print('\n------Bill Details--------')

        print('doctor:', self.doctor_fee)
        print('medicine:', self.medicine_charge)
        print('lab:', self.lab_charge)


# patient
p1 = Patient(101, "sandeep", 22, "Fever")

# doctor
d1 = Doctor(1, "Dr Raj", "General", "Monday to friday")

# bill
b1 = Bill(500, 200, 300)

p1.visit_patient(
    "Fever",
    'Dr Raj',
    "10-05-2026",
    "Paracetamol",
    b1)

p1.get_patient_details()


d1 = Doctor(
    1,
    "Dr Raj",
    "Cardiologist",
    "Monday to Friday"
)

d1.get_doctor_details()

h1 = HospitalSystem()



# first booking
h1.request_appointment(
    p1,
    d1,
    "monday ",
     '10am'
)
b1.calculate_total()
b1.bill()



