import helpers
import re

DAY = 6 
PART = 1

OFF = 0
ON = 1 
TOG = 2

def parse_line(line):
	c_re = r"(?P<command>[\w]+\s*\w*)\s+"
	tl_re = r"(?P<top_left>[\d]+,[\d]+)"
	br_re = r"(?P<bottom_right>[\d]+,[\d]+)"
	filler_re = r"\s+.*\s+"
	
	instruction_regex = r"^" + c_re + tl_re + filler_re + br_re + r"$"
						
	comp_regex = re.compile(instruction_regex)
	match = comp_regex.match(line)
	assert(match != None) # this shouldn't happen

	action = None
	if "turn off" in match.group("command"):
		action = OFF

	if "turn on" in match.group("command"):
		action = ON

	if "toggle" in match.group("command"):
		action=TOG

	tl_coord = map(int,match.group("top_left").split(","))
	br_coord = map(int,match.group("bottom_right").split(","))

	command = (action,tl_coord,br_coord)

	return command

def evaluate(command,grid):
	action = command[0]
	tl_coord = command[1]
	br_coord = command[2]
	
	x_tl = tl_coord[0]
	y_tl = tl_coord[1]

	x_br = br_coord[0]
	y_br = br_coord[1]

	# find the other points.
	x_bl = x_tl
	y_bl = y_br

	x_tr = x_br
	y_tr = y_tl

	for i in xrange(x_tl,x_tr + 1):
		for j in xrange(y_tl,y_bl + 1):
			if action == ON:
				grid[i][j] = True
			if action == OFF:
				grid[i][j] = False
			if action == TOG:
				grid[i][j] = not grid[i][j]

def check_status(grid):
	lit = 0
	for row in grid:
		for element in row:
			if element:
				lit += 1	
	return lit

def solution(f_obj):
	grid = [ [ False for x in xrange(1000) ] for x in xrange(1000) ]

	for line in f_obj:
		command = parse_line(line)
		evaluate(command,grid)

	return check_status(grid)

helpers.solve(DAY,PART,solution,line_by_line=True)