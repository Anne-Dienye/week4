# functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Test program
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}C is equivalent to {temp_f}F.")

temp_f_input = float(input("Enter temperature in Fahrenheit: "))
temp_c_output = fahrenheit_to_celsius(temp_f_input)
print(f"{temp_f_input}F is equivalent to {temp_c_output}C.")