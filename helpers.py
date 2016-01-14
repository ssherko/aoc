def print_stuff(day,part,args):
	if args == None:
		args = "!Not Implemented!"
	print "Advent Of Code (DAY {0}, PART {1}) - Result: {2}".format(day,part,args)

def solve(day,part,solution_funct,line_by_line=False):
	f = None
	if line_by_line:
		f = open("day{0}.txt".format(day))
	else:
		f = open("day{0}.txt".format(day)).read()

	out = solution_funct(f)
	print_stuff(day,part,out)
