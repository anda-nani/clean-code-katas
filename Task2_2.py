#function that build a tringle of based on the integer provided
def triangle(num: int, mode: str = "left") -> None:
    col = 0 
    if mode == "left":             #check if input is positve 
        col = 1               #set number of columns in first row
        for _ in range(num):
            print("#" * col)   #multiply the hash with num of columns
            col += 1          #increment num columns for the next row
   
    elif mode == "right":
            for i in range(1, num + 1):
                spaces = num - i
                print(" " * spaces + "#" * i)

    elif mode == "isosceles":
        if num > 0:
            for i in range(1, num + 1):
                spaces = num - i
                hashes = 2 * i - 1
                print(" " * spaces + "#" * hashes)
        else:
            num = abs(num)
            for i in range(num, 0, -1):
                spaces = num - i
                hashes = 2 * i - 1
                print(" " * spaces + "#" * hashes)
             
            

   
#sample call 
triangle(3)
triangle(3, "right")
triangle(3, "isosceles")
triangle(-3, "isosceles")
