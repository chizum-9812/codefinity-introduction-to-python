#Initialize list
meat = ["Ham",3.99,50,"Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99,75, "Spicy"]

#combine list
deli_dept = [meat, cheese, condiment]

#first print
print (f"Initial Deli List: {deli_dept}")

#restock
if ("Ham" in meat) and (meat[2]<100):
    meat [2] = 100
#Add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append (seasonal_meat)

#remove condiment
deli_dept.remove (condiment)

#sort
deli_dept.sort()

#print
print ("Updated Deli List: ", deli_dept)