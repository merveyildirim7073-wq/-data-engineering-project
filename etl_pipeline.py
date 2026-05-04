import pandas as pd

# Extract
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [5000, 6000, 7000]
}

df = pd.DataFrame(data)

# Transform
df["salary_with_bonus"] = df["salary"] * 1.10

# Load
df.to_csv("output.csv", index=False)

print("ETL process completed successfully!")
