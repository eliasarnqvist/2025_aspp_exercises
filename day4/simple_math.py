"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Calculates the sum of two numbers.

    Parameters
    ----------
    a : int or float
        The first number to be added
    b : int or float
        The second number to be added
    
    Returns
    -------
    int or float
        The sum of a and b
    """
    return a+b

def simple_sub(a,b):
    """
    Calculates the difference between two numbers.

    Parameters
    ----------
    a : int or float
        The number to be subtracted from
    b : int or float
        The number to subtract
    
    Returns
    -------
    int or float
        The difference between a and b
    """
    return a-b

def simple_mult(a,b):
    """
    Calculates the product of two numbers.

    Parameters
    ----------
    a : int or float
        The first number to be multiplied
    b : int or float
        The second number to be multiplied
    
    Returns
    -------
    int or float
        The product of a and b
    """
    return a*b

def simple_div(a,b):
    """
    Calculates the quotient of two numbers.

    Parameters
    ----------
    a : int or float
        The number to be divided
    b : int or float
        The divisor
    
    Returns
    -------
    float
        The quotient of a and b
    
    Raises
    ------
    ZeroDivisionError
        If b is zero
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Evaluates a first degree polynomial at x.

    Parameters
    ----------
    x : int or float
        The point at which to evaluate the polynomial
    a0 : int or float
        The coefficient of the zeroth degree term
    a1 : int or float
        The coefficient of the first degree term
    
    Returns
    -------
    int or float
        The value of the polynomial at x
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Evaluates a second degree polynomial at x.

    Parameters
    ----------
    x : int or float
        The point at which to evaluate the polynomial
    a0 : int or float
        The coefficient of the zeroth degree term
    a1 : int or float
        The coefficient of the first degree term
    a2 : int or float
        The coefficient of the second degree term
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
