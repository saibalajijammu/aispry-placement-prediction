import pandas as pd
import great_expectations as gx

# Load dataset
df = pd.read_csv("data/processed/training_dataset.csv")

# Create GX dataframe
gx_df = gx.from_pandas(df)

# Expectations
gx_df.expect_column_values_to_not_be_null("CGPA")
gx_df.expect_column_values_to_not_be_null("Age")
gx_df.expect_column_values_to_not_be_null("Placement_Status")

gx_df.expect_column_values_to_be_between(
    "CGPA",
    min_value=0,
    max_value=10
)

gx_df.expect_column_values_to_be_between(
    "Age",
    min_value=18,
    max_value=23
)

gx_df.expect_column_values_to_be_in_set(
    "Placement_Status",
    [0, 1]
)

# Validate
results = gx_df.validate()

print(results)