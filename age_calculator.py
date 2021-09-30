import datetime

year = datetime.datetime.now().year


# name = input("Enter your first name:  ")
# year_of_birth = int(input("Enter your year of birth:  "))
# age = year - year_of_birth


def name():
    x = input("Enter your first name: ")
    return x


def age_calculation(x):
    years = year - x
    return years


name = name()
age = age_calculation(int(input("Enter birth year:  ")))

print(f'Hi {name} you are {age} years of age')
