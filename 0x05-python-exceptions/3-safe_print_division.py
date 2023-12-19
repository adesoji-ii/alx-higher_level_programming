#!/usr/bin/python3

def safe_print_division(dividend, divisor):
	"""Returns the division of dividend by divisor."""
	try:
		result = dividend / divisor
	except ZeroDivisionError:
		print("Error: Division by zero")
		result = None
	except TypeError:
		print("Error: Unsupported operand type")
		result = None
	finally:
		print("Result of the division: {}".format(result))
	return result
