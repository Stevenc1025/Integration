#Steven Campbell
#Ordering Togo Paying at The Olive Garden
#The entrees come with Salad and two breadsticks.
#https://www.olivegarden.com/order-online?order-type=CP

print("Hope your day is going well, order whenever you are ready", end = ".")

#Information about the Menu Options    
print("\nCurrent Special: ", "Dinners are all 14.99$ and desserts are 7.99!", sep = "")
#Getting the choices for dinner   "How many drinks do you want"     "How many desserts do you want"    "How many drinks do you want"  
drink_menu = print("\n\nBeverages:\nWater (Free)\nLemonade ($2.99)\nFresh Brewed Iced Tea ($2.99)\nFlavored Iced Teas ($2.99)\nBellini Peach-Raspberry or Mango-Strawberry ($2.99)\nFountain Drinks ($2.99)\n")
beverage = input("How many drinks would you like?")
beverage_cost = float(beverage) * 2.99

appetizer_menu = print("\nAppetizers:\nCalamari ($10.79)\nFried Mozzarella ($7.29)\nLasagna Fritta (9.99)\nToasted Ravioli ($8.49)\nClassic Shrimp Scampi Fritta ($10.49)\nStuffed Ziti Fritta ($7.49)\nSpinach-Artichoke Dip ($9.79)\n")
appetizer = input("How many appetizers would you like?")
appetizer_cost = float(appetizer) * 6.99

entrree_menu = print("\nEntrees:\nChicken Parmigiana ($16.79)\nEggplant Parmigiana ($14.99)\nFive Cheese Ziti al Forno ($14.29)\nCheese Ravioli ($13.49)\nTour of Italy ($18.79)\nLasagna Classico ($15.79)\nShrimp Scampi ($17.49)\nChicken & Shrimp Carbonara ($19.49)\nChicken Scampi ($17.49)\nChicken Alfredo ($17.29)\nShrimp Alfredo ($18.29)\n")
entree = input("How many entrees would you like?")
entree_cost = float(entree) * 15.99

dessert_menu = print("\nDesserts:\nChocolate Brownie Lasagna (7.49)\nSicilian Cheesecake (7.29)\nTiramisu (7.29)\nBlack Tie Mousse Cake (8.29)\nZeppoli (6.99)\n")
dessert = input("How many desserts would you like?")
dessert_cost = float(dessert) * 7.99

bread=int(entree)**2
salad=int(entree)
print("\nYour dinner will come with" , bread , "breadsticks and" , salad , "salad(s)!")

#Calculating the totals and printing them
cost_of_dinner = round(beverage_cost+appetizer_cost+entree_cost+dessert_cost,2)
tip_amount = input("\nWhat percentage would you like to tip for the Togo Staff tonight?")

#Reviept showing purchases and their amounts
print("\nReciept:")
reciept = print("Beverages:",beverage, "$",beverage_cost,"\nAppetizers:",appetizer,"$",appetizer_cost,"\nEntree:",entree,"$",entree_cost,"\nDessert:",dessert,"$",dessert_cost,"\n",bread,"Breadsticks and",salad, "Salad(s)")

#Sales tax in florida is 7% to derive total
print("\nSubtotal: $",cost_of_dinner)
total_cost = cost_of_dinner*1.07
print("Total: $" , round(total_cost,2))

#The tip amount and it being added to get the grand total
service_tip = (total_cost * float(tip_amount)/100)
print("Tip: $" , round(service_tip,2))
grand_total = service_tip + total_cost
print("Grand Total: $" , round(grand_total,2))

#Adding the two goodbyes together
print("\nWe Hope You Have a Wonderful Day!"+"\nPlease Come Again!")
