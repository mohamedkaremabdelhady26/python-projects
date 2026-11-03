my_numbers=[]
while True:
	try:
		num=int(input("Enter numbers or Enter 0 to exit"))
		if num ==0:
			print("Please Enter Correct numbers for start. Do not Enter Zero (0) xxx")
			continue
		my_numbers.append(num)
		break
	except ValueError:
		print("Invalid input! Please enter a valid number.")

while True:
	try:
		num=int(input("Please Enter a numbers or Enter 0 to exit"))
		if num==0:
			break
		my_numbers.append(num)
	except ValueError:
		print("Invalid input! Please enter a valid number.")
		

max_num=my_numbers[0]
min_num=my_numbers[0]
total=0
for i in my_numbers:
	if i>max_num:
		max_num=i
	if i<min_num:
		min_num=i
	total+=i
	
	
print(my_numbers)	
print("\n--- Analysis Results ---")
print(f"Maximum Number: {max_num}")
print(f"Minimum Number: {min_num}")
print(f"Total Sum     : {total}")


print("Frequency: ")
printed_numbers=[]
for i in my_numbers:
	count=0
	if i not in printed_numbers:
		printed_numbers.append(i)
		for j in my_numbers:
			if i == j:
				count+=1
		print(f"{i} appears {count} times")
