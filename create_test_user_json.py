import json
import uuid
from datetime import datetime, date
import random

y_n_list = ["Yes", "No"]
t_f_list = ["True", "False"]
grades = ["K", "1", "2", "3", "4", "5", "6"]
grades_map = {"K": None, "1": "K", "2": "1", "3":"2", "4":"3", "5":"4", "6":"5"}
gender = ["Male", "Female"]

current_datetime = datetime.now()
random_grade_index = random.randrange(7)
year_dob = 2023 - random_grade_index - 5 # b/c kindergarden enterance grade is 5
month_dob = random.randrange(1,13)
date_dob = random.randrange(1,29)
full_dob = "{}T00:00:00".format(date(year_dob, month_dob, date_dob))

existing_parent_uuid = "6d4409eb-a3cf-4066-91b9-da79872e1d5d"
existing_parent_email = "SATestParent_23_03_30_14_35_02@fake.org"
existing_round_app_id = "a9238e82-80ba-471a-971e-9dee29d1959c"

# set defaults
run_by = "00ue20xb6g3CZKVCH0h7" # hard-coded as admin
batch_id = "eaf2cfb2-cd62-4aef-8d3c-0c684199689c" # hard-coded for all test accounts in prod
scholar_uuid = str(uuid.uuid4()) # script generated uuid "abaf2f50-ce4e-11ed-afa1-0242ac120002"
scholar_contact_lastmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S")  # today's system date "2023-03-29T17:34:30"
scholar_contact_systemmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-03-29T17:34:30"
student_first_name__c = "SATestScholar" # promt user to enter, or default to "SATestScholar"
student_last_name__c = current_datetime.strftime("%y_%m_%d_%H_%M_%S") # prompt user or default to current time in YYYYMMDDHHMMSS
gender__c = random.choice(gender) # prompt user or randomly pick "Female"/"Male"
scholar_date_of_birth = full_dob # prompt user or randomly generate "2010-01-07T00:00:00"
round_app_name = "A-00099999" # hard-coded as "A-00099999"
round_app_uuid = str(uuid.uuid4()) # script generated uuid "f4ed2d34-ce4e-11ed-afa1-0242ac120002"
round_app_type = "K-6 Application" # hard-coded as "K-6 Application"
round_app_term = "2023-2024" # hard-coded as "2023-2024"
round_app_initial_submission_date = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-02-22T17:10:29"
round_app_lastmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-02-22T17:10:29"
round_app_systemmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-02-22T17:10:29"
scholar_future_accepted_school = "Training" # MUST be hard-coded as "Training"
scholar_future_accepted_school_sisid = 12562 # MUST be hard-coded as 12562
scholar_future_grade = grades[random_grade_index] # prompt user or randomly pick between K-12 "5"
scholar_current_accepted_school = None # hard-coded as None
scholar_current_accepted_school_sisid = None # hard-coded as None
scholar_current_accepted_grade = grades_map[scholar_future_grade] # scholar_future_grade - 1 "4"
parent_uuid = str(uuid.uuid4()) # script generated uuid "04ac35e4-ce4f-11ed-afa1-0242ac120002"
parent_firstname = "SATestParent" # promt user to enter, or default to "SATestParent"
parent_lastname = current_datetime.strftime("%y_%m_%d_%H_%M_%S") # prompt user or default to current time in YYYYMMDDHHMMSS
parent_email = "{}_{}@fake.org".format(parent_firstname, parent_lastname) # prompt user or default to "Mohini.n.jaiswal@gmail.com"
parent_primary_contact_number = str(random.randrange(1000000000,10000000000)) # prompt user or default to "9999999999"
parent_primary_phone_type = "Cell Phone" # hard-coded as "Cell Phone"
parent_address = "123 Fake St" # prompt user or default to "123 Fake St"
parent_apt = None # prompt user or default to None
parent_city = "New York" # prompt user or default to "New York"
parent_state = "NY" # prompt user or default to "NY"
parent_zip_code = "10001" # prompt user or default to "10001"
parent_sis_household_id = None # hard-coded as None
parent_lastmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-02-22T20:09:54"
parent_systemmodifieddate = current_datetime.strftime("%Y-%m-%dT%H:%M:%S") # today's system date "2023-02-22T20:09:54"
has_uniform_on_order__c = random.choice(t_f_list) # prompt user or default randomly pick "True"/"False"
interest_in_summer_school__c = random.choice(y_n_list) # prompt user or default randomly pick "Yes"/"No"

