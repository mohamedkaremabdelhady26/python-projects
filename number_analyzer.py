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
		print("Invalid input! Please enter a valid number")

while True:
	try:
		num=int(input("Enter numbers or Enter 0 to exit"))
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
frequency={}
for i in my_numbers:
	if i not in frequency:
		frequency[i] = 1 
	else:
		frequency[i]+=1

search_num=int(input("Enter a number to search for it"))
count=frequency.get(search_num, 0)
print(f"{search_num} appears {count} times")
