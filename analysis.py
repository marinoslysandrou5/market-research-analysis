import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Basic info
print("Dataset Info:")
print(df.info())

# Average satisfaction
avg_sat = df["Satisfaction"].mean()
print(f"\nAverage Satisfaction: {avg_sat:.2f}")

# Satisfaction by Gender
gender_sat = df.groupby("Gender")["Satisfaction"].mean()
print("\nSatisfaction by Gender:")
print(gender_sat)

# Recommendation rate
recommend_rate = df["Recommend"].value_counts(normalize=True) * 100
print("\nRecommendation Rate (%):")
print(recommend_rate)

# Plot
plt.figure()
gender_sat.plot(kind="bar", title="Satisfaction by Gender")
plt.ylabel("Satisfaction Score")
plt.xlabel("Gender")
plt.tight_layout()
plt.savefig("satisfaction_by_gender.png")

print("\nPlot saved as satisfaction_by_gender.png")