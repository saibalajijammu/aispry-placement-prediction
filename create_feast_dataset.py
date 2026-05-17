import pandas as pd

raw_df = pd.read_csv(
    "data/raw/students.csv"
)

processed_df = pd.read_csv(
    "data/processed/training_dataset.csv"
)

processed_df.insert(
    0,
    "student_id",
    raw_df["Student_ID"]
)

processed_df["event_timestamp"] = pd.Timestamp.now()

print(processed_df["event_timestamp"].dtype)

processed_df.to_parquet(
    "data/processed/feast_training_dataset.parquet",
    index=False
)

print("Feast dataset created successfully!")