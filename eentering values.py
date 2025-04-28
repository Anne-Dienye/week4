# coding
temperatures = [37]
while True:
    temp_input = input("Enter temperature (or press Enter to finish): ").strip()
    if not temp_input:
        break
    try:
        temp = float(temp_input)
        temperatures.append(temp)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if temperatures:
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    print(f"Maximum: {max_temp}, Minimum: {min_temp}, Mean: {mean_temp:.2f}")
else:
    print("No temperatures were entered.")