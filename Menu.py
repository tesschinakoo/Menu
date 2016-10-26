from Myro import *

#Chinese food lists
list1 = ['Fried','Broiled','Grilled','Stir-fry']
list2 = [' Chicken',' Beef',' Shrimp',' Lamb']
list3 = [' sweet and sour sauce',' hot sauce',' sweet soy sauce',' sesame sauce']
list10 = ['Mochi', 'Green Tea Cake', 'Fruit Cake', 'Red Bean Cake']

#American food lists
list4 = ['Chicken Fried','Grilled','Breaded','Baked']
list5 = [' Steak',' Chicken',' Pork',' Bison']
list6 = [' mashed potatoes',' french fries',' cole slaw',' creamed spinach']
list11 = ['Ice Cream', 'Chocolate Cake', 'Cookie Plate', 'Red Velvet Cupcakes']

#Italian food lists
list7 = ['Alfredo','Pesto','Marinara','Bolognese','Parmasean','Butter']
list8 = [' linquini',' penne',' rigatoni',' angel hair pasta',' fusili',' spaghetti']
list9 = [' meatballs',' filet mignon',' prosciutto',' basil',' oregano',' sausage']
list12 = ['Tiramisu', 'Cannoli', 'Gelato', 'Creme Brulee']

import random

from Graphics import *

win = Window("Menu")


answer=askQuestion("What kind of food would you like?", ["Chinese", "American", "Italian"])
if (answer=="Chinese"):
    Restaurant = "Tess's Authentic Chinese Food"
    Type = list1
    Entree = list2
    Side = list3
    Dessert = list10
if (answer=="American"):
    Restaurant = "Tess's Grill"
    Type = list4
    Entree = list5
    Side = list6
    Dessert = list11
if (answer=="Italian"):
    Restaurant = "Mama Koo's"
    Type = list7
    Entree = list8
    Side = list9
    Dessert = list12
    

RestaurantName = Text((150, 30), Restaurant)
RestaurantName.fontSize = 15
RestaurantName.fill = Color("black")
RestaurantName.draw(win)
Entrees = Text((150,65), "Entrees")
Entrees.fontSize = 14
Entrees.fill = Color("black")
Entrees.draw(win)
Desserts = Text((150, 180), "Desserts")
Desserts.fontSize = 14
Desserts.fill = Color("black")
Desserts.draw(win)
for x in range(0,4):
    choice1 = random.choice(Type)
    choice2 = random.choice(Entree)
    choice3 = random.choice(Side)
    choice4 = random.choice(Dessert)
    MenuEntree = (choice1 + choice2 + " with" + choice3)
    Item = Text((150, 85 + (x* 20)), MenuEntree)
    Item.fill = Color("black")
    Item.fontSize = 13
    Item.draw(win)
    Type.remove(choice1)
    Entree.remove(choice2)
    Side.remove(choice3)
    MenuDessert = (choice4)
    Item = Text((150, 200 + (x* 20)), MenuDessert)
    Item.fill = Color("black")
    Item.fontSize = 13
    Item.draw(win)
    Dessert.remove(choice4)


