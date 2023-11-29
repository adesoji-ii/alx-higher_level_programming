#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:  # Checking if the ASCII value is odd
        i -= 32  # Convert lowercase to uppercase by subtracting 32
        print(chr(i), end="")
