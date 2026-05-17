from datetime import timedelta
from feast import FeatureView, Field
from feast.types import Float32, Int64, String
from feast.infra.offline_stores.file_source import FileSource
from student_entity import student

student_source = FileSource(
    path="data/processed/feast_training_dataset.parquet",
    timestamp_field="event_timestamp",
)

student_features = FeatureView(
    name="student_features",
    entities=[student],
    ttl=timedelta(days=365),

    schema=[
    Field(name="student_id", dtype=Int64),

    Field(name="Age", dtype=Int64),
    Field(name="Gender", dtype=Int64),

    Field(name="CGPA", dtype=Float32),
    Field(name="Internships", dtype=Int64),

    Field(name="Coding_Skills", dtype=Int64),
    Field(name="Communication_Skills", dtype=Int64),

    Field(name="Backlogs", dtype=Int64),

    Field(name="Degree_B.Tech", dtype=Int64),
    Field(name="Degree_BCA", dtype=Int64),
    Field(name="Degree_MCA", dtype=Int64),

    Field(name="Branch_Civil", dtype=Int64),
    Field(name="Branch_ECE", dtype=Int64),
    Field(name="Branch_IT", dtype=Int64),
    Field(name="Branch_ME", dtype=Int64),
],

    source=student_source,
    online=True,
)