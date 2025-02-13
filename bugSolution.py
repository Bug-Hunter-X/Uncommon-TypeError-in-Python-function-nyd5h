def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Error: {e}"

print(function_with_improved_error_handling(10, 0))  # Output: Division by zero
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, "hello")) # Output: Error: Inputs must be numbers
print(function_with_improved_error_handling("hello", 2)) # Output: Error: Inputs must be numbers