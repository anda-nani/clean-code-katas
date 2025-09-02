def evenOrOdd(num: int) -> str:

    if num % 2 == 0 :       #Check if there is no remainder
        return "even"
    else:
        return "odd"
    
num = input("Enter a number: ")     #prompt user for input

print(evenOrOdd(int(num)))