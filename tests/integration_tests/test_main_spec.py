import sys,os,inspect
import add_and_multiply
from nose.tools import *
from describe_it import describe, it

@describe
def integration_tests():

	@it
	def can_run_main():
		"""Test main function"""
		assert_equals(add_and_multiply.main(2,3,4),20)

	@it
	def can_parse_args():
		"""Test argument parsing"""
		argv = '-f 2 -s 3 -t 4'.split()
		options = add_and_multiply.parse_args(argv)
		assert_equals(options.first,2)
		assert_equals(options.second,3)
		assert_equals(options.third,4)