import csv
import os

# file locations

file_to_load = os.path.join('Resources','budget_data.csv')

# check if the file path is correct
#print('my file is at {}'.format(file_to_load))
file_to_output = os.path.join('Analysis','budget_analysis.txt')


total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['',0]
total_net = 0


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    firstrow=next(reader)
    total_months = total_months+1
    total_net = total_net + int(firstrow[1])
    
    previous_net = int(firstrow[1])

    for row in reader:
        total_months = total_months+1  
        total_net = total_net + int(row[1])

        netchange = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [netchange]
        month_of_change = month_of_change + [row[0]]

        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange

        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange

net_monthly_avr = sum(net_change_list)/len(net_change_list)

output = (
    f'\nFinancial Analysis'
    f'\n----------------------------'
    f'\nTotal Months: {total_months}'
    f'\nTotal: ${total_net}'
    f'\nAverage  Change: ${net_monthly_avr}'
    f'\nGreatest Increase in Profits: {greatest_increase[0]} {greatest_increase [1]}'
    f'\nGreatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease [1]}'
)

print(output)
with open(file_to_output,'w') as txt_file:
    txt_file.write(output)


