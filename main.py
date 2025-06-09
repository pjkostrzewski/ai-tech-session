def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int/float): The first number
        b (int/float): The second number
    
    Returns:
        int/float: The sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first number.
    
    Args:
        a (int/float): The first number
        b (int/float): The second number
    
    Returns:
        int/float: The difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a (int/float): The first number
        b (int/float): The second number
    
    Returns:
        int/float: The product of a and b
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second number.
    
    Args:
        a (int/float): The dividend
        b (int/float): The divisor
    
    Returns:
        float: The quotient of a divided by b
    """
    return a / b   

if __name__ == "__main__":
    # Greet the user
    name = input("Hello! What's your name? ")
    print(f"Nice to meet you, {name}! Let's do some calculations.")
    print()
    
    input_a = int(input("Enter a: "))
    input_b = int(input("Enter b: "))
    print(add(input_a, input_b))
    print(subtract(input_a, input_b))
    print(multiply(input_a, input_b))
    print(divide(input_a, input_b))