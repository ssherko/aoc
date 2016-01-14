import helpers

DAY = 3
PART = 2

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
	santa_houses = {}
	robo_santa_houses = {}
	turn = 0
	
	x_s = 0
	y_s = 0

	x_r = 0
	y_r = 0 

	start = position_repr(x_s,y_s) # doesn't matter
	
	santa_houses[start] = 1
	robo_santa_houses[start] = 1

	for char in input_string:
		
		if turn % 2 == 0: # santas turn
			x_s,y_s = move(x_s,y_s,char)
			santa_new_pos = position_repr(x_s,y_s)
			if santa_houses.has_key(santa_new_pos):
				santa_houses[santa_new_pos] += 1
			else:
				santa_houses[santa_new_pos] = 1
		else: # robo_santas turn
			x_r,y_r = move(x_r,y_r,char)
			rsanta_new_pos = position_repr(x_r,y_r)
			if robo_santa_houses.has_key(rsanta_new_pos):
				robo_santa_houses[rsanta_new_pos] += 1
			else:
				robo_santa_houses[rsanta_new_pos] = 1

		turn += 1

	from_santa = dict(santa_houses)
	from_santa.update(robo_santa_houses)

	return len(from_santa)

helpers.solve(DAY,PART,solution)