import helpers

DAY = 10
PART = 2

def look_and_say(string):
	char_count = 1
	prev_char = string[0]
	new_str = ""
	
	for index in xrange(1,len(string)):
		curr_char = string[index]
		
		if curr_char == prev_char:
			char_count += 1
			continue

		to_concat = str(char_count) + prev_char if char_count else ""
		new_str += to_concat
		char_count = 1
		prev_char = curr_char


	to_concat = str(char_count) + prev_char if char_count else ""
	new_str += to_concat

	return new_str

def recurse_look_and_say(string,depth):
	if depth <= 0:
		return string

	current = look_and_say(string)
	return recurse_look_and_say(current,depth - 1)

def solution(input_string):
	new_string = recurse_look_and_say(input_string,50)
	result = len(new_string)

	return result

helpers.solve(DAY,PART,solution)

