def celcius_to_fahrenheit(celsius: float) -> float:
    
    f : float = (celsius * 9/5) + 32

    return f

print(celcius_to_fahrenheit(37))  # Example usage   

def fahrenheit_to_ceelsius(fahrenheit: float) -> float:
    
    c : float = (fahrenheit - 32) * 5/9

    return c

print(fahrenheit_to_ceelsius(98.6))  # Example usage