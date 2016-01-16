import helpers
import re
import datetime

DAY = 9
PART = 2

def parse_line(line):
	pattern = r"^(?P<start>[\w]+)\s+to\s+(?P<end>[\w]+)\s+=\s+(?P<dist>[0-9]+).*$"
	comp = re.compile(pattern)
	match = comp.match(line)
	parsed = None

	if match:
		start = match.group("start")
		end = match.group("end")
		dist = int(match.group("dist"))
		parsed = (start,end,dist)

	return parsed

def update_map(current_map, links, new_link):
	start = new_link[0]
	end = new_link[1]
	dist = new_link[2]

	if not ( start in current_map ):
		current_map.append(start)

	if not ( end in current_map ):
		current_map.append(end)

	links.append(new_link)

# A tree is a list [ ROOT, [<tree list>] ]
def build_path_tree(root, current_map, depth, max_depth):
	if depth >= max_depth:
		return root
	
	visit = [ city for city in current_map if not city in root ] # TODO filter this properly ... 
	for city in visit:
		subtree = build_path_tree([city,[]], current_map, depth + 1, max_depth)
		root[1].append(subtree)

	return root

def generate_possible_paths(tree,current_path, path_store, current_depth):
	current_path.append(tree[0])
	for subtree in tree[1]:
		generate_possible_paths(subtree,current_path,path_store,current_depth + 1)
		path_store.append(current_path)
		current_path = current_path[:current_depth+1]

def find_hamiltonian_paths(possible_paths,current_map):
	ham_paths = []

	for path in possible_paths:
		visited = [ True if city in path else False for city in current_map ]
		is_hamiltonian = reduce(lambda x, y: x and y, visited)
		if is_hamiltonian and not path in ham_paths:
			ham_paths.append(path)

	return ham_paths

def get_link_distance(start,end,links):
	distance = 0 
	for link in links:
		if link[0] == start and link[1] == end:
			distance = link[2]

		if link[0] == end and link[1] == start:
			distance = link[2]

	return distance

def calculate_distance(path,links):
	distance = 0
	for index in xrange(len(path)-1):
		city = path[index]
		next_city = path[index + 1]
		distance += get_link_distance(city,next_city,links)

	return distance

# Sit back, pour yourself a glass of juice and start watching
# a show of your choice. After that, throw a dart on a world map,
# travel to that place, learn the language (or how to swim), have a good time and 
# come back ... It's gonna be a while before this comes up with an
# answer.
def solution(f_obj):
	start = datetime.datetime.now()
	current_map = []
	links = []
	for line in f_obj:
		new_link = parse_line(line)
		update_map(current_map, links, new_link)

	tree = ["Root",[]]
	build_path_tree(tree,current_map,0,len(current_map))
	possible_paths = []
	curr_path = []

	generate_possible_paths(tree,curr_path,possible_paths,0)
	ham_paths = find_hamiltonian_paths(possible_paths,current_map)
	distances = [ calculate_distance(path,links) for path in ham_paths ]
	longest = sorted(distances,reverse=True)[0] # not storing all distances to a file was a dumb idea.
	end = datetime.datetime.now()

	print "Ran for: {0}".format(end - start)
	return longest

helpers.solve(DAY,PART,solution,line_by_line=True)