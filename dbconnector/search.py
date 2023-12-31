import mysql.connector

def search_item(table_name, records):

    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        filtered_records = {key: value for key, value in records.items() if value != ''}
        condition = ' AND '.join([f"{key}='{value}'" for key, value in filtered_records.items()])
        query1 = f"SELECT * FROM {table_name} WHERE {condition}"
        cursor.execute(query1)
        rows = cursor.fetchall()
        data = [row for row in rows]

        query2 = f"DESCRIBE {table_name}"
        cursor.execute(query2)
        columns = cursor.fetchall()
        column = [col[0] for col in columns]



        return data, column

    except mysql.connector.Error as error:
        return error