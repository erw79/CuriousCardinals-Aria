## Define and call a function that Takes in a temperature in Fahrenheit and converts it into Celsius

##Define the Function here
def fair_to_cels (temp):
    return (temp - 32) * 5/9
##Call the function for 45 degrees F and 32 degrees F 
f_to_c1 = fair_to_cels(45)
f_to_c2 = fair_to_cels(32)
f_to_c1 = str(f_to_c1)
f_to_c2 = str(f_to_c2)
## Print the results in this form: "50 Degrees F is: 10 degrees C"
print ("45 degrees F is:" + f_to_c1 + "degrees C")
print ("32 degrees F is:" + f_to_c2 + "degrees C")