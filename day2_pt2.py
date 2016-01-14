import helpers

DAY = 2
PART = 2

def get_params(line):
	dimensions = line.split("x")
	length = dimensions[0]
	width = dimensions[1]
	height = dimensions[2]

	length = int(float(length))
	width = int(float(width))
	height = int(float(height))

	return length,width,height

def get_ribbon_length(length,width,height):
	front = (length + height) * 2 
	top = (length + width) * 2 
	side = (height + width) * 2

	ribbon_length = min([front, top, side])
	bow_length = (length * width * height)

	total = ribbon_length + bow_length

	return total

def solution(file_obj):
	total = 0

	for line in file_obj:
		l,w,h = get_params(line)
		total += get_ribbon_length(l,w,h)
	
	return total

helpers.solve(DAY,PART,solution,line_by_line=True)
