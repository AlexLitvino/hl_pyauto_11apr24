import argparse

parser = argparse.ArgumentParser(prog="Calculator")

#parser.add_argument('counter', help='Counter')
parser.add_argument('--a', help='First number, float', default=0, type=float)
parser.add_argument('--b', help='Second number, float', default=0, type=float)
parser.add_argument('--method', '-m', help='Method, string', default='', type=str, dest='m')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', action='store_true')
group.add_argument('-q', action='store_true')

args = parser.parse_args()
print(args)
#print(args.counter)
#print(type(args.counter))
a = args.a
b = args.b

if args.q:
    print(a+b)
elif args.v:
    print(f"First argument {a}")
    print(f"Second argument {a}")
    print(f"Sum: {a+b}")
else:
    print(f"{a} + {b} = {a + b}")
