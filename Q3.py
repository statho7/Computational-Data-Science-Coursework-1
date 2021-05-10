# student number: 2086876

def function_renamer(code):
    '''
    Renames the function names to be in camel case for the functions included in the provided code.
    
    Args:
        code: The code provided by the user as a string.
        
    Returns: A tuple (d, newcode). The d is a nested dictionary where each key corresponds to the original function name. The newcode is a string containing the code where all function names that were not in camel case have been renamed by their camel case versions.
    '''
    
    #using regex and groups to find the functions names and append them in a list
    import re
    pattern = r'def ([\_a-zA-Z]+\w*)\('
    function_names = re.findall(pattern, str(code))
    
    d = {}
    newcode = code
    
    #iterate through the function names we found above
    for func in function_names:
        camelcase = func
        
        
        #using regex and groups to find the functions names that start with an underscore(_) or more underscores(ex. ___) and a lowercase letter
        pattern = r'([\_]+[a-z])\w*'
        start_under_lower = re.findall(pattern, func)
        
        #if we found a function that starts with an underscore(_) and a lowercase letter we keep the underscore and capitalize the letter
        if len(start_under_lower) > 0 and start_under_lower[0] == func[0:len(start_under_lower[0])]:
            camelcase = func.replace(start_under_lower[0], start_under_lower[0].upper())
        
        #using regex and groups to find the functions names that start with a lowercase letter
        pattern = r'\b([a-z]{1})\w*'
        start_lower = re.findall(pattern, func)
        
        #if we found a function that starts with a lowercase letter we capitalize the letter
        if len(start_lower) > 0:
            camelcase = camelcase.replace(start_lower[0], start_lower[0].upper().replace('_', ''))
        
        #using regex and groups to find the functions names that have in any point an underscore(_) and a lowercase letter
        pattern = r'(\_[a-z])'
        under_lower = re.findall(pattern, func)
        
        #if we found a function that has at any point an underscore(_) and a lowercase letter we remove the underscore and capitalize the letter
        if len(under_lower) > 0:
            for i in under_lower:
                if i != func[0:2]:
                    camelcase = camelcase.replace(i, i.upper().replace('_', ''))

        # we are adding a new key with the name of function in the dictionary for each function name
        d[func] = {'hash':hash(func),'camelcase': camelcase ,'allcaps':func.upper()}
        
        #replacing the function name in the code with camelcase variable
        #if the function name was already in camelcase it will make no difference in the code
        newcode = newcode.replace(func, camelcase)
    return (d, newcode)


### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
if __name__ == '__main__':
    # Example 1
    testcases = {
        'example 1':
"""
def add_two_numbers(a, b):
  return a + b

print(add_two_numbers(10, 20))
""",
    'example 2' :
"""
def _major_split(*args):
  return (args[:2], args[2:])

def CheckTruth(t = True):
  print('t is', t)
  return _major_split([t]*10)

x, y = _major_split((10, 20, 30, 40, 50))
CheckTruth(len(x) == 10)
"""
    }
    for key, code in testcases.items():
        print(f'--- {key} ---')
        out = function_renamer(code)
        if not isinstance(out, tuple) or len(out)!=2:
            raise TypeError('function_renamer should return a tuple of length 2')
        d, newcode = out
        if not isinstance(d, dict):
            raise TypeError('return argument d should be a dictionary')
        if not isinstance(newcode, str):
            raise TypeError('return argument code should be a string')
        print('d = ', d)
        print('\ncode:')
        print(newcode)