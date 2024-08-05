import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--a', action='store')
parser.add_argument('--b', action='store_const', const=34)
parser.add_argument('--c', action='store_true')
parser.add_argument('--d', action='store_false')
parser.add_argument('--e', action='append')
parser.add_argument('--f', action='append_const', const='test', dest='env')
parser.add_argument('--g', action='append_const', const='prod', dest='env')
parser.add_argument('-p', '--pro', action='count')

args = parser.parse_args()
print(args)
