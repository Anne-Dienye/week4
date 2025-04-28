#coding
def is_in_range(n):
    return 0 <= n <= 100

# Test program
number = int(input("Enter an integer: "))
if is_in_range(number):
    print(f"{number} is in the range 0 to 100.")
else:
    print(f"{number} is NOT in the range 0 to 100.")