import pandas as pd

df = pd.read_parquet(
    "data/processed/feast_training_dataset.parquet"
)

print(df.columns)