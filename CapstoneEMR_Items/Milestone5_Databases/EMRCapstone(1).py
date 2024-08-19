#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install pymongo


# In[3]:


# Import necessary libraries
from pymongo import MongoClient, ASCENDING

# Connect to MongoDB
client = MongoClient("mongodb+srv://nessa071390:Imp4l4013!@emrcapstone.5ocuvyf.mongodb.net/")
db = client.EMRCapstone

# Create indexes for collections (if not already created)
db.users.create_index([("user_id", ASCENDING)], unique=True, name="user_id_index")
db.patients.create_index([("patient_id", ASCENDING)], unique=True, name="patient_id_index")
db.patients.create_index([("user_id", ASCENDING)], unique=True, name="user_id_index")
db.doctors.create_index([("doctor_id", ASCENDING)], unique=True, name="doctor_id_index")
db.doctors.create_index([("user_id", ASCENDING)], unique=True, name="user_id_index")
db.nurses.create_index([("nurse_id", ASCENDING)], unique=True, name="nurse_id_index")
db.nurses.create_index([("user_id", ASCENDING)], unique=True, name="user_id_index")
db.office_administrators.create_index([("admin_id", ASCENDING)], unique=True, name="admin_id_index")
db.office_administrators.create_index([("user_id", ASCENDING)], unique=True, name="user_id_index")
db.medical_records.create_index([("record_id", ASCENDING)], unique=True, name="record_id_index")
db.medical_notes.create_index([("note_id", ASCENDING)], unique=True, name="note_id_index")
db.medical_notes.create_index([("medical_record_id", ASCENDING)], name="medical_record_id_index")
db.appointments.create_index([("appointment_id", ASCENDING)], unique=True, name="appointment_id_index")
db.appointments.create_index([("patient_id", ASCENDING)], name="patient_id_index")
db.appointments.create_index([("doctor_id", ASCENDING)], name="doctor_id_index")

print("Database connected and indexes created.")


# In[4]:


# Insert a user
user1 = {"user_id": 1, "username": "patient1", "password": "password123", "role": "patient"}
user2 = {"user_id": 2, "username": "doctor1", "password": "password123", "role": "doctor"}
user3 = {"user_id": 3, "username": "nurse1", "password": "password123", "role": "nurse"}
user4 = {"user_id": 4, "username": "admin1", "password": "password123", "role": "administrator"}
db.users.insert_many([user1, user2, user3, user4])

# Insert a patient
patient = {
    "patient_id": 1,
    "user_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-01-01",
    "contact_information": "123 Main St",
    "assigned_doctor": None,
    "assigned_nurse": None
}
db.patients.insert_one(patient)

# Insert a doctor
doctor = {
    "doctor_id": 1,
    "user_id": 2,
    "first_name": "Alice",
    "last_name": "Smith",
    "specialty": "Cardiology",
    "contact_information": "456 Elm St"
}
db.doctors.insert_one(doctor)

# Insert a nurse
nurse = {
    "nurse_id": 1,
    "user_id": 3,
    "first_name": "Bob",
    "last_name": "Brown",
    "contact_information": "789 Oak St"
}
db.nurses.insert_one(nurse)

# Insert an office administrator
admin = {
    "admin_id": 1,
    "user_id": 4,
    "first_name": "Admin",
    "last_name": "User",
    "contact_information": "admin@example.com"
}
db.office_administrators.insert_one(admin)

print("Documents inserted.")


# In[5]:


# Find one patient
patient = db.patients.find_one({"patient_id": 1})
print(patient)


# In[6]:


# Find all doctors
doctors = db.doctors.find()
for doctor in doctors:
    print(doctor)


# In[7]:


# Update a patient's assigned doctor and nurse
db.patients.update_one(
    {"patient_id": 1},
    {"$set": {"assigned_doctor": doctor["doctor_id"], "assigned_nurse": nurse["nurse_id"]}}
)


# In[8]:


updated_patient = db.patients.find_one({"patient_id": 1})
print(updated_patient)


# In[22]:


# Insert a medical record
medical_record = {
    "record_id": 1,
    "patient_id": 1,
    "doctor_id": 1,
    "nurse_id": 1,
    "diagnosis": "Hypertension",
    "treatment": "Medication",
    "date_of_record": "2024-05-22"
}
db.medical_records.insert_one(medical_record)

# Insert a medical note
medical_note = {
    "note_id": 1,
    "medical_record_id": 1,
    "author_id": 2,
    "note_content": "Patient needs to follow up in 6 months.",
    "date_of_note": "2024-05-22"
}
db.medical_notes.insert_one(medical_note)

# Insert an appointment
appointment = {
    "appointment_id": 1,
    "patient_id": 1,
    "doctor_id": 1,
    "appointment_date": None,
    "reason": "Routine checkup",
    "is_booked": False
}
db.appointments.insert_one(appointment)

print("Documents inserted.")


# In[24]:


#Comment for the above duplicate error, I thought it timed out and didn't enter the information into the database, but it did.


# In[12]:


# Update the medical note for John Doe (note_id = 1)
new_note_content = "Follow-up after 3 months instead of 6 months."
db.medical_notes.update_one(
    {"note_id": 1},
    {"$set": {"note_content": new_note_content, "date_of_note": "2024-05-22"}}
)


# In[21]:


# Verify the updated note
updated_note = db.medical_notes.find_one({"note_id": 1})
print(updated_note)


# In[ ]:




