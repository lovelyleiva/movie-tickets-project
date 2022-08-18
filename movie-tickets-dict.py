print('Welcome to the movies!')

child_tix_price = 7
adult_tix_price = 11.50
tax_rate = .075

choice = "y"
# list of movies
movies = {1: 'Star Wars',2:  'Top Gun Maverick',3: 'Megamind'}

def calculate_total(adult_tix, child_tix, adult_price = adult_tix_price, child_price=child_tix_price, tax = tax_rate):
    total_price = ((adult_tix * adult_price) + (child_tix * child_price)) * (1 + tax)
    return round(total_price,2)

user_choices = {}
#empty to uuse it later on

while choice == "y":
    #while loop starts here
    print('Movie List:')
    for i in movies:
        print(f'{i} - {movies[i]}')

    movie_choice =int(input('Which movie do you want to see?'))
    
    user_tix = {"adult":0, "child":0}

    user_tix["adult"] = int(input('How many adult tickets do you want to purchase?'))
    user_tix["child"] = int(input('How many child tickets do you want to purchase?'))

    user_choices[movies[movie_choice]] = user_tix
    #for dicts, you retrieve values from the KEYS, not from the indexes.

    # total price = (adult tix *adult price + child tix* child price ) * (1 + tax rate)
    #total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    #total_price_str = str(total_price)

    total_price = calculate_total(adult_tix = user_tix['adult'],child_tix = user_tix['child'])

    #print a summary
    #Thank you for your purchase
    #You are seeing Megamind
    #Your total is $xx
    print('Thanks for your purchase!')
    #print(f'You are seeing: {movies[movie_choice-1]}')
    print(f'You are seeing: {movies[movie_choice]}')
    print(f'Your total is: $' + "{:.2f}".format(total_price))
    choice = input('Do you want more tickets? y/n')
    #end of loop

print("\nTotal Ticket Summary:")
sum_total = 0
for title in user_choices:
    print(f'Movies: {title}')
    total_price = calculate_total(adult_tix = user_choices[title]["adult"], child_tix = user_choices[title]["child"])
    print(f'Total Price: {total_price}')
    sum_total += total_price

print(f"Sum total for all tickets: {sum_total}")
print('Bye')