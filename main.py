# Author: <Your name here>
# Description: This file demonstrates the use of class based polymorphism. It is assumed that you
#  are already familiar with some python concepts. This project is also designed in a very object
#  oriented fashion.


# Imports: Add your own imports here if needed!
from pet import Pet
from dog import Dog
from cat import Cat

# Notice how this import is different from the rest? Thats because the food file in a
#  directory (or folder) that is seperate from the main folder that we are in
from foods.food import Food
# Add your potato import here!


# This is the main function of the program.
#   We use this function in order to define the entry point for the program. This
#   is technically not required but is good programming practice
def main():

    # Lets create a pet object. Navigate to the pet.py file to look at the class declaration
    mypet = Pet()
    #mypet = Pet(name="steve")
    print("-------")
    mypet.feedme()
    print("-------")
    mypet.eat(Food())

    # Make sure to import potato before adding this in!
    #mypet.eat(Potato())

    #dog = Dog()
    #cat = Cat()

    #dog.feedme()
    #dog.eat(Food())

if __name__ == "__main__":
    main()



