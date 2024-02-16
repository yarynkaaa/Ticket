import mysql.connector
from functions import *
from initial_config import *

def main():

    config = get_config()

    try: 
        connection = bd_connect()
        
    except mysql.connector.errors.ProgrammingError:

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            passwd=config["passwd"],
        )

        initialize_db(connection)
        connection = bd_connect()
    


if __name__ == "__main__":
    main()