#!/usr/bin/python3

def raise_exception_msg(message=""):
	"""
	Raise a NameError exception with an optional custom message.

	Args:
	- message (str): Optional custom message for the exception.

	Raises:
	- NameError: Always raises a NameError with the given message.
	"""
	raise NameError(message)
