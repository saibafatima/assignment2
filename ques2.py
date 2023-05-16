# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.

print("*args and **kwargs are used in function definitions to allow a variable number of arguments to be passed to the function.")

def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_values(1, 2, 3, 4, 5)
print(result)  # Output: 15

print("**kwargs allows you to pass a variable number of keyword arguments to a function. It collects the keyword arguments into a dictionary. ")

def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_details(name="John", age=25, city="New York")
