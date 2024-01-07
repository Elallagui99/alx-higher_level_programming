#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the int of a + b
    * a and be must be integers or floats
    otherwise: TypeError exception
    * a and b must be casted to int if it they are float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
