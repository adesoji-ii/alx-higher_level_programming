#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	"""Print the first x elements of a list that are integers.

	Args:
		my_list (list): The list to print elements from.
		x (int): The number of elements of my_list to print.

	Returns:
		The number of elements printed.
	"""
	count_printed = 0
	for item in my_list[:x]:
		if isinstance(item, int):
			try:
				print("{:d}".format(item), end="")
				count_printed += 1
			except ValueError:
				pass  # In case of a value error in formatting
	print("")
	return count_printed
