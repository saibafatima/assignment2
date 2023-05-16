# Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

print("we use def keyword for function ")

def ger_odd_numbers():
    odd_numbers = []
    for number in range(1,26):
        if number % 2!= 0:
            odd_numbers.append(number)
    return odd_numbers 

#calling function
result = ger_odd_numbers()
print(result)