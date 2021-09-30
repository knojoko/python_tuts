import datetime

year = datetime.datetime.now().year

# name = input("Enter your first name:  ")
# year_of_birth = int(input("Enter your year of birth:  "))
# age = year - year_of_birth

def name(y):
    y = input("Enter your first name: ")
    print(y)

def age_calculator(x):
    age = year - x
    return age

name = name("khaya")
age = age_calculator(int(input("Enter birth year:  ")))



print(f"Hi {name} you are {age} years of age")



