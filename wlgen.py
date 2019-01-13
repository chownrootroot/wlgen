# ------------------------------
# Wordlist generator
# ------------------------------

# Get input from user
strFirstName = 			raw_input("Subjects first name: ")
strLastName = 			raw_input("Subjects last name: ")
strYear = 				raw_input("Subjects year of birth: ")
strMonth = 				raw_input("Subjects month of birth: ")
strDay = 				raw_input("Subjects day of birth: ")
strPartnerFirstName = 	raw_input("Subjects partners first name: ")
strPartnerLastName = 	raw_input("Subjects partners last name: ")
strPartnerYear = 		raw_input("Subjects partners year of birth: ")
strPartnerMonth = 		raw_input("Subjects partners month of birth: ")
strPartnerDay = 		raw_input("Subjects partners day of birth: ")

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
		lstrMain.append(y + x)
		lstrMain.append(y + x.upper())
		lstrMain.append(y + x.lower())
		lstrMain.append(x + y)
		lstrMain.append(x.upper() + y)
		lstrMain.append(x.lower() + y)
# ------------------------------
# Write to file 
# ------------------------------
file = open("wordlist.txt","w")
for x in lstrMain:
	file.write(x + '\n')
file.close()
