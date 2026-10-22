"""
Problem Statement:
Create a class Person and derive Doctor and Patient.
Create additional classes Surgeon and MedicalResearcher.
Design the hierarchy to demonstrate multiple inheritance
along with hierarchical inheritance.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def doctor_details(self, specialization):
        self.specialization = specialization
        print("Specialization:", self.specialization)


class Patient(Person):
    def patient_details(self, disease):
        self.disease = disease
        print("Disease:", self.disease)


class MedicalResearcher(Person):
    def research_details(self, topic):
        self.topic = topic
        print("Research Topic:", self.topic)


class Surgeon(Doctor, MedicalResearcher):
    def display(self):
        self.display_person()
        print("Specialization:", self.specialization)
        print("Research Topic:", self.topic)


s = Surgeon("Dr. Rahul", 40)

s.doctor_details("General Surgery")
s.research_details("Cancer Research")

print("Surgeon Details:")
s.display()

print()

p = Patient("Amit", 25)

print("Patient Details:")
p.display_person()
p.patient_details("Fever")