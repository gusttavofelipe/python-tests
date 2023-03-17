try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise


from calculator import calc_sum

print(calc_sum(1, 3))

try:
    print(calc_sum('8', 7))
except AssertionError as e:
    print(f'Invalid operation: {e}')

print('conta:', calc_sum(1, 4))