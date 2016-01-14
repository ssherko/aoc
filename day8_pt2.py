import helpers
import re

DAY = 8
PART = 2

def parse_line(line):
	actual = len(line) - 1 # remove the \n at the end
	encode = actual
	encode += (2+line.count('\\')+line.count('"')) # calculate the length increase
	return actual,encode



def solution(f_obj):
	actual_total = 0
	encoding_total = 0
	for line in f_obj:
		actual, encoding = parse_line(line)
		actual_total += actual
		encoding_total += encoding

	result = encoding_total - actual_total
	return result

helpers.solve(DAY,PART,solution,line_by_line=True)