import helpers

DAY = 1
PART = 2

def solution(instruction_string):
	floor = 0
	position = 0 
	for i in xrange(len(instruction_string)):
		instruction = instruction_string[i]
		
		if instruction == "(":
			floor += 1

		if instruction == ")":
			floor -= 1

		if floor < 0:
			position = i + 1
			break

	return position 

helpers.solve(DAY,PART,solution)
