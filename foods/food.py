# Author: <Your name here>
# Description: This file defines the food class

# Food
#
# This class defines what a food is
class Food:
    # Notice that there is no __init__? We don't need to do anything with the food
    #  once it is created so we can leave the default behavior in place!

    # food_name
    #
    # the food_name tells what the name of the food is
    # preconditions:
    #    - self : remember that we always need this parameter for functions in a class!
    # postconditions: NA
    # return:
    #  the name of the food. Since this is just a generic food. We can say its a food with no name
    def food_name(self):
        return "I am a food with no name"
