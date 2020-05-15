import sys

def roman_to_int(roman):

	'''
	INPUT: roman numeral string
	OUPUT: integer
	'''

	output = 0

	# short dictionary of roman to integer conversions
	single_roman = {'i':1,'v':5,'x':10,'l':50}

	# convert roman sequence to integer sequence
	try:
		int_seq = [single_roman[r] for r in roman]
	except:
		sys.exit(f"{roman} contains letter that is not a roman numeral\nexiting")

	# return if single number
	if len(int_seq) == 1:
		return int_seq[0]

	# start with total sum
	output = sum(int_seq)

	# go through and find if any number precedes one that is greater
	# if so we subtract it twice from the total to account for subraction notation
	# not optimal at scale
	i = 0
	while i < len(int_seq) - 1:
		if int_seq[i] < int_seq[i+1]:
			output -= 2*int_seq[i]
		i += 1

	return output



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

	if len(instructions) % 2 == 0:
		sys.ext(f"incorrect number of instructions {len(instructions)}\nexiting")
	
	# grab first instruction
	first_ins = instructions.pop(0)

	# attempt parse to integer
	try:
		first_ins = int(first_ins)
	except:
		sys.exit(f"first instruction {first_ins} was not an integer\nexiting")

	# look up integer in dictionary
	if first_ins in int_to_eng:
		eng = int_to_eng[first_ins]
	else:
		sys.exit(f"integer {first_ins} wasn't in dictionary\nexiting")

	while len(instructions) >= 2:

		# should be a '-'
		minus_ins = instructions.pop(0)

		# test for minus sign
		if minus_ins != '-':
			sys.exit(f"instruction {minus_ins} is not subtraction\nexiting")

		# grab instruction
		ins = instructions.pop(0)

		# test that instruction is correct length
		if len(ins) != 1 and len(ins) != 2:
			sys.exit(f"length of instruction {ins} is not correct\nexiting")

		# procedure for compound instruction
		if len(ins) == 2:

			# integer instruction
			int_ins = ins[0]

			# character instruction
			char_ins = ins[1].lower()

			# test that the first character of the instruction is an integer
			try:
				int_ins = int(int_ins)
			except:
				sys.exit(f"instruction {int_ins} was not an integer\nexiting")

			if char_ins.isalpha():
				eng = eng.replace(char_ins,'',int_ins)

			else:
				sys.exit(f"instruction {char_ins} is not a letter\nexiting")

		# procedure for simple instruction
		else:

			if ins.isalpha():
				eng = eng.replace(ins.lower(),'',1)

	# convert remaining letters from roman numerals to integer
	output = roman_to_int(eng)	

	return output

def test_suite():
	passed = True

	tests = {'6 - S':9,'5 - E - F':4,'11 - 3E - N':55}

	for item in tests.items():
		if decode(item[0]) != item[1]:
			print(f"failed {item[0]} test")
			passed = False
		else:
			print(f"passed {item[0]} test")

	if passed:
		print("passed all tests")


	