# inputs from user
print("Enter the required user details, or it will default.")
print("*Asterisk fields are randomly generated.")
is_new_parent = input("Create with defaults? Y/N (default: Y) = " or "Y")
if is_new_parent == "N":
    student_first_name__c = input("\t01/17 Student first name (default: {}) = ".format(student_first_name__c)) or student_first_name__c
    student_last_name__c = input("\t02/17 Student last name (default: {}) = ".format(student_last_name__c)) or student_last_name__c
    gender__c = input("\t03/17 Student gender Male/Female (default: {})* = ".format(gender__c)) or gender__c
    scholar_date_of_birth = input("\t04/17 Student DOB (default: {})* = ".format(scholar_date_of_birth)) or scholar_date_of_birth
    scholar_future_grade = input("\t05/17 Student future grade K-12 (default: {})* = ".format(scholar_future_grade)) or scholar_future_grade
    scholar_current_accepted_grade = input("\t06/17 Student current grade K-12 (default: {})* = ".format(scholar_current_accepted_grade)) or scholar_current_accepted_grade
    parent_firstname = input("\t07/17 Parent first name (default: {}) = ".format(parent_firstname)) or parent_firstname
    parent_lastname = input("\t08/17 Parent last name (default: {}) = ".format(parent_lastname)) or parent_lastname
    parent_email = input("\t09/17 Parent email (default: {}) = ".format(parent_email)) or parent_email
    parent_primary_contact_number = input("\t10/17 Parent contact number (default: {})* = ".format(parent_primary_contact_number)) or parent_primary_contact_number
    parent_address = input("\t11/17 Address (default: {}) = ".format(parent_address)) or parent_address
    parent_apt = input("\t12/17 Apt (default: {}) = ".format(parent_apt)) or parent_apt
    parent_city = input("\t13/17 City (default: {}) = ".format(parent_city)) or parent_city
    parent_state = input("\t14/17 State (default: {}) = ".format(parent_state)) or parent_state
    parent_zip_code = input("\t15/17 Zip Code (default: {}) = ".format(parent_zip_code)) or parent_zip_code
    has_uniform_on_order__c = input("\t16/17 Uniform on Order? True/False (default: {})* = ".format(has_uniform_on_order__c)) or has_uniform_on_order__c
    interest_in_summer_school__c = input("\t17/17 Summer School? Yes/No (default: {})* = ".format(interest_in_summer_school__c)) or interest_in_summer_school__c

# create json obj
applicants_data = {
    "scholar_uuid": scholar_uuid, 
    "scholar_contact_lastmodifieddate": scholar_contact_lastmodifieddate, 
    "scholar_contact_systemmodifieddate": scholar_contact_systemmodifieddate, 
    "student_first_name__c": student_first_name__c, 
    "student_last_name__c": student_last_name__c, 
    "gender__c": gender__c, 
    "scholar_date_of_birth": scholar_date_of_birth, 
    "round_app_name": round_app_name, 
    "round_app_uuid": round_app_uuid,
    "round_app_type": round_app_type, 
    "round_app_term": round_app_term, 
    "round_app_initial_submission_date": round_app_initial_submission_date, 
    "round_app_lastmodifieddate": round_app_lastmodifieddate, 
    "round_app_systemmodifieddate": round_app_systemmodifieddate, 
    "scholar_future_accepted_school": scholar_future_accepted_school, 
    "scholar_future_accepted_school_sisid": scholar_future_accepted_school_sisid, 
    "scholar_future_grade": scholar_future_grade, 
    "scholar_current_accepted_school": scholar_current_accepted_school, 
    "scholar_current_accepted_school_sisid": scholar_current_accepted_school_sisid, 
    "scholar_current_accepted_grade": scholar_current_accepted_grade, 
    "parent_uuid": parent_uuid, 
    "parent_firstname": parent_firstname, 
    "parent_lastname": parent_lastname, 
    "parent_email": parent_email, 
    "parent_primary_contact_number": parent_primary_contact_number, 
    "parent_primary_phone_type": parent_primary_phone_type, 
    "parent_address": parent_address, 
    "parent_apt": parent_apt, 
    "parent_city": parent_city, 
    "parent_state": parent_state, 
    "parent_zip_code": parent_zip_code, 
    "parent_sis_household_id": parent_sis_household_id, 
    "parent_lastmodifieddate": parent_lastmodifieddate, 
    "parent_systemmodifieddate": parent_systemmodifieddate, 
    "has_uniform_on_order__c": has_uniform_on_order__c, 
    "interest_in_summer_school__c": interest_in_summer_school__c
}

applicants_data_string = json.dumps(applicants_data)

message = "{\"run_by\": \"00ue20xb6g3CZKVCH0h7\", \"batch_id\": \"eaf2cfb2-cd62-4aef-8d3c-0c684199689c\", \"applicants\": [" + applicants_data_string + "]}"

data = {
	"Records": [{
		"Sns": {
			"Type": "Notification",
			"MessageId": "37cda33a-533a-5c63-9278-ff4ca7e807ea",
			"TopicArn": "arn:aws:sns:us-east-1:928507349660:application-manager-dev-process-applicants",
			"Subject": None,
			"Message": message
		}
	}]
}

print("\nGenerated JSON:\n")
print(json.dumps(data))