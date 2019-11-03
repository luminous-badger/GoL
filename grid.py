#!/usr/bin/python

# Print a grid of stars or spaces. Game of Life first attempt.
# JM Sun  3 Nov 2019 14:59:12 GMT

import random

random.seed()
golarray = []
for cols in range( 1, 11 ):
	rowarray = []
	for rows in range( 1, 11 ):
		if ( random.random() < 0.5 ):
			rowarray.append( '*' )
			print '*', 
		else:
			rowarray.append( ' ' )
			print ' ', 
	golarray.append( rowarray )
	print

print '----=====****====----'
print
for xrows in ( golarray ):
	print xrows
