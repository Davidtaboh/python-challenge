# import CSV

import csv
import os

#read file in dictionary format

file_to_read = "C:/Users/david/Desktop/Python Challenge/python-challenge/PyBank/budget_file.csv"
file_to_write = os.path.join("budget_data.txt")

with open(file_to_read) as budget_file:
    budget_file = csv.reader(budget_file)

    header = next(budget_file)

#variables
    #first_row = next(budget_file)
    total_change_profits = 0
    greatest_increase = 0
    initial_profit = 0
    monthly_changes = []
    prev_net = int(first_row[1])
   

#Total Month

    totalrevenue = 0
    date_list = [] 

    for line in budget_file:
        date_list.append(line[0])
        net_change =  int(line[1]) - prev_net 
        prev_net = int(line[1])
        monthly_changes = monthly_changes + [net_change]
        totalrevenue =  totalrevenue + int(line[1])
        
print(len(date_list)+1)
print(totalrevenue + prev_net)
print(sum(monthly_changes) / len(monthly_changes))
print(max(monthly_changes))   
print(min(monthly_changes)) 
   

with open(file_to_write, "w") as txt_file:
    txt_file.write("hello")
