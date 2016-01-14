import helpers

DAY = 2
PART = 1

def get_params(line):
	dimensions = line.split("x")
	length = dimensions[0]
	width = dimensions[1]
	height = dimensions[2]

	length = int(float(length))
	width = int(float(width))
	height = int(float(height))

	return length,width,height

def get_surface_area(length,width,height):
	top = width * length
	front = length * height
	side = height * width

	slack = min([top,front,side])

	total_area = (top+front+side) * 2
	
	return (total_area + slack)

def solution(file_obj):
	total = 0
	for line in file_obj:
		l,w,h = get_params(line)
		total += get_surface_area(l,w,h)

	return total

helpers.solve(DAY,PART,solution,line_by_line=True)