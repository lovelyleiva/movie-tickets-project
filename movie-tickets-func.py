print('Welcome to the movies!')

child_tix_price = 7
adult_tix_price = 11.50
tax_rate = .075

choice = "y"
# list of movies
movies = ['Star Wars', 'Top Gun Maverick', 'Megamind']

def display_menu():
    print('Movie List:')
    for i in range(len(movies)):
        #print(str(i + 1) + ' - ' + movies[i] )
        print(f'{i + 1} - {movies[i]}')
        #formatted string. interject variables. wrap variables in curly braces.

def get_int(prompt):
    my_int = 0
    is_valid = False
    while not is_valid:
        try:
            my_int = int(input(prompt))
            is_valid = True
        except:
            print('Invalid Integer, try again')
    return my_int

def calc_total_price(child_tix_price, adult_tix_price, tax_rate, adult_tix, child_tix):
    total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    return total_price

while choice == "y":
    #while loop starts here
    display_menu()
    movie_choice = get_int('Which movie do you want to see?')
    adult_tix = get_int('How many adult tickets do you want to purchase?')
    child_tix = get_int('How many child tickets do you want to purchase?')


    # total price = (adult tix *adult price + child tix* child price ) * (1 + tax rate)
    total_price = calc_total_price(child_tix_price, adult_tix_price, tax_rate, adult_tix, child_tix)
    total_price_str = str(total_price)


    #print a summary
    #Thank you for your purchase
    #You are seeing Megamind
    #Your total is $xx
    print('Thanks for your purchase!')
    print(f'You are seeing: {movies[movie_choice-1]}')
    print(f'Your total is: $' + "{:.2f}".format(total_price))
    choice = input('Do you want more tickets? y/n')
    #end of loop

print('Bye')