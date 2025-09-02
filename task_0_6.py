def maximum(*args: int):

    max_num = args[0]  # Assume the first number is the maximum initially

    for num in args:
        if num > max_num:
            max_num = num   
    
    return print(max_num)
    
maximum(10, 14, 12, 2, 36)