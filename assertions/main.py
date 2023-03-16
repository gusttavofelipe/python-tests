from calculator import calc


print(calc(1, 3))

try:
    print(calc('8', 7))
except AssertionError as e:
    print(f'Invalid operation: {e}')

print('conta:', calc(1, 4))