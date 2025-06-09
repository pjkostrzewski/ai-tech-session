def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   

if __name__ == "__main__":
    input_a = int(input("Enter a: "))
    input_b = int(input("Enter b: "))
    print(add(input_a, input_b))
    print(subtract(input_a, input_b))
    print(multiply(input_a, input_b))
    print(divide(input_a, input_b))