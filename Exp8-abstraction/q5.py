# Q5. Create an abstract class Patient with abstract methods calculate_bill() and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods according to the patient type.

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        return "In-patient treatment with hospital stay"

class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        return "Out-patient consultation"

class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        return "Emergency treatment"

in_patient = InPatient()
out_patient = OutPatient()
emergency_patient = EmergencyPatient()

print("In-Patient Treatment:", in_patient.treatment())
print("In-Patient Bill:", in_patient.calculate_bill())

print("Out-Patient Treatment:", out_patient.treatment())
print("Out-Patient Bill:", out_patient.calculate_bill())

print("Emergency Treatment:", emergency_patient.treatment())
print("Emergency Bill:", emergency_patient.calculate_bill())