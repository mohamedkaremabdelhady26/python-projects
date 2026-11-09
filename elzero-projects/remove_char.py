def remove_char_from(word, c):
	word_without_char=[]
	for i in word:
		if i not in [c.lower(), c.upper()]:
			word_without_char.append(i)
	
	result="".join(new_word)
	
	return result


def remove_char_from(word, c):

	result = word.replace(c.lower(), "").replace(c.upper(), "")
	return result		


print(remove_char_from("salah llsaam fdhl", "L"))
