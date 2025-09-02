from math import sqrt   

def calcAreaOfTriangle(num1: float, num2: float, num3: float) -> float:

    s: float = (num1 + num2 + num3) / 2  # semi-perimeter of the triangle

    area = sqrt(s * (s - num1) * (s - num2) * (s - num3))   #Heron's formula to calculate the area

    return area

print(calcAreaOfTriangle(3, 4, 5))

