from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job
from uuid import uuid4
from datetime import datetime

client = OpenLineageClient("http://localhost:5000")

event = RunEvent(
    eventType=RunState.START,
    eventTime=datetime.utcnow().isoformat() + "Z",

    run=Run(
        runId=str(uuid4())
    ),

    job=Job(
        namespace="aispry",
        name="training_pipeline"
    ),

    producer="https://github.com/OpenLineage/OpenLineage"
)

client.emit(event)

print("Lineage event sent successfully")