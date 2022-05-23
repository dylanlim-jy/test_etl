from prefect import Flow
from prefect.schedules import CronSchedule

from functions import extract, write

def build_flow():
    schedule = CronSchedule("0-59 * * * *")

    with Flow("test-flow", schedule=schedule) as flow:
        data = extract()
        output = write(data)
        return flow 

if __name__ == "__main__":
    flow = build_flow()
    flow.register(project_name="test etl")
