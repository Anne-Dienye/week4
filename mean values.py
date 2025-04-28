#coding
temperatures = [46]
for i in range(6):
    temp = float(input(f"Enter temperature {i+1}: "))
    temperatures.append(temp)

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)

print(f"Maximum: {max_temp}, Minimum: {min_temp}, Mean: {mean_temp:.2f}")