#!/usr/bin/python3

def safe_print_integer(value: int) -> bool:
	"""
	Safely prints an integer value.
	
	Args:
	- value: The value to be printed
	
	Returns:
	- True if the value is an integer and gets printed successfully, False otherwise
	"""
	try:
		print("{:d}".format(value))
		return True
	except (ValueError, TypeError):
		return False
