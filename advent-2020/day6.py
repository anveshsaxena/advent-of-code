#Day 6 Part 1 Advent of Code
import sys

#To save answers for each group and then flush for next
answer_list = ""
sum = 0
for group_line in sys.stdin:
	line = group_line.rstrip("\n")
	if line == "":
		#print(len(set(list(answer_list))))
		sum += len(set(list(answer_list)))
		answer_list = ""
	else:
		answer_list += line
		
print(sum)
