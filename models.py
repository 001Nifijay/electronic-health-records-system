from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Float
from sqlalchemy.orm import relationship
from database import Base  # Assuming you have a Base class for declarative model

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    allergies = relationship('Allergy', backref='patient')
    appointments = relationship('Appointment', backref='patient')
    # Add other fields as necessary

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    appointments = relationship('Appointment', backref='doctor')
    # Add other fields as necessary

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    # Add other fields as necessary

class Medication(Base):
    __tablename__ = 'medications'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    patients = relationship('Patient', backref='medications')
    # Add other fields as necessary

class Diagnosis(Base):
    __tablename__ = 'diagnoses'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    description = Column(String, nullable=False)
    # Add other fields as necessary

class Allergy(Base):
    __tablename__ = 'allergies'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    allergy_name = Column(String, nullable=False)
    # Add other fields as necessary

class LabResult(Base):
    __tablename__ = 'lab_results'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    test_name = Column(String, nullable=False)
    result_value = Column(Float, nullable=False)
    # Add other fields as necessary

class Billing(Base):
    __tablename__ = 'billing'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    amount_due = Column(Float, nullable=False)
    paid = Column(Integer, nullable=False)  # 0 for unpaid, 1 for paid
    # Add other fields as necessary
