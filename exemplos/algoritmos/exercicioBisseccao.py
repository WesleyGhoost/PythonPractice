def square_root_bisection(target_value, tolerance=3, iterations=8):
    if target_value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if target_value == 0 or target_value == 1:
        print(f'The square root of {target_value} is {target_value}')
        return target_value

    low = 0
    high = target_value if target_value > 1 else 1

    for _ in range(iterations):
        root = (low + high) / 2

        if high - low <= tolerance:
            print(f'The square root of {target_value} is approximately {root}')

            return root

        if root ** 2 > target_value:
            high = root
        else:
            low = root

    print(f'Failed to converge within {iterations} iterations')

    return None