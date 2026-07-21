"""
Clinic Appointment Exploratory Data Analysis (EDA)

Description:
This script performs exploratory data analysis on the cleaned
clinic appointment dataset using Pandas, Matplotlib, and Seaborn.
It generates visualizations to identify patterns, trends, and
insights from the data.

Author: Priyansh Dangwal
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data/Cleaned_Dataset.csv")

# Convert date columns back to datetime for analysis
df["Appointment_Date"] = pd.to_datetime(
    df["Appointment_Date"],
    format="%d/%m/%Y"
)
df["Booking_Date"] = pd.to_datetime(
    df["Booking_Date"],
    format="%d/%m/%Y"
)

#Saving the file 
def save_plot(filename):
    plt.savefig(
        f"Graphs/{filename}",
        dpi=300,
        bbox_inches="tight"
    )

# ---------------------------
# Dataset Overview
# ---------------------------

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
df.info()

print("\nStatistical Summary (Numerical)")
print(df.describe())

print("\nStatistical Summary (Categorical)")
print(df.describe(include="object"))

print("\nDataset Shape")
print(df.shape)

print("\nUnique Values")
print(df.nunique())

print("\nMissing Values")
print(df.isnull().sum())

# ---------------------------
# Age Distribution
# ---------------------------

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="Age",
    bins=10,
    kde=True
)

plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Number of Patients")

save_plot("age_distribution.png")
plt.show()


# ---------------------------
# Gender Distribution
# ---------------------------

plt.figure(figsize=(6,5))

ax= sns.countplot(
    data=df,
    x="Gender",
    hue="Gender",
    legend=False
)
for container in ax.containers:
    ax.bar_label(container)

plt.title("Gender Distribution of Patients")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")

save_plot("gender_distribution.png")
plt.show()


# ---------------------------
# Department Distribution
# ---------------------------

plt.figure(figsize=(8,5))

ax = sns.countplot(
    data=df,
    y="Department",
    hue="Department",
    legend=False,
    order=df["Department"].value_counts().index
)

for container in ax.containers:
    ax.bar_label(container)

plt.title("Patient Distribution by Department")
plt.xlabel("Number of Patients")
plt.ylabel("Department")

save_plot("department_distribution.png")
plt.show()


# ---------------------------
# Billing Amount Distribution
# ---------------------------

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="Billing_Amount",
    bins=10,
)

plt.title("Distribution of Billing Amount")
plt.xlabel("Billing Amount")
plt.ylabel("Number of Patients")

save_plot("billing_distribution.png")
plt.show()

# ---------------------------
# Billing Amount Boxplot
# ---------------------------

plt.figure(figsize=(8,4))

sns.boxplot(
    x=df["Billing_Amount"]
)

plt.title("Boxplot of Billing Amount")

save_plot("billing_amount_boxplot.png")
plt.show()

# ---------------------------
# Follow-up Distribution
# ---------------------------

plt.figure(figsize=(6,5))

ax = sns.countplot(
    data=df,
    x="Follow_Up",
    hue="Follow_Up",
    legend=False
)

for container in ax.containers:
    ax.bar_label(container)

plt.title("Follow-up Requirement Distribution")
plt.xlabel("Follow-up Required")
plt.ylabel("Number of Patients")

save_plot("follow_up_distribution.png")
plt.show()

# ---------------------------
# Average Billing Amount by Department
# --------------------------- 

plt.figure(figsize=(8,5))
ax = sns.barplot(
    data = df,
    x= "Department",
    y = "Billing_Amount",
    estimator ="mean",
    errorbar= None
)

for container in ax.containers:
    ax.bar_label(container , fmt = "%.2f")

plt.title(" Average Billing Amount by Department")
plt.xlabel("Department")
plt.ylabel("Average Billing Amount")

save_plot("billing_by_department.png")
plt.show()


# ---------------------------
# Patient Age vs Billing Amount
# ---------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Age",
    y="Billing_Amount"
)

plt.title("Age vs Billing Amount")
plt.xlabel("Age")
plt.ylabel("Billing Amount")

save_plot("age_vs_billing_amount.png")
plt.show()


# ---------------------------
# Appointments by Month
# ---------------------------

df["Month"] = df["Appointment_Date"].dt.month_name()

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

plt.figure(figsize=(10,5))

ax = sns.countplot(
    data=df,
    x="Month",
    order=month_order,
    hue="Month",
    legend=False
)

for container in ax.containers:
    ax.bar_label(container)

plt.title("Appointments by Month")
plt.xlabel("Month")
plt.ylabel("Number of Appointments")

plt.xticks(rotation=45)

save_plot("appointments_by_month.png")
plt.show()


# ---------------------------
# Appointments by Weekday
# ---------------------------

df["Weekday"] = df["Appointment_Date"].dt.day_name()

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

plt.figure(figsize=(8,5))

ax = sns.countplot(
    data=df,
    x="Weekday",
    order=weekday_order,
    hue="Weekday",
    legend=False
)

for container in ax.containers:
    ax.bar_label(container)

plt.title("Appointments by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Number of Appointments")

plt.xticks(rotation=20)

save_plot("appointments_by_weekday.png")
plt.show()


# ---------------------------
# Correlation Heatmap
# ---------------------------

plt.figure(figsize=(6,4))

correlation = df[["Age", "Billing_Amount"]].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

save_plot("correlation_heatmap.png")
plt.show()