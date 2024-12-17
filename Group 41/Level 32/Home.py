first = float(input("Enter first number =>"))
sec = float(input("Enter second number => "))
opr = str(input("Enter Operation  (+, -, *, /)"))

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total = ("Please enter a valid Operation")

print (total)