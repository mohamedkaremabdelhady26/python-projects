import string

# Method 1: Using string slicing and standard character lookup
def find_missing_letter_v1(givenletters):
    alpha = string.ascii_lowercase
    start = alpha.index(givenletters[0])
    end = alpha.index(givenletters[-1])
    
    for i in alpha[start:end+1]:
        if i not in givenletters:
            return i
            
    return "No Missing Letter In Sequence"


# Method 2: Using ASCII ord() values and sets for optimized lookup
def find_missing_letter_v2(sequence):
    sequence = sequence.lower()
    full_set = set(range(ord(sequence[0]), ord(sequence[-1]) + 1))
    given_set = set(ord(c) for c in sequence)
    
    missing_ords = sorted(full_set - given_set)
    
    if not missing_ords:
        return "No Missing Letter In Sequence"
        
    missing_chars = [chr(c) for c in missing_ords]
    return missing_chars[0] if len(missing_chars) == 1 else missing_chars


if __name__ == "__main__":
    test_str = "abcdeg"
    
    # Testing Method 1
    print("--- Method 1 Test ---")
    print(f"Result: {find_missing_letter_v1(test_str)}")
    
    # Testing Method 2
    print("\n--- Method 2 Test ---")
    print(f"Result: {find_missing_letter_v2(test_str)}")
