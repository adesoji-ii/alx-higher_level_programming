#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(1, len(sys.argv)):  # Start from index 1 to skip the script name
        try:
            total += int(sys.argv[i])
        except ValueError:
            print(f"Invalid input: {sys.argv[i]}. Skipping...")
    print("Sum:", total)
