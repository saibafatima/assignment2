# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# out odd numbers.

odd_numbers = [num for num in range(1,101) if num % 2 != 0]
print(odd_numbers)