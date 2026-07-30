class Hospital:

    def __init__(self):
        self.doctors = {
            "Dr. Smith": True,
            "Dr. John": False,
            "Dr. Priya": True
        }

    def book_appointment(self, doctor):
        if doctor not in self.doctors:
            return "Doctor Not Found"

        if self.doctors[doctor]:
            return "Appointment Confirmed"
        else:
            return "Doctor Not Available"


hospital = Hospital()

print(hospital.book_appointment("Dr. Smith"))
print(hospital.book_appointment("Dr. John"))
print(hospital.book_appointment("Dr. Priya"))
print(hospital.book_appointment("Dr. Ravi"))