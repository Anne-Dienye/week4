#coding
temp_input = input("Enter temperature in centigrade (e.g., 32C): ").strip()
if temp_input[-1] == 'C':
    temp_c = float(temp_input[:-1])
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_input} is equivalent to {temp_f}F.")
else:
    print("Invalid input format. Please use 'numberC'.")