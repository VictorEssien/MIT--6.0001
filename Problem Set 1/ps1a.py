# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:22:40 2021

@author: Victor
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_salary = annual_salary/12

monthly_savings = monthly_salary * portion_saved

total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25   #25%
down_payment = portion_down_payment * total_cost

r = 0.04
current_savings = 0.0

number_of_months = 0

while current_savings < down_payment:
    current_savings += (monthly_savings + (current_savings * (r/12)))
    number_of_months += 1
    if current_savings == down_payment:
        break
    
print("Number of months:",number_of_months)    
#print(current_savings) - to find the current savings available
