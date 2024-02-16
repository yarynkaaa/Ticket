import json
import mysql.connector

def bd_connect():
    config = get_config()

    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["passwd"],
        database=config["db-name"]
    )
    
    return connection

def get_config():

    with open("config.json", "r") as file:
        json_as_string = file.read()
        json_config = json.loads(json_as_string)
        return json_config