def longest_word_in(sentence):
	my_list=sentence.split()
	max_length=my_list[0]
	for i in my_list:
		if len(i)>len(max_length):
			max_length=i
	return max_length

print(longest_word_in("Bashar al-asad Ali Salah"))
