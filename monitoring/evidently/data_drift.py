import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Load datasets
reference_data = pd.read_csv("data/processed/training_dataset.csv")

# Simulated production data
current_data = reference_data.sample(frac=0.5).copy()

# Create report
report = Report(metrics=[
    DataDriftPreset()
])

# Run report
my_eval = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save HTML
my_eval.save_html("monitoring/evidently/data_drift_report.html")

print("Data drift report generated successfully!")