num1 = 52
num2 = 6
num3 = 125

sum_of_digits = lambda x: sum(int(digit) for digit in str(x))

print(sum_of_digits(num1))
print(sum_of_digits(num2))
print(sum_of_digits(num3))