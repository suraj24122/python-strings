# palindrome 

s = input("Enter the value = ")

reverse = s[::-1] # s[start : stop : step]
# -1: Moves backward (right to left).
# step=-1 is what makes it reverse.

if s == reverse:
    print("The value entered by user is palindrome")
else:
    print("Not a palindrome")
