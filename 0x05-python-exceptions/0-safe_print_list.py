#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
	if my_list is None:
		my_list = []  # Set default list if None is provided

	num_printed = 0
	for i in range(x):
		try:
			print(my_list[i], end="")
			num_printed += 1
		except IndexError:
			break
	print("")  # Print a newline after the loop

	return num_printed  # Return the number of elements printed
