import sys

def decode(query):

	'''
	INPUT: takes a specific kind of coded statement
	OUTPUT: decodes into integer

	idea came from a /r/puzzles post
	screenshot included in directory

	examples:

	6 - S
	SIX - S = IX = 9

	5 - E - F
	FIVE - E - F = IV = 4

	11 - 3E - N
	ELEVEN - 3E - N = LV = 55

	rules:

	- first instruction is an integer
	- letters can be subtracted
	- multiples of letters can be subtracted

	'''

	int_to_eng = {5:'five',6:'six',7:'seven',8:'eight',9:'nine',11:'eleven'}
	

	instructions = query.split()
	ins_count = len(instructions)

	if ins_count % 2 == 0:
		sys.ext(f"incorrect number of instructions {ins_count}\nexiting")
	
	# parse first instruction into integer
	try:
		first_ins = int(instructions[0])
	except:
		sys.exit(f"first instruction {instructions[0]} was not an integer\nexiting")

	# look up integer in dictionary
	if first_ins in int_to_eng:
		eng = int_to_eng[first_ins]
	else:
		sys.exit(f"integer {first_ins} wasn't in dictionary\nexiting")

	instructions = instructions[1:]
	ins_count -= 1

	while ins_count > 0:
		if instructions[0] != '-':
			sys.exit(f"instruction {instructions[0]} is not subtraction\nexiting")
		else:


	