from inflammation.models import Doctor, Patient, Person

doc = Doctor('Alice')

doc.add_patient('Jesus')
print(doc.patients)
print(doc)


