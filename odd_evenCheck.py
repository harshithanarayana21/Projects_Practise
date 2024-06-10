# Which number do you want to check?
print("Enter a number to check whether its an odd or even number")
number = int(input())
result = number % 2
if result == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
