#!/usr/bin/env python3
# date: 14 October 2020
# demo code





# The below code is a demonstration of how to keep track of the attributes of each table in a database. The table names and their numbers of attributes are stored in a dictionary (tables_dict). Remember, for an INSERT, you will need to know each piece of information for each attribute of a table.

# Note: this example code uses the table names from our campus database from class. In this assignment, you are to use your own database and so you will be changing the this code to match your database.

tables_dict = {"instructor": 5,
"teaches":5,
"student": 4,
"course": 4,
"department": 3
}

# Define a function to get user input for the name of the table
def getTableName():
	"""Function to get the table name from the user"""
	# show the tables
	print("\n\t [+] Tables to choose:\n")
	for i in tables_dict:
		print(f"\t\t {i}")
	print(" ") # drop a line

	# get user table selection
	prmpt_str = "\t Enter table name: "
	tableToEdit = input(prmpt_str) # enter input
	tableToEdit = tableToEdit.lower() # put text in to lower case

	# check to see that the selected table is contained in tables_dict
	while(tableToEdit not in tables_dict):
		print(f"\t [-] No such table, <{tableToEdit}> in dictionary. Please re-enter the name.")
		tableToEdit = input(prmpt_str) # enter input
		tableToEdit = tableToEdit.lower() # put text in to lower case

	return tableToEdit
# end of getTableName()

def userMenu():
	""" A simple menu system to help users select options"""
	prmpt_str = "\t Enter an integer 1, 2 or 3 :"
	result_int = int(input(prmpt_str))
	# note input() returns strings, so we convert string to int here.

	options_list = [1,2,3] # list of available menu items
	while result_int not in options_list:
		print(f"\t [-] Option <{result_int}> not found. Please try again.")
		result_int = int(input(prmpt_str))
	if result_int == 1:
		function1() # call this function if result_int is 1
	elif result_int == 2:
		function2() # call this function if result_int is 2
	else:
		function3() # call this function if result_int is not 1 and not 2.
	return result_int
	#end of userMenu()

def function1():
	""" print a welcome message for option 1"""
	print("\n\t Welcome to function1()")
	#end of function1

def function2():
	""" print a welcome message for option 1"""
	print("\n\t Welcome to function2()")
	#end of function1
def function3():
	""" print a welcome message for option 1"""
	print("\n\t Welcome to function3()")
	#end of function1




def main():
	# the program actually starts here. The dictionary of table names tables_dict is a global variable and is accessible by all functions, as necessary.
	print("\t Welcome to my database automation demo program!")

	myTable_str = getTableName()
	print(f" [+] There are <{tables_dict[myTable_str]}> attributes associated with table <{myTable_str}>.")

	print("\n\t Here is a fancy menu system.")
	result_int = userMenu()
	print(f"\t The menu returns value: {result_int}")

	print("  -- End of program --")
# end of main()

main() # run the driver function of program here
