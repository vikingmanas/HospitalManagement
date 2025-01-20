import mysql.connector
from mysql.connector import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")

def main():
    try:
        
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="qwert67890p"  
        )

        if connection.is_connected():
            print("Connected to MySQL Server")

            
            execute_query(connection, "CREATE DATABASE IF NOT EXISTS hospital_management_system;")
            execute_query(connection, "USE hospital_management_system;")

            
            tables = [
                """
                CREATE TABLE IF NOT EXISTS physician (
                  employeeid INT PRIMARY KEY,
                  name VARCHAR(20),
                  position VARCHAR(50),
                  ssn INT
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS department (
                  departmentid INT PRIMARY KEY, 
                  name VARCHAR(20), 
                  head INT
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS affiliated_with (
                  physicianid INT, 
                  departmentid INT, 
                  primary_affiliation VARCHAR(5),
                  FOREIGN KEY (physicianid) REFERENCES physician(employeeid),
                  FOREIGN KEY (departmentid) REFERENCES department(departmentid)
                );
                """,
               
            ]

            for table_query in tables:
                execute_query(connection, table_query)

            insert_data_queries = [
                """
                INSERT INTO physician(employeeid, name, position, ssn) VALUES
                (1, 'John Dorian', 'Staff Internist', 111111111),
                (2, 'Elliot Reid', 'Attending Physician', 222222222),
                (3, 'Christopher Turk', 'Surgical Attending Physician', 333333333),
                (4, 'Percival Cox', 'Senior Attending Physician', 444444444);
                """,
                """
                INSERT INTO department VALUES
                (1, 'General Medicine', 4),
                (2, 'Surgery', 7),
                (3, 'Psychiatry', 9);
                """,
                
            ]

            for data_query in insert_data_queries:
                execute_query(connection, data_query)

            print("Database setup and data insertion completed successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    main()
