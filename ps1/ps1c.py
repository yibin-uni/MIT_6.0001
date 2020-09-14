#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:21:10 2019

@author: yibin
"""
annual_salary=int(input("Enter the starting salary: "))
total_cost=1000000
semi_annual_raise=0.07
portion_down_payment=0.25
current_savings=0
r=0.04
initial=annual_salary
low = 0
high = 10000
guess =(low + high)/2
epsilon = 100
num_guess = 0

for i in range(37):
    current_savings = current_savings*(1+r/12)+ annual_salary/12*guess/10000
    if i>0 and i%6==0:
        annual_salary *= (1+semi_annual_raise)
    
while abs(current_savings - total_cost * portion_down_payment) >= epsilon:
    if current_savings - total_cost * portion_down_payment > 0: 
        high = guess
    else: 
        low = guess
    guess= (low + high)/2
    num_guess +=1
    current_savings=0
    annual_salary=initial
    for i in range(37):
        current_savings = current_savings*(1+r/12)+ annual_salary/12*guess/10000
        if i>0 and i%6==0:
            annual_salary *= (1+semi_annual_raise)

print("Best savings rate:", guess/10000)
print("Steps in bisection search:", num_guess)




