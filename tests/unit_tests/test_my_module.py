import sys,os,inspect
from modules import my_module
from nose.tools import *
def test_add_numbers():
	"""Test addition works"""
	assert_equals(my_module.add_numbers(1,2),3)
def test_add_number_failure():
	"""Test addition where answer is false"""
	assert_not_equals(my_module.add_numbers(1,3),3)

def test_a_few_numbers():
	"""test a few sums"""
	for numbers, answer in [[(1,2),3], [(2,2),4], [(5,6), 11]]:
		yield sum_with_answer, numbers[0], numbers[1], answer
def sum_with_answer(first,second,answer):
	print(first)
	assert_equals(my_module.add_numbers(first,second), answer)

def test_multiply_numbers():
	"""Test multiply works"""
	assert_equals(my_module.multiply_numbers(2,2),4)