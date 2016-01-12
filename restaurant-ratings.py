def restaurant_ratings(file_name):

    data = open(file_name)
    restaurant_and_rating = {}

    for line in data:
        new_line = line.rstrip()
        restaurant_name, rating = new_line.split(":")
        restaurant_and_rating[restaurant_name] = rating 

    dictionary_to_tuple = restaurant_and_rating.iteritems()

    for rn_key, rate_value in dictionary_to_tuple:
        print "%s is rated at %s." % (rn_key, rate_value)



restaurant_ratings("scores.txt")
