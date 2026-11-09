def remove_duplicate_words_from(sentence):
	my_list=sentence.split()
	new_list=[]
	for i in my_list:
		if i not in new_list:
			new_list.append(i)
	return " ".join(new_list)	
	
	
def remove_duplicate_words_from(sentence):
	my_list=sentence.split()
	result=list(dict.fromkeys(my_list))
	return " ".join(result)	


def remove_duplicate_words_from(sentence):
	return " ".join(list(dict.fromkeys(sentence.split())))	
