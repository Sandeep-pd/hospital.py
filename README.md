# 🏥 Hospital Management System (Python OOP Project)

## 📌 Project Overview

This is a simple **Hospital Management System** built using **Python Object-Oriented Programming (OOP)** concepts. The project manages patients, doctors, appointments, and billing information.

The system demonstrates real-world healthcare management operations such as:

* Patient Registration
* Doctor Management
* Appointment Booking
* Patient Visit History
* Bill Generation

---

## 🚀 Features

### 👨‍⚕️ Patient Management

* Store patient information
* Track patient visit history
* View complete patient details

### 🩺 Doctor Management

* Store doctor information
* Manage specialization details
* Display available appointment slots

### 📅 Appointment Booking

* Book appointments with doctors
* Check slot availability
* Display appointment confirmation details

### 💰 Billing System

* Calculate total bill amount
* Include:

  * Doctor Fee
  * Medicine Charges
  * Lab Charges
* Display billing details

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* datetime Module

---

## 📂 Project Structure

```text
hospital_management_system.py

├── Patient Class
├── Doctor Class
├── HospitalSystem Class
├── Bill Class
└── Main Program
```

---

## 📖 OOP Concepts Used

### Classes and Objects

* Patient
* Doctor
* HospitalSystem
* Bill

### Encapsulation

Patient, doctor, and billing data are stored inside objects.

### Composition

The Patient class uses the Bill object to calculate visit expenses.

### Methods

* visit_patient()
* get_patient_details()
* get_doctor_details()
* request_appointment()
* calculate_total()
* bill()

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/hospital-management-system.git
```

2. Navigate to the project folder

```bash
cd hospital-management-system
```

3. Run the Python file

```bash
python hospital_management_system.py
```

---

## 📊 Sample Output

```text
visit added

Id: 101
Name: sandeep
Age: 22

----patient history----
Disease : Fever
Doctor  : Dr Raj
Date    : 10-05-2026
Medicine: Paracetamol
Bill    : 1000

Appointment Confirmed
patient: sandeep
doctor: Dr Raj
date: monday
time: 10am
```

---

## 🔮 Future Improvements

* Store data using SQLite Database
* Add Login and Authentication
* GUI using Tkinter or PyQt
* Export Bills to PDF
* Multiple Doctor Scheduling
* Appointment Cancellation
* Patient Search Functionality

---

## 👨‍💻 Author

**Sandeep**

Python | Data Science | GenAI | Agentic AI Enthusiast

---

## ⭐ GitHub

If you found this project useful, please give it a ⭐ on GitHub.

