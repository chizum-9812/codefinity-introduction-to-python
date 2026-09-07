vegetables = ["tomatoes", "potatoes", "onions"]

#to remove
vegetables.remove ("onions")

#add carrots to the list
vegetables.append ("carrots")

#add cucumbers to the list
vegetables.append ("cucumbers")

#sorting
vegetables.sort()

#test
print(f"Updated vegetable Inventory: {vegetables}")
if ("carrots" in vegetables):
    print ("Carrots are already in the list.")

if ("cucumbers" in vegetables):
    print ("Cucumbers are already in the list.")