def get_multiplied_digits(number):
    if number == 0:
        return 1
    first = number % 10
    if first == 0:
        first = 1
    return first * get_multiplied_digits(number//10)

result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
