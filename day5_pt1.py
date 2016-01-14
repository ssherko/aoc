import helpers

DAY = 5
PART = 1

VOWELS = "aeiou"
NOT_ALLOWED = ["ab","cd","pq","xy"]

def is_nice(string):
	
	vowels = False
	in_a_row = False
	not_nice = False

	for ch in NOT_ALLOWED:
		if ch in string:
			not_nice = True
			break

	vowel_count = 0 
	for ch in string:
		if ch in VOWELS:
			vowel_count += 1
	vowels = vowel_count >= 3
	last = None # will hold string.
	for ch in string:
		if last == ch:
			in_a_row = True
			break

		last = ch

	return (vowels and in_a_row and (not not_nice))


def solution(f_obj):
	total = 0
	for line in f_obj:
		if is_nice(line):
			total += 1

	return total

helpers.solve(DAY,PART,solution,line_by_line=True)
