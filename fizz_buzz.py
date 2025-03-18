## Division Practice
## Fill in what you think the output of the following operations will be

# Float Division
print(7 / 2)   
print("My Guess: 3.5")

print(10 / 4)  
print("My Guess: 2.5")

print(10 / 2)  
print("My Guess: 5.0")


# Integer Division
print(7 // 2)  
print("My Guess: 3")

print(10 // 4)
print("My Guess: 2")

print(10 // 2)  
print("My Guess: 5")

# Modulus
print(7 % 2)   
print("My Guess: 1")

print(10 % 2)  
print("My Guess: 0")



## Write a program that prints the numbers 1-50
## But...
#  If the number is divisible by 3 print "Fizz" instead
# If the number is divisible by 5 print "Buzz" instead
# If the number is divisible by both 5 and 3 print "FizzBuzz"
# If neither just print the number. 
# Utilize loops, if statements etc. !!
number = 0
for i in range(50):
    number + 1 
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print ("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 > 0 and number % 5 > 0:
        print (number)