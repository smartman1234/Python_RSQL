import mysql.connector
import csv

class Connect:
    def __init__(self, host, user, password, database, port):
        self.db = mysql.connector.connect(
            host="localhost",
            user="simplerisk",
            password="simplerisk",
            database="simplerisk",
            port="3307"
        )
        self.cursor = self.db.cursor()

    def get_tables(self):
        tables_query = ("Show Tables")
        self.cursor.execute(tables_query)

        tables = []
        for table in self.cursor:
            tables.append(table[0])
        
        return tables
    
    def get_schema(self, table_name):
        schema_query = (f"DESCRIBE {table_name}")
        self.cursor.execute(schema_query)

        schema = []
        results = self.cursor.fetchall()
        for row in results:
            schema.append(row[0])
        return(schema)
    
    def get_data(self, table_name):
        schema = self.get_schema(table_name)

        fetch_query = (f"SELECT * FROM {table_name}")
        self.cursor.execute(fetch_query)
        
        data = []
        results = self.cursor.fetchall()
        for row in results:
            data.append(row)
        return(data)
    
    def csv_write(self, table_name, file_name):
        data = self.get_data(table_name)
        schema = self.get_schema(table_name)
        with open(file_name, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(schema)
            for row in data:
                writer.writerow(row)
            writer.writerow([])
    
    def csv_erase(self, file_name):
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerow([])
    
    def csv_write_tables(self, file_name):
        self.csv_erase(file_name)
        tables = self.get_tables()
        for table in tables:
            self.csv_write(table, file_name)


    def close(self):
        self.cursor.close()
        self.db.close()


db = Connect("localhost", "simplerisk", "simplerisk", "simplerisk", "3307")

db.csv_write_tables("1.csv")
db.close()




