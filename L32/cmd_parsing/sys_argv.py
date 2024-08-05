# script for adding to numbers
import sys

args = sys.argv[1:]
print(args)
if len(args) != 2:
    raise ValueError("Exactly 2 arguments shoyuld be passed")

a = int(args[0])
b = int(args[1])
print(f"{a} + {b} = {a + b}")
