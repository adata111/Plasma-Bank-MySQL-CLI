def updateStaff(cur,con):
	
	try:
		value=0
		row = {}
		
		while(value==0):
			row["sid"] = input("Enter Staff_id of staff whose details you wish to update: ")
			que = "SELECT * FROM STAFF WHERE Staff_id LIKE '%s'" % (row["sid"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid Staff_id")
			con.commit()
        #row = {}
        #print("Enter new staff's details: ")
        #row["Staff_id"] = input("Staff ID: ")
        #update
		print("Do you want to edit the following field? ")
		cha = int(input("First name (1/0) : "))
		if cha == 1:
			row["Newfname"] = input("Enter new First name : ")
			query = "UPDATE STAFF SET First_name = '%s' WHERE Staff_id LIKE '%s'" % (row["Newfname"], row["sid"])
			#value=cur.execute(query)
			
			#print(value)
			con.commit()
		else:
			print("")
		cha = int(input("Last name (1/0) : "))
		if cha == 1:
			row["Newlname"] = input("Enter new Last name : ")
			query = "UPDATE STAFF SET Last_name = '%s' WHERE Staff_id LIKE '%s'" % (row["Newlname"], row["sid"])
			cur.execute(query)
			con.commit()
		else:
			print("")
		cha = int(input("Birth date (1/0) : "))
		if cha == 1:
			row["Newbd"] = input("Enter new Birth date : ")
			query = "UPDATE STAFF SET Birth_date = '%s', Age = 28 WHERE Staff_id LIKE '%s'" % (row["Newbd"], row["sid"])
			cur.execute(query)
			con.commit()
		else:
			print("")
		cha = int(input("Salary (1/0) : "))
		if cha == 1:
			row["Newsal"] = float(input("Enter new Salary : "))
			query = "UPDATE STAFF SET Salary = '%f' WHERE Staff_id LIKE '%s'" % (row["Newsal"], row["sid"])
			cur.execute(query)
			con.commit()
		else:
			print("")
		cha = int(input("Date of joining (1/0) : "))
		if cha == 1:
			row["Newdoj"] = input("Enter new Date of joining : ")
			query = "UPDATE STAFF SET Date_of_joining = '%s' WHERE Staff_id LIKE '%s'" % (row["Newdoj"], row["sid"])
			cur.execute(query)
			con.commit()
		else:
			print("")
		cha = int(input("Supervisor (1/0) : "))
		if cha == 1:
			row["Newsup"] = input("Enter new Supervisor : ")
			if row["Newsup"]=='' or row["Newsup"]=='NULL':
				row["Newsup"]='NULL'
			else:
				row["Newsup"]= "'"+row["Newsup"]+"'"
			query = "UPDATE STAFF SET Supervisor = '%s' WHERE Staff_id LIKE '%s'" % (row["Newsup"], row["sid"])
			cur.execute(query)
			con.commit()
		else:
			print("")
        #ch = int(input("Staff skills (1/0) : "))  
        
		print("Updated Database")

	except Exception as e:
		con.rollback()
		print("Failed to update staff")
		print(">>>>>>>>>>>>>", e)

	return


def updateVehAv(cur,con):
		
	try:
		value=0
		row = {}
			
		while(value==0):
			row["vid"] = input("Enter vehicle id of vehicle where availability needs to be changed: ")
			que = "SELECT * FROM LOGISTICS WHERE Vehicle_id LIKE '%s'" % (row["vid"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid vehicle id")
			con.commit()			
		cha = bool(input("Enter new availability (1/0): "))
		query = "UPDATE LOGISTICS SET Availability = '%b' WHERE Vehicle_id LIKE '%s'" % (cha, row["vid"])
		cur.execute(query)
		con.commit()	        
		print("Updated Database")

	except Exception as e:
			con.rollback()
			print("Failed to update staff")
			print(">>>>>>>>>>>>>", e)

	return