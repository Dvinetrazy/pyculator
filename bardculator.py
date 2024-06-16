import math
import numpy as np

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def power(a, b):
  return math.pow(a, b)

def square_root(a):
  return math.sqrt(a)

def sine(a):
  return math.sin(a)

def cosine(a):
  return math.cos(a)

def tangent(a):
  return math.tan(a)

def main():
  print("Welcome to the Python calculator!")

  # Prompt the user for input.
  operation = input("What operation would you like to perform? (+, -, *, /, pow, sqrt, sin, cos, tan): ")
  number_1 = float(input("Enter your first number: "))
  number_2 = float(input("Enter your second number: "))

  # Perform the requested operation.
  if operation == "+":
    result = add(number_1, number_2)
  elif operation == "-":
    result = subtract(number_1, number_2)
  elif operation == "*":
    result = multiply(number_1, number_2)
  elif operation == "/":
    result = divide(number_1, number_2)
  elif operation == "pow":
    result = power(number_1, number_2)
  elif operation == "sqrt":
    result = square_root(number_1)
  elif operation == "sin":
    result = sine(number_1)
  elif operation == "cos":
    result = cosine(number_1)
  elif operation == "tan":
    result = tangent(number_1)
  else:
    print("Invalid operation.")
    return

  # Display the result to the user.
  print(f"{number_1} {operation} {number_2} = {result}")

if __name__ == "__main__":
  main()
