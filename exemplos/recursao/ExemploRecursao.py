def recursive_countdown(number):
    if number < 1:
        return
    recursive_countdown(number - 1)
    print(number)

recursive_countdown(5)