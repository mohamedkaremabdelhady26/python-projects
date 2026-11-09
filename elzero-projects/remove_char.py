def remove_char_from(word, c):
	word_without_char=[]
	for i in word:
		if i not in [c.lower(), c.upper()]:
			word_without_char.append(i)
	
	return "".join(word_without_char)


def remove_char_from(word, c):
	
	result=filter(lambda x:x not in [c.lower(), c.upper()], word)
	
	return "".join(result)


def remove_char_from(word, c):

	result = word.replace(c.lower(), "").replace(c.upper(), "")
	return result		



