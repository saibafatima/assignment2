# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

#initialize the first two numbers of the fibonacci sequence
num1 , num2 = 0,1
count = 0

#use a while lopp to calculate and print the fibonacci numbers
while count < 10 :
    print(num1)
    nth = num1 + num2
    num1 = num2
    num2 = nth
    count += 1

