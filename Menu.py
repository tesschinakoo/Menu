from Myro import *

#Chinese food lists
list1 = ['Fried','Broiled','Grilled','Honey']
list2 = ['Chicken','Beef','Shrimp','Lamb']
list3 = ['with sweet and sour sauce','hot sauce','soy sauce','sesame sauce']
#American food lists
list4 = ['Chicken Fried','Grilled','Breaded','Baked']
list5 = ['Steak','Chicken','Pork','Bison']
list6 = ['mashed potatoes','french frieds','cole slaw','creamed spinach']

#Italian food lists
list7 = ['Alfredo','Pesto','Marinara','Bolognese']
list8 = ['linquini','penne','rigatoni','angel hair pasta','fusili','spaghetti']
list9 = ['meatballs','filet mignon','prosciutto','basil','oregano']

import random

answer=askQuestion("What kind of food would you like?", ["Chinese", "American", "Italian"])
if (answer=="Chinese"):
    print("Tess's Authentic Chinese food")
    print("Entrees")
    for x in range(0,5):
        print(random.choice(list1), random.choice(list2),"with", random.choice(list3))
if (answer=="American"):
    print("Tess's Grill")
    print("Entrees")
    for x in range(0,5):
        print(random.choice(list4), random.choice(list5),"with", random.choice(list6))
if (answer=="Italian"):
    print("Mama Koo's")
    print("Entrees")
    for x in range(0,5):
        print(random.choice(list7), random.choice(list8),"with", random.choice(list9))
