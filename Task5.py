#function that build a tringle of based on the integer provided
def triangle(num: int) -> None:
    col = 0 
    if num > 0:             #check if input is positve 
        col = 1               #set number of columns in first row
        for _ in range(num):
            print("# " * col)   #multiply the hash with num of columns
            col += 1          #increment num columns for the next row
    else:
        num *= -1
        col = num 
        for _ in range(num):
            print("# " * col)   #multiply the hash with num of columns
            col -= 1            #decrement num columns for the next row

#sample call 
triangle(2)
triangle(4)
triangle(-2)