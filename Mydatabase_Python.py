import mysql.connector
from mysql.connector import errorcode

# Connect to the MySQL database
def connect():
    con = None
    err_msg = ""
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='mydatabase'  # Change this to your database name
        )
        print("Connection Successful")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            err_msg = "Something is wrong with your Username/Password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            err_msg = "Database does not exist"
        else:
            err_msg = str(err)
    
    return con, err_msg

# Add a new record to the appropriate table
def add(con):
    cursor = con.cursor()
    student_type = input("Enter student type (T for Transferee, A for Admitted, S for Shifter): ").upper()

    if student_type == 'T':
        table_name = 'transfer_students'
    elif student_type == 'A':
        table_name = 'admitted_students'
    elif student_type == 'S':
        table_name = 'shifters'
    else:
        print("Invalid student type. Please enter T, A, or S.")
        return

    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    middle_name = input("Enter Middle Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    year = int(input("Enter Year: "))
    
    # Execute SQL to insert data into the appropriate table
    sql = f"INSERT INTO {table_name} (last_name, first_name, middle_name, age, course, year) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (last_name, first_name, middle_name, age, course, year)
    
    cursor.execute(sql, val)
    con.commit()
    
    print("Record Saved")
    cursor.close()
    
# Search for a record in the appropriate table
def search(con):
    cursor = con.cursor()
    student_type = input("Enter student type (T for Transferee, A for Admitted, S for Shifter): ").upper()

    if student_type == 'T':
        table_name = 'transfer_students'
    elif student_type == 'A':
        table_name = 'admitted_students'
    elif student_type == 'S':
        table_name = 'shifters'
    else:
        print("Invalid student type. Please enter T, A, or S.")
        return

    code_to_search = int(input("Enter Student Code to Search: "))
    sql = f"SELECT * FROM {table_name} WHERE student_code = %s"
    cursor.execute(sql, (code_to_search,))
    records = cursor.fetchall()

    if not records:
        print(f"No record found with Student Code {code_to_search}")
    else:
        print("Record(s) Found:")
        for record in records:
            print(record)
    cursor.close()

# Update a record in the appropriate table
def update(con):
    cursor = con.cursor()
    student_type = input("Enter student type (T for Transferee, A for Admitted, S for Shifter): ").upper()

    if student_type == 'T':
        table_name = 'transfer_students'
    elif student_type == 'A':
        table_name = 'admitted_students'
    elif student_type == 'S':
        table_name = 'shifters'
    else:
        print("Invalid student type. Please enter T, A, or S.")
        return

    code_to_update = int(input("Enter Student Code to Update: "))

    print("Select fields to update:")
    print("1. Last Name")
    print("2. First Name")
    print("3. Middle Name")
    print("4. Age")
    print("5. Course")
    print("6. Year")
    print("0. Skip Update")

    fields_to_update = input("Enter field numbers to update (comma-separated): ").split(',')

    update_values = {}
    if '1' in fields_to_update:
        update_values['last_name'] = input("Enter New Last Name: ")
    if '2' in fields_to_update:
        update_values['first_name'] = input("Enter New First Name: ")
    if '3' in fields_to_update:
        update_values['middle_name'] = input("Enter New Middle Name (optional): ")
    if '4' in fields_to_update:
        update_values['age'] = int(input("Enter New Age: "))
    if '5' in fields_to_update:
        update_values['course'] = input("Enter New Course: ")
    if '6' in fields_to_update:
        update_values['year'] = int(input("Enter New Year: "))

    if not update_values or '0' in fields_to_update:
        print("No fields selected for update or skip update selected.")
        return

    # Construct the SQL update query based on the selected fields
    sql_update_parts = []
    val = []
    for field, value in update_values.items():
        sql_update_parts.append(f"{field} = %s")
        val.append(value)
    val.append(code_to_update)  # Add student code for WHERE clause

    sql_update_query = f"UPDATE {table_name} SET {', '.join(sql_update_parts)} WHERE student_code = %s"

    # Execute SQL to update data in the appropriate table
    cursor.execute(sql_update_query, val)
    con.commit()

    print("Record Updated")
    cursor.close()

# Delete a record from the appropriate table
def delete(con):
    cursor = con.cursor()
    student_type = input("Enter student type (T for Transferee, A for Admitted, S for Shifter): ").upper()

    if student_type == 'T':
        table_name = 'transfer_students'
    elif student_type == 'A':
        table_name = 'admitted_students'
    elif student_type == 'S':
        table_name = 'shifters'
    else:
        print("Invalid student type. Please enter T, A, or S.")
        return

    code_to_delete = int(input("Enter Student Code to Delete: "))
    
    # Execute SQL to delete data from the appropriate table
    sql = f"DELETE FROM {table_name} WHERE student_code = %s"
    val = (code_to_delete,)
    
    cursor.execute(sql, val)
    con.commit()
    
    print("Record Deleted")
    cursor.close()

# Shows all records in the appropriate table
def show_all_records(con):
    cursor = con.cursor()
    student_type = input("Enter student type (T for Transferee, A for Admitted, S for Shifter): ").upper()

    if student_type == 'T':
        table_name = 'transfer_students'
    elif student_type == 'A':
        table_name = 'admitted_students'
    elif student_type == 'S':
        table_name = 'shifters'
    else:
        print("Invalid student type. Please enter T, A, or S.")
        return

    sql = f"SELECT * FROM {table_name}"
    cursor.execute(sql)
    records = cursor.fetchall()

    if not records:
        print("No records found.")
    else:
        print("All Records:")
        for record in records:
            print(record)
    cursor.close()

# Main menu for CRUD operations
def main_menu(con):
    while True:
        print("\nMain Menu:")
        print("1. Add a new record")
        print("2. Search for a record")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Show all records")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            print(" ")
            add(con)
        elif choice == '2':
            print(" ")
            search(con)
        elif choice == '3':
            print(" ")
            update(con)
        elif choice == '4':
            print(" ")
            delete(con)
        elif choice == '5':
            print(" ")
            show_all_records(con)
        elif choice == '6':
            print(" ")
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Example usage
connection, err_message = connect()
if connection:
    main_menu(connection)
else:
    print(err_message)
