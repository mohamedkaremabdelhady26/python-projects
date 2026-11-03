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
even_num=0
odd_num=0
total=0
for i in my_numbers:
	if i>max_num:
		max_num=i
	if i<min_num:
		min_num=i
	if i%2==0:
		even_num+=1
	else:
		odd_num+=1
		
	total+=i
average=total/len(my_numbers)

frequency={}
for i in my_numbers:
	if i not in frequency:
		frequency[i]=1
	else:
		frequency[i]+=1	

print(my_numbers)	
print("\n--- Analysis Results ---")
print(f"Maximum Number: {max_num}")
print(f"Minimum Number: {min_num}")
print(f"Total Sum     : {total}")
print(f"Average    : {average}")
print(f"Number of even numbers    : {even_num}")
print(f"Number of odd numbers    : {odd_num}")

max_frequency=0
for i, j in frequency.items():
	if j>max_frequency:
		max_frequency=j
	
for i, j in frequency.items():
	if j==max_frequency:
		print(f"The number that appeared most frequently is {i}, and it appeared {j} times.")
		
