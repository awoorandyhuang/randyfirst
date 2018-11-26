# example.py
from argparse import ArgumentParser
parser1 = ArgumentParser()
parser2 = ArgumentParser(prog="my_example")
parser3 = ArgumentParser(usage="usage")
parser4 = ArgumentParser(description="a simple demo of argparse")
parser5 = ArgumentParser(epilog="see the doc: https://docs.python.org/3/library/argparse.html")
parser1.print_help()
