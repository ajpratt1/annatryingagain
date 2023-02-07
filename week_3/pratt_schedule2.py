schedule = {
	"monday" :   ['Human-Information Behavior','Information Professions','Research Mthds/Law Lit','Strategic Leadership','Conservation and Preservation','Info Services & Resources'],
	"tuesday":   ['Information Arch/Inter Design','Information Professions','Acad Libraries and Scholarly','Info Services & Resources'],
	"wednesday": ['Info Services & Resources','Usability Theory & Practice','Mgmt of Archives/Sp Collection','Government Info Sources','Library Media Centers','Mgmt of Archives/Sp Collection'],
	"thursday": ['Information Science Research','Information Professions','Information Professions'],
}


#loop through each day in schedule, print the name of the day, and then loop through all the class names and print them out

#output sample:

# ❯ python3 pratt_schedule2.py
# monday
# Human-Information Behavior
# Information Professions
# ...

for day in schedule:
	print(day)
	cl = schedule[day]
	if type(cl) is list:
		for x in cl:
			print(x)