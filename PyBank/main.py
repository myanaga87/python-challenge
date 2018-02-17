#import module
import os
import csv

csvpath = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "NUCHI201801DATA4-Class-Repository-DATA", "MWS", "Homework", "03-Python", "Instructions", "PyBank", "raw_data", "budget_data_1.csv")

#set empty lists
months = []
revenue = []

#read the csv
with open(csvpath, newline='') as data1:
    csvreader = csv.reader(data1, delimiter=',')

    #skip the header row
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        revenue.append(float((row[1])))

#find the total num of months in the dataset
    totalMonths = len(months)
    

#find the total amt of revenue gained over the entire period
    totalRevenue = (sum(revenue))    
    

#find the average change in revenue between months over the entire period
    avgChange = round(totalRevenue / totalMonths,2)
    

#find the greatest increase in revenue (date and amt) over the entire period
    greatestInc = float('-inf')
    for i in revenue:
        if i > greatestInc:
            greatestInc = i
    

#find the greatest decrease in revenue (date and amt) over the entire period
    greatestDec = 1195111
    for i in revenue:
        if i < greatestDec:
            greatestDec = i

#set up template
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+ str(totalMonths))
    print("Total Revenue: "+ str(totalRevenue))
    print("Average Revenue Change: "+ str(avgChange))
    print("Greatest Increase in Revenue: "+ str(greatestInc))
    print("Greatest Decrease in Revenue: "+ str(greatestDec))
    

#set up the output text file
output_file = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "python-challenge", "PyBank", "budget_data_Analysis.txt")

with open(output_file, 'w') as Analysis:
    Analysis.write("Financial Analysis\n")
    Analysis.write("-------------------------\n")
    Analysis.write("Total Months: "+ str(totalMonths)+"\n")
    Analysis.write("Total Revenue: "+ str(totalRevenue)+"\n")
    Analysis.write("Average Revenue Change: "+ str(avgChange)+"\n")
    Analysis.write("Greatest Increase in Revenue: "+ str(greatestInc)+"\n")
    Analysis.write("Greatest Decrease in Revenue: "+ str(greatestDec))


#empty the lists
months = []
revenue = []

#run the same process for the next file
csvpath = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "NUCHI201801DATA4-Class-Repository-DATA", "MWS", "Homework", "03-Python", "Instructions", "PyBank", "raw_data", "budget_data_2.csv")

with open(csvpath, newline='') as data2:
    csvreader = csv.reader(data2, delimiter=',')

    #skip the header row
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        revenue.append(float((row[1])))


#find the total num of months in the dataset
    totalMonths = len(months)
  

#find the total amt of revenue gained over the entire period
    totalRevenue = (sum(revenue))    
   

#find the average change in revenue between months over the entire period
    avgChange = round(totalRevenue / totalMonths,2)
    

#find the greatest increase in revenue (date and amt) over the entire period
    greatestInc = float('-inf')
    for i in revenue:
        if i > greatestInc:
            greatestInc = i
    

#find the greatest decrease in revenue (date and amt) over the entire period
    greatestDec = float(greatestInc)
    for i in revenue:
        if i < greatestDec:
            greatestDec = i
   

#set up template
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+ str(totalMonths))
    print("Total Revenue: "+ str(totalRevenue))
    print("Average Revenue Change: "+ str(avgChange))
    print("Greatest Increase in Revenue: "+ str(greatestInc))
    print("Greatest Decrease in Revenue: "+ str(greatestDec))


#set up the output text file
output_file = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "python-challenge", "PyBank", "budget_data_Analysis2.txt")

with open(output_file, 'w') as Analysis2:
    Analysis2.write("Financial Analysis\n")
    Analysis2.write("-------------------------\n")
    Analysis2.write("Total Months: "+ str(totalMonths)+"\n")
    Analysis2.write("Total Revenue: "+ str(totalRevenue)+"\n")
    Analysis2.write("Average Revenue Change: "+ str(avgChange)+"\n")
    Analysis2.write("Greatest Increase in Revenue: "+ str(greatestInc)+"\n")
    Analysis2.write("Greatest Decrease in Revenue: "+ str(greatestDec))

#empty the lists
months = []
revenue = []