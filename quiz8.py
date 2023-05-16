# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

number = int(input("enter a number: "))
original_number = number
reverse_number = 0

while number > 0 :
    remainder = number % 10
    reverse_number = (reverse_number * 10) + remainder
    number = number//10

if original_number == reverse_number:
    print("the number is a palindrome.")

else:
    print("the number is not a palindrome.")
    
