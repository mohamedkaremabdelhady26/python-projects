import string

def find_missing_letter_v1(givenletters):
    alpha = string.ascii_lowercase
    start = alpha.index(givenletters[0])
    end = alpha.index(givenletters[-1])
    
    for i in alpha[start:end+1]:
        if i not in givenletters:
            return i
            
    return "No Missing Letter In Sequence"

