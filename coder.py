#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pfp, pfp.fuzz
# import IPython

# import sys
# if __name__ == "__main__":
# 	#file = sys.argv[1]
# 	#print file

file = "input/date"

dom = pfp.parse(
	data_file = file,
	template_file = "ELF.bt"
)

# print dom._pfp__show()

class IntegersOnly(pfp.fuzz.StratGroup):
	name = "ints_only"

	class IntStrat(pfp.fuzz.FieldStrat):
		klass = pfp.fields.IntBase
		choices = [xrange(10)]

	def filter_fields(self, fields):
		return filter(lambda x: isinstance(x, pfp.fields.IntBase), fields)

counter = 0

for mutation in pfp.fuzz.mutate(dom, IntegersOnly, num=1, at_once=1):
	mutated = mutation._pfp__build()
	filename_out = "output/bin." + str(counter) + ".elf"
	with open(filename_out, 'wb') as file:
		file.write(bytes(mutated))
		file.close()
	m = mutated  # lazy typer.
	# IPython.embed()
	counter += 1
#print dom._pfp__error()
# IPython.embed()
