"""
Author is Steven Campbell This is a takeout ordering system for Olive Garden
with their menu.
"""
__author__ = "Steven Campbell"

# Ordering Togo Paying at The Olive Garden
# The entrees come with Salad or Soup and two breadsticks.


def main():

    """
Retrieves information on the users dinner and drinks.
    """

    order = input('Hope your day is going well,'
                  ' would you like to make an order? If not say no.')
    print('Please hold while we get a togo member to take your order.')
    wait = 10
    while wait != 0:
        print(wait)
        wait -= 1
    if order != "no":
        # Information about the Menu Options
        print("\nCurrent Special: ",
              "Dinners are all 14.99$ and desserts are 7.99!", sep="")
        # Getting the choices for dinner   "How many drinks do you want"
        print(
            '\n\nBeverages:\nAqua Panna (2.99)\nLemonade ($2.99)'
            '\nFresh Brewed Iced Tea ($2.99)\nFlavored Iced Teas ($2.99)'
            '\nBellini Peach-Raspberry or Mango-Strawberry ($2.99)\n'
            'Fountain Drinks ($2.99)\n')
        while True:
            try:
                beverage = int(input("How many drinks would you like in whole "
                                     "numbers?"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if beverage > 0:
            pass
        elif beverage == 0 or "zero":
            pass
        else:
            beverage = int(input("Please enter a valid integer."))
        beverage_cost = float(beverage) * 2.99

        print(
            '\nAppetizers:\nCalamari ($10.79)\nFried Mozzarella ($7.29)'
            '\nLasagna Fritta (9.99)\nToasted Ravioli ($8.49)'
            '\nClassic Shrimp Scampi Fritta ($10.49)\n'
            'Stuffed Ziti Fritta ($7.49)\nSpinach-Artichoke Dip ($9.79)\n')
        while True:
            try:
                appetizer = int(input("How many appetizers would you like?"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if appetizer >= 0:
            pass
        else:
            appetizer = int(input("Please enter a valid number."))
        appetizer_cost = float(appetizer) * 6.99
        # Salad or Soup counter
        print('\nEntrees:\nChicken Parmigiana ($16.79)\nEggplant Parmigiana '
              '($14.99)\nFive Cheese Ziti al Forno ($14.29)\nCheese Ravioli '
              '($13.49)\nTour of Italy ($18.79)\nLasagna Classico ($15.79)'
              '\nShrimp Scampi ($17.49)\nChicken & Shrimp Carbonara ($19.49)'
              '\nChicken Scampi ($17.49)\nChicken Alfredo ($17.29)'
              '\nShrimp Alfredo ($18.29)\n')
        while True:
            try:
                entree = int(input("How many entrees would you like?"))
                break
            except ValueError:
                print("Error. Must be a whole number.")

        """
        Counter for the soups or salads and totals them up depending on 
        amount of entrees.
        """

        soup = 0
        salad = 0
        if entree > 0:
            for entree_count in range(entree):
                soup_or_salad = input(
                    "Would you like soup or salad with entree your entree(s)")
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
                        print("Please let us know what you would like "
                              "when you arrive.")
        elif entree == 0 or "zero":
            pass
        else:
            entree = input("Please enter a valid number.")
        entree_cost = float(entree) * 15.99

        print("\nDesserts:\nChocolate Brownie Lasagna (7.49)"
              "\nSicilian Cheesecake (7.29)\nTiramisu (7.29)"
              "\nBlack Tie Mousse Cake (8.29)\nWarm Italian Donuts (6.99)\n")
        while True:
            try:
                dessert = int(input("How many desserts would you like?"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if dessert >= 0:
            pass
        else:
            input("Please enter a valid number.")
        dessert_cost = float(dessert) * 7.99

        bread = int(entree) ** 2

        """
        Print statements depending on amount of soups and/or salads.
        """

        if salad > 0 and soup < 1:
            print("\nYour dinner will come with", bread, "breadsticks and",
                  salad, "salad(s)!")
        elif salad > 0 and soup > 0:
            print("\nYour dinner will come with", bread, "breadsticks and",
                  salad, "salad(s) and,", soup, "soup(s)")
        elif salad < 1 and soup > 0:
            print("\nYour dinner will come with", bread, "breadsticks and",
                  soup, "soup(s)!")
        else:
            print("\nYour dinner will come with", bread, "breadsticks!")

        """
        # Calculating the totals, adds the tip and displays the gratitude.
        """

        cost_of_dinner = round(
            beverage_cost + appetizer_cost + entree_cost + dessert_cost, 2)
        while True:
            try:
                tip_amount = int(input("\nWhat percentage would you like to"
                                       " tip for the Togo Staff tonight?"))
                break
            except ValueError:
                print("Error. Must be a whole number.")
        if tip_amount >= 0:
            if tip_amount >= 30 and cost_of_dinner > 50:
                print("Thank you so much you made our Togo Teams night "
                      "and we gave you some extra bread!")
            elif tip_amount >= 30 and not cost_of_dinner > 50:
                print("Thank you so much you made our Togo Teams night!")
            elif tip_amount >= 20:
                print("Thank you we appreciate your generosity!")
            elif tip_amount > 0:
                print("Thank you!")
            else:
                pass

        """
        # Receipt showing choices and their amounts for their togo order.
        """

        print("\nReceipt:")
        if salad > 0 and soup < 1:
            print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:",
                  appetizer, "$", appetizer_cost,
                  "\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert,
                  "$", dessert_cost, "\n",
                  bread, "Breadsticks and", salad, "Salad(s)")
        elif salad > 0 and soup > 0:
            print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:",
                  appetizer, "$", appetizer_cost, "\nEntree:", entree, "$",
                  entree_cost, "\nDessert:", dessert, "$", dessert_cost, "\n",
                  bread, "Breadsticks", salad, "Salad(s)", soup, "and Soup(s)")
        elif salad < 1 and soup > 0:
            print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:",
                  appetizer, "$", appetizer_cost,
                  "\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert,
                  "$", dessert_cost, "\n",
                  bread, "Breadsticks and", soup, "Soup(s)")
        else:
            print("Beverages:", beverage, "$", beverage_cost, "\nAppetizers:",
                  appetizer, "$", appetizer_cost,
                  "\nEntree:", entree, "$", entree_cost, "\nDessert:", dessert,
                  "$", dessert_cost, "\n",
                  bread, "Breadsticks")
        # Sales tax in florida is 7% to derive total
        print("\nSubtotal: $", cost_of_dinner)
        total_cost = cost_of_dinner * 1.07
        print("Total: $", round(total_cost, 2))

        """
        The tip amount and it being added to get the grand total
        """

        service_tip = (total_cost * float(tip_amount) / 100)
        print("Tip: $", round(service_tip, 2))
        grand_total = service_tip + total_cost
        print("Grand Total: $", round(grand_total, 2))
        print("\nWe Hope You Have a Wonderful Day!" + "\nPlease Come Again!")
    else:
        print("\nWe Hope You Have a Wonderful Day!" + "\nPlease Come Again!")


main()
