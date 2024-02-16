import json
from functions import get_config

def initialize_db(connection):
    db_cursor = connection.cursor()

    config = get_config()
    
    db_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config["db-name"]}")
    
    #db_cursor.execute("CREATE TABLE events (name VARCHAR(50), description VARCHAR(1250), price_children smallint(255), price_adults smallint(255), bought_children smallint(255), bought_adult smallint(255), capacity smallint(255) );")
