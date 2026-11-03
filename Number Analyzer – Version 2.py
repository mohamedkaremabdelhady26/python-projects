my_numbers=[]
frequency={}
while True:
	try:
		num=int(input("Enter numbers or Enter 0 to exit"))
		if num ==0:
			print("Please Enter Correct numbers for start. Do not Enter Zero (0) xxx")
			continue
		my_numbers.append(num)
		break
	except ValueError:
		print("Invalid input! Please enter a valid number")

while True:
	try:
		num=int(input("Enter numbers or Enter 0 to exit"))
		if num==0:
			break
		my_numbers.append(num)
	except ValueError:
		print("Invalid input! Please enter a valid number.")
def get_max(numbers):
	max_num=numbers[0]
	for i in numbers:
		if i>max_num:
			max_num=i
	return max_num		

def get_min(numbers):
	min_num=numbers[0]
	for i in numbers:
		if i<min_num:
			min_num=i
	return min_num

def calculate_total(numbers):
	total=0
	for i in numbers:
		total+=i
	return total
				
def calculate_average(numbers):
	total=calculate_total(numbers)
	return total/len(numbers)	

def count_even(numbers):
	even_num=0
	for i in numbers:
		if i%2==0:
			even_num+=1
	return even_num
	
def count_odd(numbers):
	odd_num=0
	for i in numbers:
		if i%2!=0:
			odd_num+=1
	return odd_num		

def get_frequency(numbers):
	frequency={}
	for i in numbers:
		if i not in frequency:
			frequency[i]=1
		else:
			frequency[i]+=1
	return frequency

def display_frequency(x):
	print("-------frequency-------")
	for i, j in x.items():
		print(f"number : {i}, appears : {j}")

def get_max_frequency(my_freq):
	max_frequency=0
	for i, j in my_freq.items():
		if j>max_frequency:
			max_frequency=j
		
	for i, j in my_freq.items():
		if j==max_frequency:
			print(f"The number that appeared most frequently is {i}, and it appeared {j} times.")
		
def analyze_numbers(numbers):
	print(numbers)	
	print("\n--- Analysis Results ---")
	print(f"Maximum Number: {get_max(numbers)}")
	print(f"Minimum Number: {get_min(numbers)}")
	print(f"Total Sum     : {calculate_total(numbers)}")
	print(f"Average    : {calculate_average(numbers)}")
	print(f"Number of even numbers    : {count_even(numbers)}")
	print(f"Number of odd numbers    : {count_odd(numbers)}")
	frequency_numbers=get_frequency(numbers)
	display_frequency(frequency_numbers)
	get_max_frequency(frequency_numbers)

analyze_numbers(my_numbers)
