def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def main():
  while True:
    operation = input("Select operation.\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")

    if operation in ('1', '2', '3', '4'):
      first_number = float(input("Enter first number: "))
      second_number = float(input("Enter second number: "))

      if operation == '1':
        print(first_number, "+", second_number, "=", add(first_number, second_number))
      elif operation == '2':
        print(first_number, "-", second_number, "=", subtract(first_number, second_number))
      elif operation == '3':
        print(first_number, "*", second_number, "=", multiply(first_number, second_number))
      elif operation == '4':
        print(first_number, "/", second_number, "=", divide(first_number, second_number))

    elif operation == '5':
      break

    else:
      print("Invalid input!")

if __name__ == "__main__":
  main()
