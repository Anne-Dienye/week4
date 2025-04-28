#coding
def remove_last_char(s):
    if len(s) > 1:
        return s[:-1]
    return s

# Test program
text = input("Enter a string: ")
result = remove_last_char(text)
print(f"String after removing last character: {result}")