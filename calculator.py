

a = float(input("Enter number 1: "))  
o = input("Enter operator: ")
b = float(input("Enter number 2: ")) 

if o in ['+', '-', '*', '/']:  
    if o == '+':
        out = a + b
    elif o == '-':
        out = a - b
    elif o == '*':
        out = a * b
    elif o == '/':
        if b != 0:  
            out = a / b  
        else:
            print("Error: cannot Divide by zero")
            out = None
    if out is not None:  
        print("Output:", out)
else:
    print("Error: Invalid Operator")
