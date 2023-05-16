# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.

print("genrator function is a special type of function that returns an iterator called generator")

print("the yeild keyword is used in a generator function  to indicate that th function should pause its extecution and yeild a value to the caller")

def generate_even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

# Using the generator function
even_generator = generate_even_numbers(10)

for num in even_generator:
    print(num)
