#Day 3- Advent of Code 2020
import sys

def slope_calc(data, right, down):
	tree = 0
	open_space = 0
	first = True
	position = right
	line_count = 0
	
	for line in data:
		if line != "":
			line_read = line.rstrip("\n")
			if first:
				first = False
			else:
				if line_count % down == 0:
					if line_read[position] == ".":
						open_space += 1
					else:
						if line_read[position] == "#":
							tree += 1
					position += right
					if position > len(line_read)-1:
						position = position-len(line_read)
		line_count += 1
	
	print("Tree = {}, Open = {}".format(tree, open_space))
	return tree

data = []
for line in sys.stdin:
	data.append(line.rstrip("\n"))
	
print(slope_calc(data,1,1) * slope_calc(data,3,1) * slope_calc(data,5,1) * slope_calc(data,7,1) * slope_calc(data,1,2))
