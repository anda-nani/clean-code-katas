def has_three(num1: int, num2: int) -> bool:
    sum = num1 + num2

    has_digit_three = '3' in str(sum)     #Checking for 3 in the sum value
    has_input_three = num1 == 3 or num2 == 3

    return has_input_three and has_digit_three

print(has_three(10, 20))