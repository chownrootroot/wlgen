# ------------------------------
# Wordlist generator
# ------------------------------

import time
import sys

def remove(duplicate): 
    final_list = []
    iCurrent = 0
    iLength = len(duplicate) 
    sys.stdout.write("Removing duplicates from wordlist...\n")
    for strng in duplicate:
        iCurrent += 1
        iPercent = (iCurrent * 100) / iLength
        sys.stdout.write("\r%d%%" % iPercent)  
        sys.stdout.flush()
#        sys.stdout.write("Progress: " + str(iPercent) + "\n")
        if strng not in final_list: 
            final_list.append(strng) 
    return final_list 

# ------------------------------
# Declarations
# ------------------------------
strFirstName = ""
strLastName = ""
strYear = ""
strMonth = ""
strDay = ""
strLast4 = ""
strPartnerFirstName = ""
strPartnerLastName = ""
strPartnerYear = ""
strPartnerMonth = ""
strPartnerDay = ""
strPartnerLast4 = ""
strChild1FirstName = ""
strChild1LastName = ""
strChild1Year = ""
strChild1Month = ""
strChild1Day = ""
strChild1Last4 = ""
strChild2FirstName = ""
strChild2LastName = ""
strChild2Year = ""
strChild2Month = ""
strChild2Day = ""
strChild2Last4 = ""
strChild3FirstName = ""
strChild3LastName = ""
strChild3Year = ""
strChild3Month = ""
strChild3Day = ""
strChild3Last4 = ""
lstrCustomWords = []

# ------------------------------
# User input
# ------------------------------
strFirstName = input("Subjects first name: ")
strLastName = input("Subjects last name: ")
strYear = input("Subjects year of birth: ")
strMonth = input("Subjects month of birth: ")
strDay = input("Subjects day of birth: ")
strLast4 = input("Subjects last four digits (swe personnr): ")

strAnswer = "n"
strAnswer = input("Partner? <y/n>: ")
if strAnswer.lower() == "y": 
	strPartnerFirstName = input("Partners first name: ")
	strPartnerLastName = input("Partners last name: ")
	strPartnerYear = input("Partners year of birth: ")
	strPartnerMonth = input("Partners month of birth: ")
	strPartnerDay = input("Partners day of birth: ")
	strPartnerLast4 = input("Partners last four digits (swe personnr): ")

strAnswer = "n"
strAnswer = input("Child? <y/n>: ")
if strAnswer.lower() == "y": 
	strChild1FirstName = input("Childs first name: ")
	strChild1LastName = input("Childs last name: ")
	strChild1Year = input("Childs year of birth: ")
	strChild1Month = input("Childs month of birth: ")
	strChild1Day = input("Childs day of birth: ")
	strChild1Last4 = input("Childs last four digits (swe personnr): ")

	strAnswer = "n"
	strAnswer = input("Another child? <y/n>: ")
	if strAnswer.lower() == "y": 
		strChild2FirstName = input("Childs first name: ")
		strChild2LastName = input("Childs last name: ")
		strChild2Year = input("Childs year of birth: ")
		strChild2Month = input("Childs month of birth: ")
		strChild2Day = input("Childs day of birth: ")
		strChild2Last4 = input("Childs last four digits (swe personnr): ")

		strAnswer = "n"
		strAnswer = input("Another child? <y/n>: ")
		if strAnswer.lower() == "y": 
			strChild3FirstName = input("Childs first name: ")
			strChild3LastName = input("Childs last name: ")
			strChild3Year = input("Childs year of birth: ")
			strChild3Month = input("Childs month of birth: ")
			strChild3Day = input("Childs day of birth: ")
			strChild3Last4 = input("Childs last four digits (swe personnr): ")

while strAnswer != "":
	strAnswer = input("Add more words! Idols etc..: ")
	if strAnswer.lower() != "":
		if strAnswer not in lstrCustomWords:
			lstrCustomWords.append(strAnswer)
	
# ------------------------------
# Add to names wordlist
# ------------------------------
# Declare lists
lstrNames  = [] # Main names list
tempNames1 = [] # Temporary clone 1
tempNames2 = [] # Temporary clone 2
tempNames3 = [] # Result list -> main

# Manual add user strings
if strFirstName != "" and strFirstName not in lstrNames:
	lstrNames.append(strFirstName)
if strLastName != "" and strLastName not in lstrNames:
	lstrNames.append(strLastName)
if strPartnerFirstName != "" and strPartnerFirstName not in lstrNames:
	lstrNames.append(strPartnerFirstName)
if strPartnerLastName != "" and strPartnerLastName not in lstrNames:
	lstrNames.append(strPartnerLastName)
if strChild1FirstName != "" and strChild1FirstName not in lstrNames:
	lstrNames.append(strChild1FirstName)
if strChild1LastName != "" and strChild1LastName not in lstrNames:
	lstrNames.append(strChild1LastName)
