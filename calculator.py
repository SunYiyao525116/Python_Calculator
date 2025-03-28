# Add the following code to the calculator.py file

def add(a, b):
    """
    This function is used to calculate the sum of two numbers
    :param a: The first number
    :param b: The second number
    :return: The sum of the two numbers
    """
    return a + b

def subtract(a, b):
    """
    This function is used to calculate the difference between two numbers
    :param a: The minuend
    :param b: The subtrahend
    :return: The difference between the two numbers
    """
    return a - b

def multiply(a, b):
    """
    This function is used to calculate the product of two numbers
    :param a: The first number
    :param b: The second number
    :return: The product of the two numbers
    """
    return a * b

def divide(a, b):
    """
    This function is used to calculate the quotient of two numbers
    :param a: The dividend
    :param b: The divisor
    :return: The quotient of the two numbers
    """
    if b == 0:
        print("Error: The divisor cannot be zero!")
        return None
    return a / b
