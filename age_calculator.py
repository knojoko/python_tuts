import datetime

year = datetime.datetime.now().year

name = input("Enter your first name:  ")
year_of_birth = int(input("Enter your year of birth:  "))
age = year - year_of_birth



print(f"Hi {name} you are {age} years of age")



