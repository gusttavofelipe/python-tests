
# "assert" verifica se uma condicao esta sendo satisfeita pra continuacao do codigo

def soma(x, y) -> float:
    assert isinstance(x, (int, float)), 'x should be int or float'
    assert isinstance(y, (int, float)), 'y should be int or float'
    # assert x < y, 'x must be less than y'
    return float(x)+float(y)
