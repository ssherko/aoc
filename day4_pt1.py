import helpers
import hashlib

DAY = 4 
PART = 1 

def check_prefix(string):
	for char in string:
		if not char == "0":
			return False

	return True

def solution(input_string):
	found = False
	key = 0

	while not found:
		to_hash = input_string + str(key)
		my_hash = hashlib.md5(to_hash).hexdigest()
		if check_prefix(my_hash[0:5]):
			found = True
			continue

		key += 1

	return key

helpers.solve(DAY,PART,solution)