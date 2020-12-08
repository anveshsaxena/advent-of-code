# Day 4 Advent of Code
import sys

def check_passport(passport):
	""" Check if the passport has required fields"""
	return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

data = ""
valid = 0

for line in sys.stdin:
	if line.rstrip("\n") == "":
		if check_passport(data):
			valid += 1
		data = ""
	else:
		data = data + " " + line.rstrip("\n")

print("Valid Passports = {}".format(valid))
