from calculator import sum


print(sum(1, 3))

try:
    print(sum('8', 7))
except AssertionError as e:
    print(f'Invalid operation: {e}')

print('conta:', sum(1, 4))