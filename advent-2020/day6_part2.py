#Day 6 Part 1 Advent of Code
import sys

def count_char(group_ans, num_of_ppl):
	""" Counts the number of characters that are selected by all in the group
		Checks if count for the character is equal to num_of_ppl"""
	unique = 0
	for character in set(list(group_ans)):
		if group_ans.count(character) == num_of_ppl:
			unique += 1
		#print(character + " " + str(group_ans.count(character))+ " " + str(num_of_ppl))
	return unique

#To save answers for each group and then flush for next
answer_list = ""
sum = 0
people_in_grp = 0
for group_line in sys.stdin:
	line = group_line.rstrip("\n")
	if line == "":
		#print(count_char(answer_list, people_in_grp))
		sum += count_char(answer_list, people_in_grp)
		#reset for the next group
		people_in_grp = 0
		answer_list = ""
	else:
		answer_list += line
		people_in_grp += 1
print(sum)
