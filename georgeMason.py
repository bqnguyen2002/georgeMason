# Python program to read
# json file

import json
 
# Opening JSON file
f = open('APCredits.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list

ap_exams = []
for i in data['credit_transfer']:
    if(i['ap_exam'] not in ap_exams):
        ap_exams.append(i['ap_exam'])
 
# Closing file
f.close()

switch = 0
ask_again = 0

print('\n' + 'Options: ' + '\n')
for i in ap_exams:
    print(i + "\n")

user_classes = []
user_scores = []

while switch == 0:
    ap_courses = input("What AP Course do you want to transfer?: ")
    if ap_courses in (ap_exams):
        ask_again = 0
        switch = 1
        while switch == 1:
            ap_credits = input("What score did you receive on " + ap_courses + " (3 - 5): ")
            if(ap_credits == '3' or ap_credits == '4' or ap_credits == '5'):
                user_classes.append(ap_courses)
                user_scores.append(ap_credits)
                switch = 0
            else:
                print("Invalid AP Score! Please enter a score 3 - 5")
        while ask_again == 0:
            option = input("Would you like to input any more classes (Y/N)? ")
            if(option == 'N' or option == 'n'):
                switch = 2
                ask_again = 1
            elif(option == 'Y' or option == 'y'):
                switch = 0
                ask_again = 1
            else:
                print("Invalid input! Please enter Y or N ")
    print("Invalid AP Course!")
print(user_classes)
print(user_scores)

print('calculating scores...')
total = 0
for i in data['credit_transfer']:
    for j in range(len(user_classes)):
        if(i['ap_exam'] == user_classes[j] and i['minimum_score'] == user_scores[j]):
            total += int(i['credits'])
print("You will be able to receive " + str(total) + " transfer credits from GMU based on your AP Scores!")

    
