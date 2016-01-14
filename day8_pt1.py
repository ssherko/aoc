import helpers
import re

DAY = 8
PART = 1

def parse_line(line):
	escapes = [r"\\",r"\""] #priority
	new_line = r"" + line
	
	rep = len(new_line) - 1 # minus \n
	for esc in escapes:
		new_line = new_line.replace(esc,"~")

	deduct = new_line.count(r"\x")
	
	mem = len(new_line) - 3 - (deduct*(3))# minus the quotes and \n
	return rep, mem

def solution(f_obj):
	total_mem = 0
	total_rep = 0

	for line in f_obj:
		rep, mem = parse_line(line)
		total_mem += mem
		total_rep += rep
	
	return total_rep - total_mem

helpers.solve(DAY,PART,solution,line_by_line=True)