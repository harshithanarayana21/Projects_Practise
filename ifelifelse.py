print("Enter your height in meters")
height = float(input())  # in meters e.g., 1.55
print("Enter your weight in kilograms")
weight = int(input())  # in kilograms e.g., 72
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
