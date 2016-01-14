import helpers

DAY = 1
PART = 1

def solution(instruction_string):
	floor = 0
	for instruction in instruction_string:
		if instruction == "(":
			floor += 1

		if instruction == ")":
			floor -= 1

	return floor

helpers.solve(DAY,PART,solution)