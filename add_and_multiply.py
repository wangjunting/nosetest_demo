#!/usr/bin/env python
import sys, os, inspect
import argparse
from modules import my_module

def main(first, second, third):
	sum = my_module.add_numbers(first,second)
	product = my_module.multiply_numbers(sum, third)
	print(product)
	return product


def parse_args(args):

	parser = argparse.ArgumentParser(description='Simple app to add and them multiply')

	parser.add_argument('--first', '-f', action="store", required=True, type=int)
	parser.add_argument('--second', '-s', action="store", required=True, type=int)
	parser.add_argument('--third', '-t', action="store", required=True, type=int)

	return parser.parse_args(args)

if __name__ == "__main__":
	options = parse_args(sys.argv[1:])
	main(options.first, options.second, options.third)
