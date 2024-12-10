## Lets Make a Simple Calculator that only does Subtraction and Addition, Using what we have learned so far



## 1) Print an introductory statement explaining the rules of the calculator (Subtraction and Addition only).
print ("Welcoome to the calculator. You will be selecting addition or subtraction and then selecting the numbers you would like to add or subtract. I will do the math for you and thene tell you the answer.")




## 2) Ask the user whether they want to add or subtract and store their answer into memory for later use
operation = input("Do you want to add or subtract?")


## 3) Ask the user for their 2 numbers and store them into memory.
number1 = input("Choose your first number.")
number2 = input ("Choose your second number")
number1 = float(number1)
number2 = float(number2)

## 4) Using an if statement, perform either subtraction or addtion on the 2 numbers.
if operation == "+":
    number1 + number2
    print (number1 + number2)
else:
    number1 - number2
    print (number1 - number2)

##.   and Print the output to the user.

