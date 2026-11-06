"""
Logical Calculator Project (Enhanced from Codewars 8 kyu)
This script allows the user to input a list of booleans dynamically,
select a logical operation (AND, OR, XOR), and compute the final sequential result.
"""


def fill_array():
	my_array=[]
	while len(my_array)<2:
		bool_value=(input("Enter A Boolean Value (True/False): ")).strip().capitalize()
		if bool_value=="True":
			my_array.append(True)
		elif bool_value=="False":
			my_array.append(False)
		else:
			print("Invalid input! Please enter True or False.")

	while True:
			bool_value=(input("Enter A Boolean Value or Exit To finish: ")).strip().capitalize()
			if bool_value=="Exit":
				print("The entry has been completed successfully.")
				break
			elif bool_value=="True":
				my_array.append(True)
			elif bool_value=="False":
				my_array.append(False)
			else:
				print("Invalid input! Please enter True or False.")
	return my_array



def selecting_operation():
	while True:
		input_value=(input("Enter A Operation (AND, OR, XOR): ")).strip().upper()
		if input_value in ["AND", "OR", "XOR"]:
			return input_value
		else:
			print("Invalid input! Please enter AND, OR, XOR.")

		

def logical_calc(array, op):
    result=array[0]
    for i in array[1:]:
        if op == "AND":
            result = result and i
        elif op == "OR":
            result = result or i
        elif op == "XOR":
            result = result != i
    return result
            
def display_logical_calc():
	print("Welcome To Logical Calculator Programing")
	x=fill_array()
	y=selecting_operation()
	z=logical_calc(x, y)
	print(f"Your Booleans : {x} And The Operation [{y}] And The Result Is : [{z}]")
	
	
	
display_logical_calc()	
	
