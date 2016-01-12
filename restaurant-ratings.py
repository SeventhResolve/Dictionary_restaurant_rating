def restaurant_ratings(file_name):
    """Prints out restaurant name and rating.""" 

    data = open(file_name)
    restaurant_and_rating = {}

    for line in data:
        new_line = line.rstrip()
        restaurant_name, rating = new_line.split(":")
        restaurant_and_rating[restaurant_name] = rating 

    dictionary_to_tuple = restaurant_and_rating.iteritems()

    for rn_key, rate_value in dictionary_to_tuple:
        # print "%s is rated at %s." % (rn_key, rate_value)

        return restaurant_and_rating

def update_restaurant_and_ratings():
    """Asks user for new restaurant and rating and adds it to dictionary from restaurant_ratings()"""

    user_restaurant_name = raw_input("Enter restaurant name: ")
    user_restaurant_rating = raw_input("Enter restaurant rating: ")

    while True:
        try:
            int_user_restaurant_rating = int(user_restaurant_rating)
            break

        except ValueError:
            print "Please enter a number."
            return update_restaurant_and_ratings()

    restaurant_and_rating = restaurant_ratings("scores.txt")

    restaurant_and_rating[user_restaurant_name] = int_user_restaurant_rating

    sorted_restaurants_alphabetically = sorted(restaurant_and_rating)

    for restaurant in sorted_restaurants_alphabetically:
        print "%s %s" % (restaurant, restaurant_and_rating[restaurant])  
        


    # if type(user_restaurant_rating) != type(10):
    #     print "Enter a number"
    #     return update_restaurant_and_ratings()
    
    # else:
    #     restaurant_and_rating = restaurant_ratings("scores.txt")

    #     restaurant_and_rating[user_restaurant_name] = int(user_restaurant_rating)

    #     sorted_restaurants_alphabetically = sorted(restaurant_and_rating)

    #     for restaurant in sorted_restaurants_alphabetically:
    #         print "%s %s" % (restaurant, restaurant_and_rating[restaurant])


update_restaurant_and_ratings()