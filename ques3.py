# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

print(" iterator is an object that allows you to iterate over a sequence of elements")

my_list = [2,4,6,8,10,12,14,16,18,20 ]
my_iterator = iter(my_list)

for i in range(5) :
    element = next(my_iterator)
    print(element)