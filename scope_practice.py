## Lets look at scope!
z=100

def multiply(num1,num2):
   answer = num1 * num2
   return answer




##Predict and then run!
answer = multiply(10,50)
print (answer)  # What is printed?
print(z)  # What is printed outside the function?

x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    y = 20  # Another local variable
    print("Inside function:")
    print("x =", x)  # Refers to local x
    print("y =", y)  # Refers to local y

my_function()

y = 50  # Global y, different from local y in the function

print("Outside function:")
print("x =", x)  # Refers to global x
print("y =", y)  # Refers to global y