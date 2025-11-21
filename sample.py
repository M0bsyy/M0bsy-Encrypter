#!/usr/bin/env python3
"""
Sample Python File - Demonstrates the encryption tool
This is a simple example program that will be encrypted.
"""

def greet(name):
    """Greet someone by name"""
    return f"Hello, {name}! Welcome to the encrypted world!"

def calculate_fibonacci(n):
    """Calculate Fibonacci sequence"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    print("=" * 50)
    print("Sample Python Program - Before Encryption")
    print("=" * 50)
    
    message = greet("User")
    print(f"\n{message}\n")
    
    print("Let's calculate Fibonacci sequence (first 10 numbers):")
    fib_numbers = calculate_fibonacci(10)
    print(f"Fibonacci: {fib_numbers}")
    
    print("\nThis program demonstrates that encrypted files")
    print("work exactly the same as the original!")
    print("\n" + "=" * 50)
    print("Program completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
