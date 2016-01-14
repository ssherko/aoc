import helpers

DAY = 3
PART = 1

def position_repr(x,y):
	return "{0},{1}".format(x,y)

def move(x,y,symbol):
	if symbol == "^":
		return x,y+1
	if symbol == "v":
		return x,y-1
	if symbol == ">":
		return x+1,y
	if symbol == "<":
		return x-1,y

	return None,None # should be interpreted as Error.

def solution(input_string):
	houses = {}
	x = 0
	y = 0
	start = position_repr(x,y)
	houses[start] = 1

	for char in input_string:
		x,y = move(x,y,char) # too lazy. 
		new_pos = position_repr(x,y)

		if houses.has_key(new_pos):
			houses[new_pos] += 1
		else:
			houses[new_pos] = 1

	return len(houses)

helpers.solve(DAY,PART,solution)