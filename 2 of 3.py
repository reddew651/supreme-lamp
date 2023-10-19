def largest_factor(number):
    # start with the largest possible factor
    potential_factor = number - 1
    # keep going until we find a factor
    while potential_factor > 0:
        # check if this number is a factor
        if number % potential_factor == 0:
            # if it is, then we're done!
            return potential_factor
        else:
            # otherwise, we should keep trying
            potential_factor = potential_factor - 1