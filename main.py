# to print msg which function/operation starts performing
def function_start_msg(fun_name):
    function_name_msg = f" {fun_name} Function "
    print("\n" + function_name_msg.center(90, "*") + "\n")


# to print msg function/operation ends
def function_end_msg(fun_name):
    function_name_msg = f" {fun_name} Ends "
    print("\n" + function_name_msg.center(90, "*") + "\n")


# to verify user input data is valid or not default value set to none
def data_verification(Id=None, Name=None, RollNo=None, Contact=None):
    # roll no formatting eg SE-2020-053
    pattern = r"^SE-\d{4}-\d{3}$"

    if Id:
        if not (Id.isnumeric()):
            raise Exception("Invalid Id entered")
    if Name:
        name = Name.replace(" ", "")
        if not (name.isalpha()) or len(name) > 20:
            raise Exception("Invalid Name entered")

    if RollNo:
        if not (re.match(pattern, RollNo.upper())):
            raise Exception("Invalid Roll No format")

    if Contact:
        if not (Contact.isnumeric()) or len(Contact) != 11:
            raise Exception("Invalid Number entered")


# to display data of students
def view_record():
    function_start_msg("Fetching")
    # fetching all the records from the database
    get_query = "select Id, Name, RollNo, Contact from Students where IsDeleted = 0"
    sql_cursor.execute(get_query)
    records = sql_cursor.fetchall()

    # Creating heading
    headings = ["Id", "Name", "Roll No", "Contact"]
    heading = ("|" + headings[0].center(4, " ") +
               "|" + headings[1].center(20, " ") +
               "|" + headings[2].center(15, " ") +
               "|" + headings[3].center(13, " ") + "|")

    print("-" * len(heading))
    print(heading)
    print("-" * len(heading))

    # printing records from database
    for i in records:
        record = ("|" + str(i[0]).center(4, " ") +
                  "|" + i[1].center(20, " ") +
                  "|" + i[2].center(15, " ") +
                  "|" + i[3].center(13, " ") + "|")
        print(record)
    print("-".center(len(heading), '-'))
    function_end_msg("Fetching")


# to search any particular record
def search_record():
    function_start_msg("Searching")
    try:
        # Getting value to search
        option = int(input("Enter the following to search record:\n"
                           "By Id: 1\n"
                           "By Name: 2\n"
                           "By Roll No: 3\n"
                           "Enter you choice: "))
        # assigning key against user entered no
        var = {
            1: "Id",
            2: "Name",
            3: "RollNo"
        }
        key = var[option]
        value = input(f"Enter {key} to search record: ")

        if not value:
            raise Exception(f"{var[option]} not provided try again")

        data_verification(**{key: value})
        # fetching particular data
        search_query = "Select Id, Name, RollNo, Contact from Students where {} like %s" \
                       " and IsDeleted = 0 ".format(key)

        sql_cursor.execute(search_query, (value,))
        exist = sql_cursor.fetchone()
        if exist:
            print("Record found successful")
            print(exist)
            function_end_msg("Searching")
            return var[option], value
        else:
            print("Record not found")
            function_end_msg("Searching")
            return False

    except Exception as Error:
        print(Error)
        function_end_msg("Searching")


# to insert data in database
def insert_record():
    function_start_msg("Insertion")
    try:
        # getting following data from user
        print("Enter the following details")
        get_name = input("Full Name: ").title()
        get_roll_no = input("Roll No: ").upper()
        get_contact = input("Contact No: ")

        # validating user entered data
        data_verification(Name=get_name, RollNo=get_roll_no, Contact=get_contact)
        print("data verified")

        # Verifying if the given roll no already exist
        sql_query = "select RollNo from Students where RollNo = %s"
        value = (get_roll_no,)
        # Execution
        sql_cursor.execute(sql_query, value)
        exist = sql_cursor.fetchone()

        if exist:
            # alter message for user if record exist with the provided roll no
            query = "select Id, Name, RollNo, Contact, IsDeleted from Students where RollNo = %s"
            sql_cursor.execute(query, (get_roll_no.upper(),))
            get_details = sql_cursor.fetchone()

            # if recorde found in deleted
            if get_details[4] == 1:
                print("Roll No exist found following deleted record")
                print(get_details)
            else:
                print("Roll No exist found following active record")
                print(get_details)

            function_end_msg("Insertion")

        elif get_contact and get_name and get_roll_no:
            # if student doesn't exist add the student
            insert_query = "insert into Students (Name, RollNo, Contact) values (%s, %s, %s)"
            insert_values = (get_name.title(), get_roll_no.upper(), get_contact)
            # Execution
            sql_cursor.execute(insert_query, insert_values)
            mydb.commit()

            print(sql_cursor.rowcount, "Record inserted successful")
            function_end_msg("Insertion")

        else:
            print("Got null, Record insertion unsuccessful")
            function_end_msg("Insertion")

    except Exception as Error:
        print(Error)
        function_end_msg("Insertion")


