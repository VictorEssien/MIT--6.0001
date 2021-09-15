# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:22:40 2021

@author: Victor
"""


def find_best_rate():
    """ 
    Input: Annual salary, semi-annual raise, cost of home
    Assumes: a time frame of three years (36 months), a down payment of 25% of the total cost, 
    current savings starting from 0 and annual return of 4%
    Returns the best savings rate within (plus/minus) $100 of the downpayment, and bisection search
    else returns false if result is not possible
    
    """
    annual_salary = float(input("Enter your annual salary: "))
    total_cost = float(1000000)
    semi_annual_raise = float(0.07)
    
    monthly_salary = annual_salary/12
    r = 0.04
    down_payment = 0.25 * total_cost
    current_savings = 0
    time = 36
    
    epsilon = 100
    low = 0
    high = 10000
    savings_rate = (low + high)//2
    num = 0
    
    while abs(current_savings - down_payment) >= epsilon:
        mod_annual_salary = annual_salary  #The annual salary we will use to modify/ make changes
        current_savings = 0
        portion_saved = savings_rate/10000  #Converting our floor/ int division to decimal (as a portion to save)
        
        for month in range(1, time+1):
            if month % 6 == 0:
                mod_annual_salary += (annual_salary * semi_annual_raise)
            
            monthly_salary = mod_annual_salary/12
            monthly_savings = monthly_salary * portion_saved
            additional = monthly_savings + (current_savings * r/12) #Additional return considering monthly and current savings
            current_savings += additional
        
        #Bisection search 
        if current_savings < down_payment:
            low = savings_rate
        else:
            high = savings_rate
        
        savings_rate = (low + high)//2
        num += 1
        
        if num > 15:  #Log_2 (10000) is 13.28... it will not make sense to keep searching after this point
            break
            
    if num < 15:
        print("Best Savings Rate: {} or {}%".format(portion_saved, portion_saved*100)),
        print("Steps in bisection Search: {}".format(num))
        return portion_saved
    else:
        return("It is not possible to pay the down payment in three years")
        
        
    