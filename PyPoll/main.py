#set dependencies
import os
import csv

csvpath = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "NUCHI201801DATA4-Class-Repository-DATA", "MWS", "Homework", "03-Python", "Instructions", "PyPoll", "raw_data", "election_data_2.csv")

#set empty lists
voter_id = []
county = []
candidate = []

#read the csv
with open(csvpath, newline='') as election1:
    csvreader = csv.reader(election1, delimiter=',')
    
    #skip the header row
    next(csvreader, None)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
#The total number of votes cast
    totalVotes = len(voter_id)

#A complete list of candidates who received votes
    candidate_list = []
    for x in candidate:
        if x not in candidate_list:
            candidate_list.append(x)


#The total number of votes each candidate won

    
    candidate1 = 0
    for i in candidate:
        if i == str(candidate_list[0]):
            candidate1 += 1
    
    candidate2 = 0
    for j in candidate:
        if j == str(candidate_list[1]):
            candidate2 += 1
    
    candidate3 = 0
    for k in candidate:
        if k == str(candidate_list[2]):
            candidate3 += 1
    
    candidate4 = 0
    for m in candidate:
        if m == str(candidate_list[3]):
            candidate4 += 1
    

#The percentage of votes each candidate won
    percent1 = round(candidate1 / totalVotes * 100,0)
    percent2 = round(candidate2 / totalVotes * 100,0)
    percent3 = round(candidate3 / totalVotes * 100,0)
    percent4 = round(candidate4 / totalVotes * 100,0)

#The winner of the election based on popular vote

    if candidate1 > candidate2 and candidate1 > candidate3 and candidate1 > candidate4:
        winner = str(candidate_list[0])
    elif candidate2 > candidate1 and candidate2 > candidate3 and candidate2 > candidate4:
        winner = str(candidate_list[1])
    elif candidate3 > candidate1 and candidate3 > candidate2 and candidate3 > candidate4:
        winner = str(candidate_list[2])
    elif candidate4 > candidate1 and candidate4 > candidate2 and candidate4 > candidate3:
        winner = str(candidate_list[3])
    else:
        print("there must be a tie somehow.")

#print election results
    print("Election Results")
    print("--------------------------")
    print("Total Votes: "+ str(totalVotes))
    print("--------------------------")
    print(str(candidate_list[0])+ ": "+str(percent1)+"% "+"("+str(candidate1)+")")
    print(str(candidate_list[1])+ ": "+str(percent2)+"% "+"("+str(candidate2)+")")
    print(str(candidate_list[2])+ ": "+str(percent3)+"% "+"("+str(candidate3)+")")
    print(str(candidate_list[3])+ ": "+str(percent4)+"% "+"("+str(candidate4)+")")
    print("--------------------------")
    print("Winner is "+ str(winner))
    print("--------------------------")

#set up the output text file and print results
text_file = os.path.join("C:/", "Users", "Yanagam", "Desktop", "DataScience", "python-challenge", "PyPoll", "ElectionResults2.txt")

with open(text_file, 'w') as Results:
    Results.write("Election Results\n")
    Results.write("--------------------------\n")
    Results.write("Total Votes: "+ str(totalVotes)+"\n")
    Results.write("--------------------------\n")
    Results.write(str(candidate_list[0])+ ": "+str(percent1)+"% "+"("+str(candidate1)+")\n")
    Results.write(str(candidate_list[1])+ ": "+str(percent2)+"% "+"("+str(candidate2)+")\n")
    Results.write(str(candidate_list[2])+ ": "+str(percent3)+"% "+"("+str(candidate3)+")\n")
    Results.write(str(candidate_list[3])+ ": "+str(percent4)+"% "+"("+str(candidate4)+")\n")
    Results.write("--------------------------\n")
    Results.write("Winner is "+ str(winner)+"\n")
    Results.write("--------------------------")