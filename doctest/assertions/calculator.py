# doctest - testa funcoes com os testes escritos na docstring

def calc(x, y) -> float:
    """ calc x and y
    
    >>> calc(-5, 20)
    15.0

    >>> calc(0, -1)
    -1.0

    >>> calc('1', 1)
    Traceback (most recent call last):
    ...
    AssertionError: x should be int or float

    >>> calc(1, '1')
    Traceback (most recent call last):
    ...
    AssertionError: y should be int or float
    """    
    
    assert isinstance(x, (int, float)), 'x should be int or float'
    assert isinstance(y, (int, float)), 'y should be int or float'
    return float(x)+float(y)


def subtract(x, y) -> float:
    """ subtract x from y
    
    >>> subtract(-5, 20)
    -25.0

    >>> subtract(0, -1)
    1.0

    >>> subtract('1', 1)
    Traceback (most recent call last):
    ...
    AssertionError: x should be int or float

    >>> subtract(1, '1')
    Traceback (most recent call last):
    ...
    AssertionError: y should be int or float
    """    
    
    assert isinstance(x, (int, float)), 'x should be int or float'
    assert isinstance(y, (int, float)), 'y should be int or float'
    return float(x)-float(y)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) # verbose=True exibe os testes detalhadamente