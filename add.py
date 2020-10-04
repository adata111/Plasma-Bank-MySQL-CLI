"""
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
"""


def newUser(cur,con,login):
    
    row={}
    row["Password"] = input("Login Password: ")
    row["Contact"] = int(input("Contact Number: "))
    row["Address"] = input("Address: ")

    query = "INSERT INTO USER(Login_id, Password, Contact, Address) VALUES('%s', '%s', '%d', '%s')" % (
            login, row["Password"], row["Contact"], row["Address"])

#    print(query)
    cur.execute(query)
    con.commit()


def hireStaff(cur,con):
    try:
        row = {}
        print("Enter new staff's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["Login_id"] = "STAFF"+row["Staff_id"]
        newUser(cur,con,row["Login_id"])
        
        row["doj"] = input("Date of joining (YYYY-MM-DD): ")
        row["Salary"] = float(input("Salary: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["sup"] = input("Supervisor staff ID: ")

        if row["sup"]=='' or row["sup"]=='NULL':
            row["sup"]='NULL'
        else:
            row["sup"]= "'"+row["sup"]+"'"
        
        query = "INSERT INTO STAFF(First_name, Last_name, Staff_id, Birth_date, Salary, Date_of_joining, Supervisor, Login_id, Age) VALUES('%s', '%s', '%s', '%s', %f, '%s', %s, '%s', 28)" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["Bdate"], row["Salary"], row["doj"], row["sup"], row["Login_id"])

        print(query)
        cur.execute(query)
        con.commit()

        skills = (input("Skills (comma separated): ")).split(',')
        for skill in skills:
            query = "INSERT INTO STAFF_SKILLS(Staff_id,Skills) VALUES('%s','%s')"%(row["Staff_id"],skill)
            cur.execute(query)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addDonor(cur,con):
    try:
        row = {}
        print("Enter new donor's details: ")
        row["Donor_id"] = input("Donor ID: ")
        row["name"] = (input("Name (Fname Lname): "))
        row["Login_id"] = "DONOR"+row["Donor_id"]
        newUser(cur,con,row["Login_id"])
        
        row["aadhar"] = int(input("Aadhar Number: "))
        row["Blood_type"] = input("Blood Type (A+/-,B+/-,O+/-,AB+/-): ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["noDon"] = int(input("Number of donations: "))

        query = "INSERT INTO DONOR(Name, Donor_id, Birth_date, Number_of_donations, Blood_type, Aadhar_num, Login_id, Age) VALUES('%s', '%s', '%s', %d, '%s', %d, '%s', 28)" % (
            row["name"], row["Donor_id"], row["Bdate"], row["noDon"], row["Blood_type"], row["aadhar"], row["Login_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addDep(cur,con):
    try:
        row = {}
        print("Enter new dependent's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["gend"] = input("Gender (F,M,T,O): ")
        row["rel"] = input("Relationship: ")
        row["age"] = int(input("Age: "))

        query = "INSERT INTO DEPENDENT(First_name, Last_name, Staff_id, Gender, Relationship, Age) VALUES('%s', '%s', '%s', '%c', '%s', '%d')" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["gend"], row["rel"], row["age"])

        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    
def addVehi(cur,con):
    try:
        row = {}
        print("Enter new vehicle's details: ")
        row["Vehicle_id"] = input("Vehicle ID: ")
        row["Vehicle_type"] = input("Vehicle_type (HCV, LCV, Two-wheeler, Car): ")
        row["Availability"] = int(input("Vehicle Availability (1, 0): "))
        row["Deliveries"] = int(input("Number of deliveries: "))
        row["Department_id"] = input("Department_id: ")

        query = "INSERT INTO LOGISTICS(Vehicle_id, Vehicle_type, Availability, Deliveries, Department_id) VALUES('%s', '%s', %d, %d, '%s')" % (
            row["Vehicle_id"], row["Vehicle_type"], row["Availability"], row["Deliveries"], row["Department_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addPlasma(cur, con):
    try:
        row = {}
        print("Enter plasma details: ")
        row["Donor_id"] = input("Donor ID: ")
        row["Donation_date"] = input("Donation date: ")
        row["Sample_no"] = int(input("Sample number (1, 2): "))
        
        query1 = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE Vacancy>0"

        if cur.execute(query1)==0:
            con.commit()
            print("Add an inventory with vacancy first")
            return

        inventory_id = cur.fetchall()[0][0]
        query = "INSERT INTO PLASMA(Donor_id, Donation_date, Sample_no, Used, Inventory_id) VALUES('%s', '%s', %d, 0, '%s')" % (
            row["Donor_id"], row["Donation_date"], row["Sample_no"], inventory_id)

        print(query)
        cur.execute(query)
        con.commit()


        #updating inventory
        que = "SELECT Blood_type FROM DONOR WHERE Donor_id LIKE '%s'" % (row["Donor_id"])     
        if cur.execute(que):
            btype = cur.fetchall(que)

        if btype == "A+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Aplus = No_of_Aplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "A-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Aminus = No_of_Aminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "B+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Bplus = No_of_Bplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "B-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Bminus = No_of_Bminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "O+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Oplus = No_of_Oplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "O-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Ominus = No_of_Ominus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "AB+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_ABplus = No_of_ABplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "AB-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_ABminus = No_of_ABminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        
        cur.execute(quer)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addInventory(cur, con):
    try:
        row = {}
        print("Enter new plasma inventory details: ")
        row["Inventory_id"] = input("Inventory ID:")
        row["Capacity"] = int(input("Capacity: "))

        query = "INSERT INTO PLASMA_INVENTORY(No_of_Aplus, No_of_Aminus, No_of_Bplus, No_of_Bminus, No_of_ABplus, No_of_ABminus, No_of_Oplus, No_of_Ominus,Capacity,Vacancy,Department_id, Inventory_id) VALUES(0, 0, 0, 0, 0,0,0,0,%d,%d,'DPI','%s')" % (
            row["Capacity"], row["Capacity"], row["Inventory_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def placeOrder(cur,con):
    try:
        row = {}
        print("Enter details to place order: ")
        row["Hospital_id"] = input("Hospital ID:")
        row["name"] = (input("Hospital Name: "))
        row["dist"] = float(input("Hospital Distance from plasma bank: "))
        row["Login_id"] = "HOSP"+row["Hospital_id"]
        newUser(cur,con,row["Login_id"])
        
        query = "INSERT INTO HOSPITAL(Hospital_id,Hospital_name,Distance,Login_id) VALUES('%s','%s',%f,'%s')"%(
            row["Hospital_id"], row["name"], row["dist"], row["Login_id"])
        cur.execute(query)
        con.commit()

        row["Patient_id"] = input("Patient ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["Blood_type"] = input("Blood Type (A+/-,B+/-,O+/-,AB+/-): ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")

        query = "INSERT INTO PATIENT(First_name, Last_name, Patient_id, Birth_date, Hospital_id, Blood_type, Age) VALUES('%s', '%s', '%s', '%s', '%s', '%s', 28)" % (
            row["Fname"], row["Lname"], row["Patient_id"], row["Bdate"], row["Hospital_id"], row["Blood_type"])

        print(query)
        cur.execute(query)
        con.commit()

        row["Order_id"] = input("Order ID:")
        row["Order_date"] = (input("Order date: "))
        uery = "INSERT INTO ORDER_REQUEST(Order_id, Vehicle_id, Order_date, Hospital_id, Blood_type, Accepted, Distance, Donor_id) VALUES('%s', NULL, '%s', '%s', '%s', 0, %f, NULL)" % (
            row["Order_id"], row["Order_date"], row["Hospital_id"], row["Blood_type"], row["dist"])

        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
