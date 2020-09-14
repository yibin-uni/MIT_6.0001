#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:07:12 2019

@author: yibin
"""

annual_salary=int(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=int(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal:"))
portion_down_payment=0.25
current_savings=0
r=0.04
n=0
while current_savings < total_cost*portion_down_payment:
    current_savings = current_savings*(1+r/12)+ annual_salary/12*portion_saved
    n+=1
    if n%6==0:
        annual_salary= annual_salary*(1+semi_annual_raise)


print("Number of months:", n)