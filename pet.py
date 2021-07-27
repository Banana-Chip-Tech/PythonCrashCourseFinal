# Author: <Your name here>
# Description: This file defines the pet class

# Pet
#
# This class defines the base class for all pet objects
class Pet:
    #__init___
    #
    # this function defines the init function for this class. This function will be called
    #   as soon as the Pet object is created
    # preconditions:
    #  self - the Pet class. Remember that all functions in a class must pass in the self object
    #     as the first parameter!
    #  name - the name of the pet. Notice that in the function declaration its set = to empty string?
    #     this demonstrates the use of template parameters!
    # postconditions:
    #     a message stating that this is a new pet is printed out to the screen
    # return: None
    def __init__(self,name=""):
        #print("Hi! I'm your new pet! My name is: %s" % name)
        self.name = name



    # feedme
    #
    # this function prints out a statement that tells the pet owner that the pet needs to be fed
    # preconditions: None
    # postconditions:
    #   - a message saying that the pet is hungry is printed out to the screen
    # return: None
    def feedme(self):
        # %s allows us to inject variables into strings.
        #  Therefore, the print message that we will get will be something like
        #  "<Pet Name> says: I'm hungry ..."
        print("%s says: I'm hungry! Feed me!" % self.name)

    # eat
    #
    # the eat function has the pet eat whatever food they were given
    # preconditions:
    #    - food : a food object is passed in. Refer to the foods/food.py file to find out about this!
    # postconditions:
    #    - the name of the food is printed out to the screen
    # return: None
    def eat(self,food):
        print("%s just ate a %s" %(self.name,food.food_name()))
