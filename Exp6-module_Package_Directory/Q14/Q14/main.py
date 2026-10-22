from patient.patient import patient_details
from doctor.doctor import doctor_details
from billing.bill import calculate_bill
from medical_records.records import medical_record

print("--- Patient Management ---")
patient_details()

print("\n--- Doctor Management ---")
doctor_details()

print("\n--- Medical Records ---")
medical_record()

print("\n--- Billing ---")
calculate_bill(500, 1000)