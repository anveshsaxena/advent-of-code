import sys
import math #for ceil and floor functions

def row_search(seat):
	upper = 127
	lower = 0
	for character in seat[0:7]:
		if character == "F":
			upper = math.floor((lower + upper)/2)
		elif character == "B":
			lower = math.ceil((lower+upper)/2)
		#print("Character {} Lower {} Upper {}".format(character, lower, upper))
	return upper

def column_search(seat):
	right = 7
	left = 0
	#print(seat[-3:])
	for character in seat[-3:]:
		if character == "R":
			left = math.ceil((right+left)/2)
		elif character == "L":
			right = math.floor((right+left)/2)
		#print("Character {} left {} right {}".format(character, left, right))
	return right

highest = 0
seat_list = []
full_seats = range(0,1023)
for boarding_pass in sys.stdin:
		#print(row_search(boarding_pass.rstrip("\n")))
		#print(column_search(boarding_pass.rstrip("\n")))
		#print(row_search(boarding_pass.rstrip("\n")) * 8 + column_search(boarding_pass.rstrip("\n")))
		seat_list.append(row_search(boarding_pass.rstrip("\n")) * 8 + column_search(boarding_pass.rstrip("\n")))
		if highest < row_search(boarding_pass.rstrip("\n")) * 8 + column_search(boarding_pass.rstrip("\n")):
			highest = row_search(boarding_pass.rstrip("\n")) * 8 + column_search(boarding_pass.rstrip("\n"))

print(highest)
print(len(seat_list))
print(set(full_seats) - set(seat_list))
