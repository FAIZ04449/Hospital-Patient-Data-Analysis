import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("hospital_data.csv")

print("=== Dataset Preview ===")
print(df.head())

# -----------------------------
# 1. Disease Frequency
# -----------------------------
disease_count = df['disease'].value_counts()
print("\n=== Disease Frequency ===")
print(disease_count)

# -----------------------------
# 2. Treatment Cost Statistics
# -----------------------------
print("\n=== Treatment Cost Statistics ===")
print(df['treatment_cost'].describe())

# -----------------------------
# 3. Doctor Workload
# -----------------------------
doctor_group = df['doctor'].value_counts()
print("\n=== Doctor Workload ===")
print(doctor_group)

# -----------------------------
# 4. Pie Chart (Disease Distribution)
# -----------------------------
plt.figure()
disease_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Disease Distribution")
plt.ylabel('')
plt.savefig("screenshots/pie_chart.png")
plt.show()

# -----------------------------
# 5. Bar Chart (Doctor Workload)
# -----------------------------
plt.figure()
doctor_group.plot(kind='bar')
plt.title("Doctor Workload")
plt.xlabel("Doctor")
plt.ylabel("Number of Patients")
plt.savefig("screenshots/bar_chart.png")
plt.show()