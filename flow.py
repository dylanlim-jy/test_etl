from prefect import Flow
from prefect.schedules import CronSchedule

from functions import extract, write

def build_flow():
    """Creates and returns a Flow object. To run this file as a background process (pseudo-daemon),
    1. SSH into remote server
    2. cd into the right directory
    3. Activate venv: `source venv/bin/activate`
    4. Register the flow if not registered already: `python3 flow.py`
    5. Run the Prefect agent using nohup: `sudo nohup prefect agent local start`
    6. Exit terminal
    
    To kill the process:
    1. Find the PID: `ps ax | grep prefect`
    2. `kill pid`
    """
    schedule = CronSchedule("0-59 * * * *")

    with Flow("test-flow", schedule=schedule) as flow:
        data = extract()
        output = write(data)
        return flow 

if __name__ == "__main__":
    flow = build_flow()
    flow.register(project_name="test etl")
