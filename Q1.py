# student number: 2086876

def do_arithmetic(x, y, op='add'):
    '''
    Does an arithmetic calculation based on the arguments the user provides.

    Args:
        x: The first number provided by the user.
        y: The second number provided by the user.
        op: The operation user wants to perform. Default value is the add operation.

    Returns: The result of the calculation as a float number.
    '''

    operations = ['add', 'substract', 'multiply', 'divide']
    # if statement to check if the op provided is one of those stated in the Q1 a)
    if op not in operations:
        print('Unknown operation')
    else:
        if op == 'substract':
            return float(x - y)
        elif op == 'multiply':
            return float(x * y)
        elif op == 'divide':
            # we use try-except to catch the ZeroDivisionError and return 'None' as asked if y equals 0
            try:
                return float(x / y)
            except:
                return 'None'
        else:
            return float(x + y)


def sum_of_digits(s=0):
    '''
    Calculates the sum of the digits that the provided string contains.

    Args:
        s: The string provided by the user.

    Returns: The sum of the digits as an integer number.
    '''
    # if statement to check if the user provided string
    if s == 0:
        return 0
    else:
        # using regex to isolate numbers in an array and then use sum() function to return their sum
        import re
        pattern = '[0-9]'
        # list of the digits as strings
        string_digits = re.findall(pattern, s)
        # list of the digits as integers
        integer_digits = [int(i) for i in string_digits]
        return sum(integer_digits)


# --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
if __name__ == '__main__':
    testcases = {'do_arithmetic': [(10, 4, 'add'), (2, 3, 'multiply')],
                 'sum_of_digits': [("123",), ("10a20",)]}

    print('\n-- do_arithmetic testcases --')
    for args in testcases['do_arithmetic']:
        print('input:', str(args))
        print('output:', do_arithmetic(*args))
        print('-----------')

    print('\n-- sum_of_digits testcases --')
    for args in testcases['sum_of_digits']:
        print('input:', str(args))
        print('output:', sum_of_digits(*args))
        print('-----------')
