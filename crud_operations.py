# CRUD Operations for Electronic Health Records System

## 1. Managing Patients
class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def create(patient_id, name, age, gender):
        return Patient(patient_id, name, age, gender)

    @staticmethod
    def update(patient, name=None, age=None, gender=None):
        if name:
            patient.name = name
        if age:
            patient.age = age
        if gender:
            patient.gender = gender

    @staticmethod
    def delete(patient):
        # Logic to delete patient
        del patient

## 2. Managing Doctors
class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    @staticmethod
    def create(doctor_id, name, specialty):
        return Doctor(doctor_id, name, specialty)

    @staticmethod
    def update(doctor, name=None, specialty=None):
        if name:
            doctor.name = name
        if specialty:
            doctor.specialty = specialty

    @staticmethod
    def delete(doctor):
        # Logic to delete doctor
        del doctor

## 3. Managing Appointments
class Appointment:
    def __init__(self, appointment_id, patient, doctor, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.time = time

    @staticmethod
    def create(appointment_id, patient, doctor, time):
        return Appointment(appointment_id, patient, doctor, time)

    @staticmethod
    def update(appointment, time=None):
        if time:
            appointment.time = time

    @staticmethod
    def delete(appointment):
        # Logic to delete appointment
        del appointment

## 4. Managing Medications
class Medication:
    def __init__(self, medication_id, name, dosage):
        self.medication_id = medication_id
        self.name = name
        self.dosage = dosage

    @staticmethod
    def create(medication_id, name, dosage):
        return Medication(medication_id, name, dosage)

    @staticmethod
    def update(medication, name=None, dosage=None):
        if name:
            medication.name = name
        if dosage:
            medication.dosage = dosage

    @staticmethod
    def delete(medication):
        # Logic to delete medication
        del medication

## 5. Managing Diagnoses
class Diagnosis:
    def __init__(self, diagnosis_id, name):
        self.diagnosis_id = diagnosis_id
        self.name = name

    @staticmethod
    def create(diagnosis_id, name):
        return Diagnosis(diagnosis_id, name)

    @staticmethod
    def update(diagnosis, name=None):
        if name:
            diagnosis.name = name

    @staticmethod
    def delete(diagnosis):
        # Logic to delete diagnosis
        del diagnosis

## 6. Managing Allergies
class Allergy:
    def __init__(self, allergy_id, name):
        self.allergy_id = allergy_id
        self.name = name

    @staticmethod
    def create(allergy_id, name):
        return Allergy(allergy_id, name)

    @staticmethod
    def update(allergy, name=None):
        if name:
            allergy.name = name

    @staticmethod
    def delete(allergy):
        # Logic to delete allergy
        del allergy

## 7. Managing Lab Results
class LabResult:
    def __init__(self, result_id, test_name, result):
        self.result_id = result_id
        self.test_name = test_name
        self.result = result

    @staticmethod
    def create(result_id, test_name, result):
        return LabResult(result_id, test_name, result)

    @staticmethod
    def update(lab_result, result=None):
        if result:
            lab_result.result = result

    @staticmethod
    def delete(lab_result):
        # Logic to delete lab result
        del lab_result

## 8. Managing Billing Records
class Billing:
    def __init__(self, billing_id, patient, amount):
        self.billing_id = billing_id
        self.patient = patient
        self.amount = amount

    @staticmethod
    def create(billing_id, patient, amount):
        return Billing(billing_id, patient, amount)

    @staticmethod
    def update(billing, amount=None):
        if amount:
            billing.amount = amount

    @staticmethod
    def delete(billing):
        # Logic to delete billing record
        del billing