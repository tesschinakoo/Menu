from Myro import *

#Chinese food lists
list1 = ['Fried','Broiled','Grilled','Stir-fry']
list2 = ['Chicken','Beef','Shrimp','Lamb']
list3 = ['sweet and sour sauce','hot sauce','sweet soy sauce','sesame sauce']
#American food lists
list4 = ['Chicken Fried','Grilled','Breaded','Baked']
list5 = ['Steak','Chicken','Pork','Bison']
list6 = ['mashed potatoes','french frieds','cole slaw','creamed spinach']

#Italian food lists
list7 = ['Alfredo','Pesto','Marinara','Bolognese','Parmasean','Butter']
list8 = ['linquini','penne','rigatoni','angel hair pasta','fusili','spaghetti']
list9 = ['meatballs','filet mignon','prosciutto','basil','oregano','sausage']

import random

answer=askQuestion("What kind of food would you like?", ["Chinese", "American", "Italian"])
if (answer=="Chinese"):
    print("Tess's Authentic Chinese food")
    print("Entrees")
    for x in range(0,4):
        choice1 = random.choice(list1)
        choice2 = random.choice(list2)
        choice3 = random.choice(list3)
        print(choice1, choice2,"with", choice3)
        list1.remove(choice1)
        list2.remove(choice2)
        list3.remove(choice3)
if (answer=="American"):
    print("Tess's Grill")
    print("Entrees")
    for x in range(0,4):
        choice4 = random.choice(list4)
        choice5 = random.choice(list5)
        choice6 = random.choice(list6)
        print(choice4, choice5,"with", choice6)
        list4.remove(choice4)
        list5.remove(choice5)
        list6.remove(choice6)
if (answer=="Italian"):
    print("Mama Koo's")
    print("Entrees")
    for x in range(0,6):
        choice7 = random.choice(list7)
        choice8 = random.choice(list8)
        choice9 = random.choice(list9)
        print(choice7, choice8,"with", choice9)
        list7.remove(choice7)
        list8.remove(choice8)
        list9.remove(choice9)