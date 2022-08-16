print('Welcome to the movies!')

child_tix_price = 7
adult_tix_price = 11.50
tax_rate = .075

choice = "y"

while choice == "y":
    #while loop starts here
    print('Movie List:')
    print('1- Star Wars')
    print('2 - Top Gun Maverick')
    print('3 - Megamind')

    movie_choice =int(input('Which movie do you want to see?'))
    adult_tix = int(input('How many adult tickets do you want to purchase?'))
    child_tix = int(input('How many child tickets do you want to purchase?'))


    # total price = (adult tix *adult price + child tix* child price ) * (1 + tax rate)
    total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    total_price_str = str(total_price)

    print('Thanks for your purchase. Your total is: $' + "{:.2f}".format(total_price))
    choice = input('Do you want more tickets? y/n')
    #end of loop

print('Bye')