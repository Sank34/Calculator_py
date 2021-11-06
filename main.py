# Python Calculator example by Sank34

# first,we need to introduce the signs(+,-,etc)

# subtract 2 numbers
def subtract(x, y):
    return x - y

# add 2 num.
def add(x, y):
    return x + y

# divide 2 num.
def divide(x, y):
    return x / y

# multiply 2 num.
def multiply(x, y):
    return x * y

# Now,we need to print the options
# Show the options in the output
print("Select an option:")
print("1.Add 2 num.")
print("2.Subtract 2 num.")
print("3.Multiply 2 num.")
print("4.Divide 2 num.")

# Loop for the calculator

while True:
    ch = input("enter what do you wanna choose(1/2/3/4): ")
    # Adding the error message
    if ch != "1" and ch != "2" and ch != "3" and ch != "4":
        print("ERROR!Please select a valid option")
        ch = input("enter what do you wanna choose(1/2/3/4): ")

    # checking if the choice is in the list
    if ch in ("1", "2", "3", "4"):
          num1 = float(input("Enter the first num: "))
          num2 = float(input("Enter the second num: "))

    if ch == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif ch == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif ch == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif ch == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    break


