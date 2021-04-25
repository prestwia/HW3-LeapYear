# Program: alexander_prestwich_hw1.py
# Author: Alexander Prestwich
# Date: 4/11/2021
# Class: CS 362
# Description: Program takes integer input from user
#				prints if it is a leap year or not

#Instructions to run on server:
#paste: python alexander_prestwich_hw1.py


print("Determine if year is a leap year.")

while True:
	while True:
		try:
			year = int(input("Enter year: "))
			break
		except:
			print("Enter an integer")
	if (year >= 1):
		break
	else:
		print("Enter a positive year > 0")

isLeap = False
if (year % 4 == 0):
	isLeap = True
	if (year % 100 == 0):
		isLeap = False
		if (year % 400 == 0):
			isLeap = True

if (isLeap):
	print(str(year) + " is a leap year")
else:
	print(str(year) + " is not a leap year")


