import helpers
import re

DAY = 7
PART = 1

def parse_line(line):
	operators = {
		"AND" 	: r"^(?P<lval>[\w]+)\s+AND\s+(?P<rval>[\w]+)\s+->\s+(?P<out>[\w]+)$",
		"NOT" 	: r"^NOT\s+(?P<lval>[\w]+)\s+->\s+(?P<out>[\w]+)$",
		"OR"  	: r"^(?P<lval>[\w]+)\s+OR\s+(?P<rval>[\w]+)\s+->\s+(?P<out>[\w]+)$",
		"LSHIFT": r"^(?P<lval>[\w]+)\s+LSHIFT\s+(?P<rval>[\w]+)\s+->\s+(?P<out>[\w]+)$",
		"RSHIFT": r"^(?P<lval>[\w]+)\s+RSHIFT\s+(?P<rval>[\w]+)\s+->\s+(?P<out>[\w]+)$",
		"ASSIGN": r"^(?P<lval>[\w]+)\s+->\s+(?P<out>[\w]+)$"

	}

	command = {}

	for key in operators:
		regex = operators[key]
		comp_re = re.compile(regex)
		match = comp_re.match(line)
		if not match:
			continue
		
		command["op"] = key
		command["lval"] = match.group("lval")
		command["out"] = match.group("out")

		if key in ["AND","OR","LSHIFT","RSHIFT"]:
			command["rval"] = match.group("rval")

	return command

def evaluate(circuit,root,store,verb=True):
	if verb: print "Currently @ " + root

	command = circuit[root]
	memoized = check_store(store,command)

	if not memoized == None:
		if verb: print "Retrieved from store: " + root
		return memoized

	lval = command["lval"]
	op = command["op"]


	if op == "ASSIGN":
		if lval.isdigit(): # fuckn' FINALLY!
			result = int(lval)
			if verb: print "Found: " + root + " Val: " + str(result)
			store.append((result,command))
			return result
		else:
			result = evaluate(circuit,lval,store,verb)
			store.append((result,command))
			return result

	if op == "NOT":
		if lval.isdigit():
			result = (1 << 16) - (int(lval)) -1
			if verb: print "Found: " + root + " Val: " + str(result) 
			store.append((result,command))
			return result
		else:
			result = (1 << 16) - evaluate(circuit,lval,store,verb) - 1
			store.append((result,command)) 
			return result


	if op == "AND":
		rval = command["rval"]
		
		if lval.isdigit() and rval.isdigit():
			result = int(lval) & int(rval)
			if verb: print "Found: " + root + " Val: " + str(result)
			store.append((result,command))
			return result

		if lval.isdigit():
			lhs = int(lval)
			rhs = evaluate(circuit,rval,store,verb)
			result = lhs & rhs
			store.append((result,command))
			return result

		if rval.isdigit():
			lhs = evaluate(circuit,lval,store,verb)
			rhs = int(rval)
			result = lhs & rhs
			store.append((result,command))
			return result

		lhs = evaluate(circuit,lval,store,verb)
		rhs = evaluate(circuit,rval,store,verb)
		result = lhs & rhs
		store.append((result,command))
		return result


	if op == "OR":
		rval = command["rval"]
		
		if lval.isdigit() and rval.isdigit():
			result = int(lval) | int(rval)
			if verb: print "Found: " + root + " Val: " + str(result)
			store.append((result,command))
			return result

		if lval.isdigit():
			lhs = int(lval)
			rhs = evaluate(circuit,rval,store,verb)
			result = lhs | rhs
			store.append((result,command))
			return result

		if rval.isdigit():
			lhs = evaluate(circuit,lval,store,verb)
			rhs = int(rval)
			result = lhs | rhs
			store.append((result,command))
			return result

		lhs = evaluate(circuit,lval,store,verb)
		rhs = evaluate(circuit,rval,store,verb)
		result = lhs | rhs
		store.append((result,command))
		return result

	if op == "LSHIFT":
		rval = command["rval"]

		if lval.isdigit() and rval.isdigit():
			result = int(lval) << int(rval)
			if verb: print "Found: " + root + " Val: " + str(result)
			store.append((result,command))
			return result

		if lval.isdigit():
			lhs = int(lval)
			rhs = evaluate(circuit,rval,store,verb)
			result = lhs << rhs
			store.append((result,command))
			return result

		if rval.isdigit():
			lhs = evaluate(circuit,lval,store,verb)
			rhs = int(rval)
			result = lhs << rhs
			store.append((result,command))
			return result

		lhs = evaluate(circuit,lval,store,verb)
		rhs = evaluate(circuit,rval,store,verb)
		result = lhs << rhs
		store.append((result,command))
		return result


	if op == "RSHIFT":
		rval = command["rval"]

		if lval.isdigit() and rval.isdigit():
			result = int(lval) >> int(rval)
			if verb: print "Found: " + root + " Val: " + str(result)
			store.append((result,command))
			return result

		if lval.isdigit():
			lhs = int(lval)
			rhs = evaluate(circuit,rval,store,verb)
			result = lhs >> rhs
			store.append((result,command))
			return result

		if rval.isdigit():
			lhs = evaluate(circuit,lval,store,verb)
			rhs = int(rval)
			result = lhs >> rhs
			store.append((result,command))
			return result

		lhs = evaluate(circuit,lval,store,verb)
		rhs = evaluate(circuit,rval,store,verb)
		result = lhs >> rhs
		store.append((result,command))
		return result

def check_store(store,command):
	for elem in store:
		val = elem[0]
		mem = elem[1]
		# the comparison might be a bit more clever (i.e.: a AND b == b AND a) ... too lazy.
		if cmp(command,mem) == 0:
			return val
	return None

def solution(f_obj):
	expression = {}
	store = []

	for line in f_obj:
		command = parse_line(line)
		key = command.pop("out")
		expression[key] = command

	
	return evaluate(expression,"a",store,verb=False)

helpers.solve(DAY,PART,solution,line_by_line=True)