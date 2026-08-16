#Calculator
a = int(input("Enter first number:"))
opt = input("Enter operator(+,-,*,%,**):")
b = int(input("Enter second number:"))

if opt == '+':
    print("Answer:",a+b)
elif opt == '-':
    print("Answer:",a-b)
elif opt == '*':
    print("Answer:",a*b)
elif opt == '%':
    print("Answer:",a%b)
elif opt == '**':
    print("Answer:",a**b)
else:
    print("Invalid operator!")