# to delete any particular data
def delete_record():
    function_start_msg("Deletion")
    # to display all data
    view_record()
    # to fetch particular record and getting kry and value
    exist = search_record()

    if exist:
        try:
            confirmation = int(input("Enter 1 to confirm deletion else 0: "))
            if confirmation:
                delete_query = "update Students set IsDeleted = 1 where {} = %s".format(exist[0])
                value = exist[1]

                sql_cursor.execute(delete_query, (value,))
                mydb.commit()
                print("Record deleted successful")
                function_end_msg("deletion")

            else:
                print("Deletion unsuccessful")
                function_end_msg("Deletion")

        except Exception as delete_error:
            print(delete_error)
            function_end_msg("Deletion")


# to update any particular data
def update_record():
    function_start_msg("Updating")
    # fetching particular record
    exist = search_record()
    if exist:
        key = exist[0]
        value = exist[1]

        # fetching particular data if exist
        get_query = "select Id, Name, RollNo, Contact from Students where {} = %s".format(key)
        sql_cursor.execute(get_query, (value,))
        get_details = sql_cursor.fetchone()

        id = get_details[0]
        name = get_details[1]
        roll_no = get_details[2]
        contact = get_details[3]

        # getting values to update record
        get_name = input(f"To update ({name}) enter Name else press enter: ")
        if get_name:
            name = get_name.title()

        get_roll_no = input(f"To update ({roll_no}) enter Roll No else press enter: ")
        if get_roll_no:
            roll_no = get_roll_no.upper()

        get_contact = input(f"To update ({contact}) enter Contact else press enter: ")
        if get_contact:
            contact = get_contact

        # if any of the value entered update record else do not update
        if get_name or get_roll_no or get_contact:
            # verifying entered data
            try:
                data_verification(Name=name, RollNo=roll_no, Contact=contact)

                # updating data
                update_query = "update Students set Name = %s, RollNo = %s, Contact = %s where Id = %s"
                value = (name, roll_no, contact, id)
                sql_cursor.execute(update_query, value)
                mydb.commit()

                print(sql_cursor.rowcount, "updated successful")
                function_end_msg("Updating")

            except Exception as Error:
                print(Error)

                function_end_msg("Updating")

        else:
            print("No record updated")
            function_end_msg("Updating")

    else:
        function_end_msg("Updating")


# main file
if __name__ == "__main__":
    import mysql.connector
    import re

    # Creating SQL database connection
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="123Lakhani",
                                   database="test")
    # creating SQL cursor
    sql_cursor = mydb.cursor()

    function_start_msg("Welcome to Student Management System")
    while True:
        try:
            choice = int(input("To view record  : 1\n"
                               "To insert record: 2\n"
                               "To delete record: 3\n"
                               "To search record: 4\n"
                               "To update record: 5\n"
                               "To exit: 6\n"
                               "Enter no to perform desired operation: "))
        except Exception as E:
            print(E)
            msg = " Try Again "
            print()
            print(msg.center(90, "*"))
            print()
            continue

        if choice == 1:
            view_record()

        elif choice == 2:
            insert_record()

        elif choice == 3:
            delete_record()

        elif choice == 4:
            search_record()

        elif choice == 5:
            update_record()

        elif choice == 6:
            function_end_msg("Application")
            break

        # invalid data is entered
        else:
            print("Invalid choice")
            continue
