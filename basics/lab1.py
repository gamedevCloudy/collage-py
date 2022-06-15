#!/usr/local/bin/python3

basic = float(input("Enter salary of the employee:- "))

hra = basic * .1
ta = basic * .05

gross = basic + hra + ta
print("Gross Salary: ", gross)
prof_tax = gross*.02
calc = gross - prof_tax

print("Total Salary: ", calc  )
