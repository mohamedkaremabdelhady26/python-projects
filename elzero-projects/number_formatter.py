def add_commas_underscore(num):
	formatted="{:,}".format(num)
	if len(formatted)>3:
		return formatted[:-4]+"_"+formatted[-3:]
				
	return formatted
	
def add_commas_underscore(num):
	formatted=f"{num:,}"
	if len(formatted)>3:
		return formatted[:-4]+"_"+formatted[-3:]
			
	return formatted
	
