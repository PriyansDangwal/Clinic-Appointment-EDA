"""
Clinic Appointment Dataset Cleaning

Description:
This script cleans a raw clinic appointment dataset by handling
missing values, standardizing text values, converting data types,
validating the dataset, and exporting a cleaned CSV file.

Author: Priyansh Dangwal
"""


import pandas as pd
import matplotlib.pyplot as plt
#read csv file.........
df = pd.read_csv("Data/messy_clinic_appointments.csv")

#Data understanding....
print(df.head()) #will return first 5 values of the dataset.
df.info() #will tell you about the datatype and how many values are missing
print(df.columns) #will give the name of the columns in the dataset
print(df.shape) # will tell u abt the (rows, columns) in the dataset

#null values
print(df.isnull().sum()) #100 null values in column gender and billing amount 
print("\n")
print(df.duplicated().sum()) #it has 0 duplicated value 
print(df.dtypes)
print(df["gender"].unique())

pd.set_option("display.max_columns", None)


#renaming columns 
df.rename(columns={
    "patient_id":"Patient_ID",
    "patient_name":"Patient_Name",
    "age":"Age",
    "gender":"Gender",
    "appointment_date":"Appointment_Date",
    "booking_date":"Booking_Date",
    "doctor":"Doctor",
    "department":"Department",
    "billing_amount":"Billing_Amount",
    "follow_up_required":"Follow_Up"
}, inplace=True)

text_columns = ["Patient_Name", "Gender", "Doctor", "Department", "Follow_Up"]

for col in text_columns:
    df[col] = df[col].str.strip().str.title()


# ---------------------------
#sorting and reseting index..... patient id
# ---------------------------
# Generating new unique Patient IDs because original IDs were inconsistent...........
df = df.sort_values(by="Patient_ID").reset_index(drop=True) #the index has been reset and 
df["Patient_ID"] = range(1000, 1000 + len(df)) #new index has been started from 1000 as range(starting value [1000], ending value [len(df)that is 1999])


# ---------------------------
#Patient Name Column
# ---------------------------
print(df["Patient_Name"].duplicated().sum()) #tells you how many duplicated value are there 
print(df[df["Patient_Name"].duplicated(keep=False)]) #return the data of the duplicated value

# ---------------------------
#Age Column
# ---------------------------
print(df["Age"].isnull().sum())
print(df["Age"].describe())
print(df[(df["Age"] < 0) | (df["Age"] > 120)])

# ---------------------------
#Standardize Gender values and replace missing entries
# ---------------------------
df["Gender"] = df["Gender"].replace({
    "Male": "M",
    "Female": "F",
    "0" : "M",
    "1" : "F"
})
df["Gender"] = df["Gender"].fillna("Unknown")
print(df["Gender"].value_counts(dropna=False))

# ---------------------------
# Appoinment Date column
# ---------------------------
df["Appointment_Date"] = pd.to_datetime(
    df["Appointment_Date"],
    format="mixed",
    errors="coerce"
)
print(df["Appointment_Date"].isnull().sum())

# ---------------------------
# Booking Date column
# ---------------------------
df["Booking_Date"]= pd.to_datetime(
    df["Booking_Date"],
    format="mixed",
    errors="coerce"
)
print(df["Booking_Date"].isnull().sum())

# ---------------------------
# Billing Amount column
# ---------------------------
print(df["Billing_Amount"].head(10))
print(df["Billing_Amount"].isnull().sum())
df["Billing_Amount"] = df["Billing_Amount"].str.replace(
    r"Rs|₹|\$|€|£|,",
    "",
    regex=True
)

df["Billing_Amount"] = pd.to_numeric(
    df["Billing_Amount"],
    errors="coerce"
)
print(df["Billing_Amount"].dtype)
df["Billing_Amount"] = df["Billing_Amount"].fillna(
    df["Billing_Amount"].mean()
)
df["Billing_Amount"] = df["Billing_Amount"].round(2)

# ---------------------------
# Follow Up column
# ---------------------------
df["Follow_Up"] = df["Follow_Up"].replace({
    "Y": "Yes",
    "N": "No",
    "0" : "No",
    "1" : "Yes"
})
df["Follow_Up"] = df["Follow_Up"].fillna("Unknown")
print(df.isnull().sum())


# ---------------------------
# Final Checking column
# ---------------------------
print("\nFinal Dataset Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nDataset Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

# ---------------------------
# Formating date and time columns 
# ---------------------------
df_to_save = df.copy()

df_to_save["Appointment_Date"] = df_to_save["Appointment_Date"].dt.strftime("%d/%m/%Y")
df_to_save["Booking_Date"] = df_to_save["Booking_Date"].dt.strftime("%d/%m/%Y")

# ---------------------------
# Saving The Code 
# ---------------------------
df_to_save.to_csv("Data/Cleaned_Dataset.csv", index=False)

