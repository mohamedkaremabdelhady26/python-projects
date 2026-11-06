""""
Logical Calculator Problem from Codewars (8 kyu)
This function takes a list of booleans and applies a logical operator sequentially.

"""

def logical_calc(array, op):
    result=array[0]
    for i in array[1:]:
        if op == "AND":
            result = result and i
        elif op == "OR":
            result = result or i
        elif op == "XOR":
            result = result != i
    return result
            