if strChild2FirstName != "" and strChild2FirstName not in lstrNames:
	lstrNames.append(strChild2FirstName)
if strChild2LastName != "" and strChild2LastName not in lstrNames:
	lstrNames.append(strChild2LastName)
if strChild3FirstName != "" and strChild3FirstName not in lstrNames:
	lstrNames.append(strChild3FirstName)
if strChild3LastName != "" and strChild3LastName not in lstrNames:
	lstrNames.append(strChild3LastName)
if len(lstrCustomWords) > 0:
	lstrNames = lstrNames + lstrCustomWords

# Add combinations
tempCaseNames = []
for x in lstrNames:
	if x.upper() not in tempCaseNames:
		tempCaseNames.append(x.upper())
	if x.lower() not in tempCaseNames:
		tempCaseNames.append(x.lower())
lstrNames = lstrNames + tempCaseNames

tempNames1 = lstrNames
tempNames2 = lstrNames

for x in tempNames1:
	for y in tempNames2:
		if x != y:
			if str(x + y) not in tempNames3:
				tempNames3.append(x + y)
			if str(y + x) not in tempNames3:
				tempNames3.append(y + x)
lstrNames = lstrNames + tempNames3

# ------------------------------
# Add to dates wordlist
# ------------------------------
# Declare lists
lstrDates =  [] # Main dates list
tempDates1 = [] # Temporary clone 1
tempDates2 = [] # Temporary clone 2
tempDates3 = [] # Result list -> main

# Manual add user strings
if strYear != "" and strYear not in lstrDates:
	lstrDates.append(strYear)
if strMonth != "" and strMonth not in lstrDates:
	lstrDates.append(strMonth)
if strDay != "" and strDay not in lstrDates:
	lstrDates.append(strDay)
if strLast4 != "" and strLast4 not in lstrDates:
	lstrDates.append(strLast4)
if strPartnerYear != "" and strPartnerYear not in lstrDates:
	lstrDates.append(strPartnerYear)
if strPartnerMonth != "" and strPartnerMonth not in lstrDates:
	lstrDates.append(strPartnerMonth)
if strPartnerDay != "" and strPartnerDay not in lstrDates:
	lstrDates.append(strPartnerDay)
if strPartnerLast4 != "" and strPartnerLast4 not in lstrDates:
	lstrDates.append(strPartnerLast4)
if strChild1Year != "" and strChild1Year not in lstrDates:
	lstrDates.append(strChild1Year)
if strChild1Month != "" and strChild1Month not in lstrDates:
	lstrDates.append(strChild1Month)
if strChild1Day != "" and strChild1Day not in lstrDates:
	lstrDates.append(strChild1Day)
if strChild1Last4 != "" and strChild1Last4 not in lstrDates:
	lstrDates.append(strChild1Last4)
if strChild2Year != "" and strChild2Year not in lstrDates:
	lstrDates.append(strChild2Year)
if strChild2Month != "" and strChild2Month not in lstrDates:
	lstrDates.append(strChild2Month)
if strChild2Day != "" and strChild2Day not in lstrDates:
	lstrDates.append(strChild2Day)
if strChild2Last4 != "" and strChild2Last4 not in lstrDates:
	lstrDates.append(strChild2Last4)
if strChild3Year != "" and strChild3Year not in lstrDates:
	lstrDates.append(strChild3Year)
if strChild3Month != "" and strChild3Month not in lstrDates:
	lstrDates.append(strChild3Month)
if strChild3Day != "" and strChild3Day not in lstrDates:
	lstrDates.append(strChild3Day)
if strChild3Last4 != "" and strChild3Last4 not in lstrDates:
	lstrDates.append(strChild3Last4)

# Add combinations
tempDates1 = lstrDates
tempDates2 = lstrDates

for x in tempDates1:
	for y in tempDates2:
		if x != y:
			if str(x + y) not in tempDates3:
				tempDates3.append(x + y)
			if str(y + x) not in tempDates3:
				tempDates3.append(y + x)
lstrDates = lstrDates + tempDates3

# ------------------------------
# Add to main wordlist
# ------------------------------
lstrMain = []

# Combine dates and names
for x in lstrNames:
	for y in lstrDates:
		lstrMain.append(x)
		lstrMain.append(y)
		lstrMain.append(y + x)
		lstrMain.append(x + y)

# Remove duplicates
strAnswer = input("Remove duplicates? Will take a LONG time... <y/n>: ")
if strAnswer.lower() == "y":
	lstrMain = remove(lstrMain)
	sys.stdout.write("\n")
else:
	sys.stdout.write("Duplicates can be removed using <sort " + strFirstName + "_wordlist.txt | uniq | tee sorted_wordlist.txt>\n")
# ------------------------------
# Write to file 
# ------------------------------
file = open(strFirstName + "_wordlist.txt","w")
for x in lstrMain:
	file.write(x + '\n')
file.close()
