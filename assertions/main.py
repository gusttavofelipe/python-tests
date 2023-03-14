from calculadora import soma


print(soma(1, 3))

try:
    print(soma('8', 7))
except AssertionError as e:
    print(f'Invalid operation: {e}')

print('conta:', soma(1, 4))