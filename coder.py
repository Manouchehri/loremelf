#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pfp, pfp.fuzz
import sys
import IPython

# file = None

# if __name__ == "__main__":
# 	pass
# 	#file = sys.argv[1]
# 	#print file

file = "input/date"

dom = pfp.parse(
	#keep_successful=True,
	# predefines=None,
	#printf=False,
	# interp=None,
	#debug=True,
	# int3=None,
	data_file = file,
	template_file = "ELF.bt"
)

# print dom._pfp__show()

class IntegersOnly(pfp.fuzz.StratGroup):
	name = "ints_only"

	class IntStrat(pfp.fuzz.FieldStrat):
		klass = pfp.fields.IntBase
		choices = [0, 1, 2, 3]

	def filter_fields(self, fields):
	 	return filter(lambda x: isinstance(x, pfp.fields.IntBase), fields)

counter = 0

for mutation in pfp.fuzz.mutate(dom, IntegersOnly, num=10, at_once=10):
	mutated = mutation._pfp__build()
	filename_out = "output/bin." + str(counter) + ".elf"
	with open(filename_out, 'w') as file:
		file.write(mutated)
	
	counter += 1
#print dom._pfp__error()
# IPython.embed()
