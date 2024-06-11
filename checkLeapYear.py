# Which year do you want to check?
print("Enter an year to check if it is a leap year")
year = int(input())
# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
     print("Leap year")
else:
  print("Not leap year")