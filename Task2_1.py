def square(num: int, ch: chr = '#') -> None: #assign a default value to be printed #
    for _ in range(num):      #for the number of rows (value of argument)
        print(ch * num)       #printing a multiplied string (columns)

square(2, '*') 