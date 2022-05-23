import datetime 
import csv
import json
import requests
from prefect import task 

@task
def extract():
    """Sends a GET request to xMath API and returns a mathematical expression.
    More information at https://x-math.herokuapp.com/"""
    r = requests.get("https://x-math.herokuapp.com/api/random")
    expression = json.loads(r.text)['expression']
    answer = json.loads(r.text)['answer']

    output = str(expression) + " = " + str(answer) + " | " + str(datetime.datetime.now())
    print(output)
    return output

@task
def write(line):
    """Writes a single-line input into an output csv
    Returns None"""
    
    with open('output.csv', 'a', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        writer.writerow([line])
    return