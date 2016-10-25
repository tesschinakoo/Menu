from Myro import *

#Chinese food lists
list1 = ['Spicy','Broiled','Grilled']
list2 = ['Chicken','Beef','Shrimp','Lamb']
list3 = ['with sweet and sour sauce','hot sauce','soy sauce','sesame sauce']
#American food lists

#Italian food lists


answer=askQuestion("What kind of food would you like?", ["Chinese", "American", "Italian"])
if (answer=="Chinese"):
    print("Tess's Authentic Chinese food")
    print("%s %s with %s") % (list1[1], list2[1], list3[1])
if (answer=="American"):
    print("Tess's Bistro")
if (answer=="Italian"):
    print("Mama Koo's")

