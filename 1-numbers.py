#!/usr/bin/python

import sys, logging, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


def is_leap_year(year):
	leap = False
	try:
		if year % 400 == 0:
			leap = True
		elif year % 100 == 0:
			leap = False
		elif year % 4 == 0:
			leap = True
	except TypeError:
		leap = False
	return leap

def main():
	years = []

	for i in range(100):
		years.append(random.randrange(1900,2100))

	for y in years:
		if is_leap_year(y):
			print('{0}: I get an extra day this year!'.format(y))
		else:
			print(str(y) + ': Just 365 for me')

if __name__ == '__main__':
	main()