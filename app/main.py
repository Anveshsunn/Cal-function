# This file contains math functions: exponentiation, square root, absolute value, and cube.
# These functions expand the capabilities of our calculator by performing more advanced math operations.


def exponentiation(base: float, exp: float) -> float:
    """
    This function takes two numbers: 'base' and 'exp', and returns 'base' raised to the power of 'exp' (base ** exp).
    'base' is the number we want to multiply by itself 'exp' times.
    Example: if we call exponentiation(2.0, 3.0), it will return 8.0 (because 2 * 2 * 2 = 8).
    """
    return base ** exp  # This raises the base to the power of exp and returns the result.

def square_root(a: float) -> float:
    """
    This function takes one number (a) and returns its square root (math.sqrt(a)).
    The square root is a number that, when multiplied by itself, equals the original number.
    BUT, we cannot take the square root of a negative number, so we raise a 'ValueError' if 'a' is negative.
    Example: if we call square_root(16.0), it will return 4.0 (because 4 * 4 = 16).
    """
    if a < 0:
        # This part checks if 'a' is negative. If it is, we raise an error since the square root of a negative number is not allowed.
        raise ValueError("Square root of negative number is not allowed.")  # Error message for negative input.
    return a ** 0.5  # This calculates the square root of the number and returns the result.

def absolute_value(a: float) -> float:
    """
    This function takes one number (a) and returns its absolute value (abs(a)).
    The absolute value of a number is its distance from zero, so it removes any negative sign.
    Example: if we call absolute_value(-5.0), it will return 5.0.
    """
    return abs(a)  # This returns the absolute value of the number 'a'.

def cube(a: float) -> float:
    """
    This function takes one number (a) and returns its cube (a ** 3).
    Cubing a number means multiplying it by itself two more times.
    Example: if we call cube(3.0), it will return 27.0 (because 3 * 3 * 3 = 27).
    """
    return a ** 3  # This calculates the cube of the number and returns the result.
