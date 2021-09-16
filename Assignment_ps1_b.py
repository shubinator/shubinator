#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:19:07 2021

@author: shubhamchohda
"""
"""
Part B: saving with raise 

Every 6 months the company gives a raise. 



"""
# Below numbers are all assumptions you can edit them to your needs.  




annual_salary = float(input( "You are annual salary:$ ")) # $ my annual salary 
saved_portion = float(input( "The percenatge of your salary you want to save:$ "))
total_cost = float(input( "Total cost of your dream home:$ "))
semi_annual_raise = float(input( "% of salary increase every 6 months.  "))

monthly_salary = annual_salary/12

down_payment_portion =0.25*total_cost #  Assumed 25 %  needed for down payment 

current_savings = 0 #$ My current savings. This is true in real life lool. 


#print(f"My savings at month 0: {savings_each_month}")

 # % interest rate / month from the bank on my saving accound deposit.
counter = 0 
while current_savings<= down_payment_portion:
    
    if counter %6 ==0 and counter != 0 : 
        monthly_salary += semi_annual_raise *monthly_salary 
        
    monthly_interest= (0.04*current_savings)/12  #  % of monthly salary saved 
    #print(f"ROI: {monthly_interest}")
    savings_each_month= monthly_salary* saved_portion    
    current_savings += savings_each_month + monthly_interest
    counter +=1 
    
       
        
    #print( f"My current savings: {current_savings} at month: {counter}")
    #print(f"New monthly salary : {monthly_salary}")
   

print(f"No of months: {counter}")


