# ------------------------------
# Wordlist generator
# ------------------------------

strFirstName = ""
strLastName = ""
strYear = ""
strMonth = ""
strDay = ""
strPartnerFirstName = ""
strPartnerLastName = ""
strPartnerYear = ""
strPartnerMonth = ""
strPartnerDay = ""
strChild1FirstName = ""
strChild1LastName = ""
strChild1Year = ""
strChild1Month = ""
strChild1Day = ""
strChild2FirstName = ""
strChild2LastName = ""
strChild2Year = ""
strChild2Month = ""
strChild2Day = ""
strChild3FirstName = ""
strChild3LastName = ""
strChild3Year = ""
strChild3Month = ""
strChild3Day = ""

# Get input from user
strFirstName = raw_input("Subjects first name: ")
strLastName = raw_input("Subjects last name: ")
strYear = raw_input("Subjects year of birth: ")
strMonth = raw_input("Subjects month of birth: ")
strDay = raw_input("Subjects day of birth: ")

strAnswer = "n"
strAnswer = raw_input("Partner? <y/n>: ")
if strAnswer.lower() == "y": 
	strPartnerFirstName = raw_input("Partners first name: ")
	strPartnerLastName = raw_input("Partners last name: ")
	strPartnerYear = raw_input("Partners year of birth: ")
	strPartnerMonth = raw_input("Partners month of birth: ")
	strPartnerDay = raw_input("Partners day of birth: ")

strAnswer = "n"
strAnswer = raw_input("Child? <y/n>: ")
if strAnswer.lower() == "y": 
	strChild1FirstName = raw_input("Childs first name: ")
	strChild1LastName = raw_input("Childs last name: ")
	strChild1Year = raw_input("Childs year of birth: ")
	strChild1Month = raw_input("Childs month of birth: ")
	strChild1Day = raw_input("Childs day of birth: ")

	strAnswer = "n"
	strAnswer = raw_input("Another child? <y/n>: ")
	if strAnswer.lower() == "y": 
		strChild2FirstName = raw_input("Childs first name: ")
		strChild2LastName = raw_input("Childs last name: ")
		strChild2Year = raw_input("Childs year of birth: ")
		strChild2Month = raw_input("Childs month of birth: ")
		strChild2Day = raw_input("Childs day of birth: ")

		strAnswer = "n"
		strAnswer = raw_input("Another child? <y/n>: ")
		if strAnswer.lower() == "y": 
			strChild3FirstName = raw_input("Childs first name: ")
			strChild3LastName = raw_input("Childs last name: ")
			strChild3Year = raw_input("Childs year of birth: ")
			strChild3Month = raw_input("Childs month of birth: ")
			strChild3Day = raw_input("Childs day of birth: ")

# ------------------------------
# Add to names wordlist
# ------------------------------
# Declare lists
lstrNames  = [] # Main names list
tempNames1 = [] # Temporary clone 1
tempNames2 = [] # Temporary clone 2
tempNames3 = [] # Result list -> main

# Manual add user strings
if strFirstName != "":
	lstrNames.append(strFirstName)
if strLastName != "":
	lstrNames.append(strLastName)
if strPartnerFirstName != "":
	lstrNames.append(strPartnerFirstName)
if strPartnerLastName != "":
	lstrNames.append(strPartnerLastName)
if strChild1FirstName != "":
	lstrNames.append(strChild1FirstName)
if strChild1LastName != "":
	lstrNames.append(strChild1LastName)
if strChild2FirstName != "":
	lstrNames.append(strChild2FirstName)
if strChild2LastName != "":
	lstrNames.append(strChild2LastName)
if strChild3FirstName != "":
	lstrNames.append(strChild3FirstName)
if strChild3LastName != "":
	lstrNames.append(strChild3LastName)

# Add combinations
tempNames1 = lstrNames
tempNames2 = lstrNames

for x in tempNames1:
	for y in tempNames2:
		if x != y:
			tempNames3.append(x + y)
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
if strYear != "":
	lstrDates.append(strYear)
if strMonth != "":
	lstrDates.append(strMonth)
if strDay != "":
	lstrDates.append(strDay)
if strPartnerYear != "":
	lstrDates.append(strPartnerYear)
if strPartnerMonth != "":
	lstrDates.append(strPartnerMonth)
if strPartnerDay != "":
	lstrDates.append(strPartnerDay)
if strChild1Year != "":
	lstrDates.append(strChild1Year)
if strChild1Month != "":
	lstrDates.append(strChild1Month)
if strChild1Day != "":
	lstrDates.append(strChild1Day)
if strChild2Year != "":
	lstrDates.append(strChild2Year)
if strChild2Month != "":
	lstrDates.append(strChild2Month)
if strChild2Day != "":
	lstrDates.append(strChild2Day)
if strChild3Year != "":
	lstrDates.append(strChild3Year)
if strChild3Month != "":
	lstrDates.append(strChild3Month)
if strChild3Day != "":
	lstrDates.append(strChild3Day)

# Add combinations
tempDates1 = lstrDates
tempDates2 = lstrDates

for x in tempDates1:
	for y in tempDates2:
		if x != y:
			tempDates3.append(x + y)
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
		lstrMain.append(x.upper())
		lstrMain.append(x.lower())
		lstrMain.append(y)
		lstrMain.append(y.upper())
		lstrMain.append(y.lower())
		lstrMain.append(y + x)
		lstrMain.append(y + x.upper())
		lstrMain.append(y + x.lower())
		lstrMain.append(x + y)
		lstrMain.append(x.upper() + y)
		lstrMain.append(x.lower() + y)
# ------------------------------
# Write to file 
# ------------------------------
file = open(strFirstName + "_wordlist.txt","w")
for x in lstrMain:
	file.write(x + '\n')
file.close()
