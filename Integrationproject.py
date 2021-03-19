#Steven Campbell
#Ordering Togo Paying at The Olive Garden
#The entrees come with Salad and two breadsticks.
#https://www.olivegarden.com/order-online?order-type=CP


def main():
    order = input("Hope your day is going well, would you like to make an order? If not say no.")
    print("Please hold while we get a togo member to take your order.")
    wait = 10
    while wait != 0:
        print(wait)
        wait -= 1
    if order != "no":
        #Information about the Menu Options
        print("\nCurrent Special: ", "Dinners are all 14.99$ and desserts are 7.99!", sep = "")
        #Getting the choices for dinner   "How many drinks do you want"     "How many desserts do you want"    "How many drinks do you want"
        drink_menu = print("\n\nBeverages:\nAqua Panna (2.99)\nLemonade ($2.99)\nFresh Brewed Iced Tea ($2.99)\nFlavored Iced Teas ($2.99)\nBellini Peach-Raspberry or Mango-Strawberry ($2.99)\nFountain Drinks ($2.99)\n")
        beverage = int(input("How many drinks would you like?"))
        if beverage > 0:
            beverage_cost = float(beverage) * 2.99
        elif beverage == 0 or "zero":
            beverage_cost = 0
        else:
           beverage = int(input("Please enter a valid number."))

        appetizer_menu = print("\nAppetizers:\nCalamari ($10.79)\nFried Mozzarella ($7.29)\nLasagna Fritta (9.99)\nToasted Ravioli ($8.49)\nClassic Shrimp Scampi Fritta ($10.49)\nStuffed Ziti Fritta ($7.49)\nSpinach-Artichoke Dip ($9.79)\n")
        appetizer = int(input("How many appetizers would you like?"))
        if appetizer > 0:
            appetizer_cost = float(appetizer) * 6.99
        elif appetizer == 0 or "zero":
            appetizer_cost = 0
        else:
            appetizer = int(input("Please enter a valid number."))


        entrree_menu = print("\nEntrees:\nChicken Parmigiana ($16.79)\nEggplant Parmigiana ($14.99)\nFive Cheese Ziti al Forno ($14.29)\nCheese Ravioli ($13.49)\nTour of Italy ($18.79)\nLasagna Classico ($15.79)\nShrimp Scampi ($17.49)\nChicken & Shrimp Carbonara ($19.49)\nChicken Scampi ($17.49)\nChicken Alfredo ($17.29)\nShrimp Alfredo ($18.29)\n")
        entree = int(input("How many entrees would you like?"))
        if entree > 0:
            soup = 0
            salad = 0
            for entreecount in range(entree):
                soup_or_salad = input("Would you like soup or salad with entree your entree(s)")
                if soup_or_salad == "salad":
                    salad += 1
                elif soup_or_salad == "soup":
                    soup += 1
                else:
                    soup_or_salad = input("Please choose soup or salad.")
                    if soup_or_salad == "salad":
                        salad += 1
                    elif soup_or_salad == "soup":
                        soup += 1
                    else:
                        print("Please let us know what you would like when you arrive.")
            entree_cost = float(entree) * 15.99
        elif entree == 0 or "zero":
            entree_cost = 0
        else:
            entree = input("Please enter a valid number.")

        dessert_menu = print("\nDesserts:\nChocolate Brownie Lasagna (7.49)\nSicilian Cheesecake (7.29)\nTiramisu (7.29)\nBlack Tie Mousse Cake (8.29)\nZeppoli (6.99)\n")
        dessert = int(input("How many desserts would you like?"))
        if dessert > 0:
            dessert_cost = float(dessert) * 6.99
        elif dessert == 0 or "zero":
            dessert_cost = 0
        else:
            input("Please enter a valid number.")
        dessert_cost = float(dessert) * 7.99

        bread=int(entree)**2

        if salad > 0 and soup < 1:
            print("\nYour dinner will come with" , bread , "breadsticks and" , salad , "salad(s)!")
        elif salad >0 and soup > 0:
            print("\nYour dinner will come with" , bread , "breadsticks and" , salad , "salad(s) and,", soup,"soup(s)")
        elif salad < 1 and soup > 0:
            print("\nYour dinner will come with" , bread , "breadsticks and" , soup , "soup(s)!")
        else:
            print("\nYour dinner will come with", bread, "breadsticks!")


        #Calculating the totals and printing them
        cost_of_dinner = round(beverage_cost+appetizer_cost+entree_cost+dessert_cost,2)
        tip_amount = int(input("\nWhat percentage would you like to tip for the Togo Staff tonight?"))
        if tip_amount >= 0:
            if tip_amount >= 30 and cost_of_dinner > 50:
                print("Thank you so much you made our Togo Teams night and we gave you some extra bread!")
            elif tip_amount >= 30 and not cost_of_dinner > 50:
                print("Thank you so much you made our Togo Teams night!")
            elif tip_amount >= 20:
                print("Thank you we appreciate your generosity!")
            elif tip_amount > 0:
                print("Thank you!")
            else:
                pass

        #Reviept showing purchases and their amounts
        print("\nReciept:")
        if salad > 0 and soup < 1:
            reciept = print("Beverages:",beverage, "$",beverage_cost,"\nAppetizers:",appetizer,"$",appetizer_cost,"\nEntree:",entree,"$",entree_cost,"\nDessert:",dessert,"$",dessert_cost,"\n",bread,"Breadsticks and",salad, "Salad(s)")
        elif salad >0 and soup > 0:
            reciept = print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:", appetizer, "$", appetizer_cost, "\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert, "$", dessert_cost, "\n", bread, "Breadsticks", salad, "Salad(s)", soup, "and Soup(s)")
        elif salad < 1 and soup > 0:
            reciept = print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:", appetizer, "$", appetizer_cost,"\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert, "$", dessert_cost, "\n", bread,"Breadsticks and", soup, "Soup(s)")
        else:
            reciept = print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:", appetizer, "$", appetizer_cost,"\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert, "$", dessert_cost, "\n", bread,"Breadsticks")
        #Sales tax in florida is 7% to derive total
        print("\nSubtotal: $",cost_of_dinner)
        total_cost = cost_of_dinner*1.07
        print("Total: $" , round(total_cost,2))

        #The tip amount and it being added to get the grand total
        service_tip = (total_cost * float(tip_amount)/100)
        print("Tip: $" , round(service_tip,2))
        grand_total = service_tip + total_cost
        print("Grand Total: $" , round(grand_total,2))
        print("\nWe Hope You Have a Wonderful Day!" + "\nPlease Come Again!")
    else:
        print("\nWe Hope You Have a Wonderful Day!"+"\nPlease Come Again!")

main()