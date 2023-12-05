#!/usr/bin/python3

# Assuming the divisible_by_2 function exists and performs the intended operation
def divisible_by_2(my_list):
    return [x % 2 == 0 for x in my_list]

# Using the imported function to get the list indicating divisibility by 2
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

# Printing the results
i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
