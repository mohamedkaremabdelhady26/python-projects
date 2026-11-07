# ~ def convert(n):
	# ~ my_list=[]
	# ~ return [int(i) for i in str(n)[::-1]]

# ~ print(convert(19216811))
#####################################################
# ~ def convert(n):
	# ~ my_list=[]
	# ~ for i in str(n):
		# ~ my_list.insert(0, int(i))
	# ~ return my_list	

# ~ print(convert(19216811))
#####################################################
# ~ def convert(n):
	# ~ st=str(n)
	# ~ my_list=[]
	# ~ for i in st:
		# ~ my_list.append(int(i))
	# ~ my_list.reverse()
	# ~ return my_list	

# ~ print(convert(19216811))
#####################################################		
#Top
# ~ def convert(n):
	# ~ my_list=str(n)
	# ~ new_list=[]
	# ~ for i in range(1, len(my_list)+1):
		# ~ new_list.append(int(my_list[-i]))
	# ~ return new_list

# ~ print(convert(123456))
	
