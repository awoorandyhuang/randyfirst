# example3.py
from __future__ import print_function
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("n", help="repeat time", type=int)
parser.add_argument("-u", "--user-name", dest="user_name")
args = parser.parse_args()
for _ in range(args.n):
    print("Hello, {}".format(args.user_name))
