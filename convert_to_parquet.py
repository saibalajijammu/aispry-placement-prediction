import pandas as pd

df = pd.read_csv(
    "data/processed/feast_training_dataset.csv"
)
print(df["event_timestamp"].dtype)
df.to_parquet(
    "data/processed/feast_training_dataset.parquet",
    index=False
)

print("Parquet file created successfully!")