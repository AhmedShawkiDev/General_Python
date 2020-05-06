

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
len(vendors)
#5
list(range(5))
#[0, 1, 2, 3, 4]
for element_index in range(len(vendors)):
	print(vendors[element_index])
	
#Cisco
#etc....
######New code

for index, element in enumerate (vendors):
	print(index, element)
