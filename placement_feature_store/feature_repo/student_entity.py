from feast import Entity
from feast.types import ValueType 

student = Entity(
    name="student_id",
    join_keys=["student_id"],
    value_type=ValueType.INT64,
)