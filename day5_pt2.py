import helpers

DAY = 5
PART = 2

def is_nice(string):
	rule1 = False # a group of two letters that appear twice in a row (i.e.:"xzxz")
	rule2 = False # a letter that appears twice with a letter inbetween (i.e.: "xzx")

	for i in xrange(1,len(string)-1):
		low = i - 1
		high = i + 1
		if string[low] == string[high]:
			rule2 = True
			break

	for i in xrange(len(string)-1):
		high = i + 1
		seq = string[i:high+1] # damn you slices.
		tail = string[high+1:]
		if seq in tail:
			rule1 = True
			break

	return (rule1 and rule2)


def solution(f_obj):
	total = 0
	for line in f_obj:
		if is_nice(line):
			total += 1

	return total

helpers.solve(DAY,PART,solution,line_by_line=True)
