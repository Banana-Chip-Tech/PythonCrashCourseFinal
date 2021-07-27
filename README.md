# Polymorphism Example

Polymorphism is a difficult concept for students to grasp. In this tutorial we will
cover some of the basics of polymorphism in python, specifically inheritance based polymorphism. Further reading can be found here: https://www.geeksforgeeks.org/polymorphism-in-python/

### Step 1: Project Setup
The first thing that we need to do is set up the project. We can do this 1 of two ways
 - using git clone (recommended)
 - downloading the zip file

#### Git Clone
To use the git clone method, run the following command in the **shell**.
`git clone https://github.com/shenoisam/PolymorphismExample.git`

This will copy all of the code found in this repository (or project) to your local computer.

#### Zip Download (Not recommended)
Navigate to `https://github.com/shenoisam/PolymorphismExample.git` in your web browser and click on the green **Code** button. There is then an option to download a zip file. Please click on this and have the code download to your computer.

### Step 2: Orient ourselves with the code
There's a lot of files in this folder! Let's briefly look at what files we can see in this folder.
The current directory structure looks like what we see below.
```
PolymorphismExample (our project folder)
|    main.py
|    cat.py
|    dog.py
|    GermanShepard.py
|    main.py
|    pet.py
|    README.md (thats this file!)
|    .gitignore (we can ignore this file)
| -- foods
     | \__init__.py
     | food.py
     | potato.py
     | .gitignore (we can ignore this file)
```
We will eventually be working in most of these files. Notice how the files are grouped. The foods files are placed in the foods folder. The pets files, however, are not in their own folder. We will fix this later! For now let's look at the main.py file.

### Step 3: main.py file
The main,py file contains the code that we are going to use as our entry point code. It is customary to name this file main.py (but not required). Let's take a look at the contents.

The first part of the file contains some imports from pet, dog, and cat. We will use these later
on in the tutorial.
```
from pet import Pet
from dog import Dog
from cat import Cat
```

Notice how the following import statement is different from the rest? That's because we are importing Food from the food file which is in the foods folder.
```
from foods.food import Food
```

**Challenge 1: Can you import the Potato class from the potato.py file into main.py?**

The next block of code contains the main function. Let's take a look at the first two lines.
Notice here we are creating a pet named mypet and then running the feedme function. Try running the
code and see what happens. Also notice the commented out line that creates a new pet with the name of Steve? This demonstrates the use of template parameters! We don't have to pass in a name but
we can!
```
def main():
    # Lets create a pet object. Navigate to the pet.py file to look at the class declaration
    mypet = Pet()
    #mypet = Pet(name="steve")
    mypet.feedme()
```
**Challenge 2: Try creating a pet with a different name.**


## Step 4: pet.py
Let's take a look at the pet.py file to see what the feedme function is doing! We've removed the comments present in the file in order to make it a little more readible for this tutorial.
Notice how the name parameter in the ```__init__``` function is set equal to 0? This is what is
called a default parameter. It allows us to not have to pass in a value for a paramter to a function. If we don't pass in a parameter it defaults to the value after the equal sign.

**Challenge 3: Try changing the value of the default parameter and run the code. Did it do what you expected it to?**

Finally, notice how we set self.name equal to the variable name. The self.name variable refers to a varaible that can be accessed by any functions in the class! The self in front is the same self that we have to pass in to every function in a class!
```
class Pet:

    def __init__(self,name=""):
        print("Hi! I'm your new pet! My name is: %s" % name)
        self.name = name
```
Lets look at the other two functions present in the Pet class. The `feedme` function demonstrates the use of string injection. This allows us to insert a variable into a string!
```
class Pet:
    ...

    def feedme(self):
        print("%s says: I'm hungry! Feed me!" % self.name)
    ...
```
**Challenge 4: Modify the feedme function to print out a different message**

Finally, the eat function takes in a food parameter. This function is how the pet will eat.
Notice that all it does is call `food.food_name()`. That will become important later!
```
class Pet:
    ...
    def eat(self,food):
        print(food.food_name())

```
**Challenge 5: Add a function to let the user know that the pet is thirsty**

## Step 4: main.py continued
Thats it for the pet file. Lets go back and look at the **main.py** file. Notice how we create
a dog and a cat. The dog and the cat are pets and therefore they act in many of the same ways as
pets. There are a few differences between them. To test this out, lets look at what happens when we
try to feed a dog. How does this differ from when we try to feed a pet or when we try to feed a cat?
```
    dog = Dog()
    cat = Cat()

    dog.feedme()
    dog.eat(Food())

if __name__ == "__main__":
    main()
```

## Step 5: Reorganizing files
The fact that all of the pets are not in their same folder is annoying! Let's organize our files into a folder.

**Challenge 6: Create a new folder for the pets and move the files to the correct location**

Now that you have moved all of the files into the correct folder, we need to do a few more things to make it work. Lets take a look at the directory structure for the foods folder.
```
 -- foods
     | \__init__.py
     | food.py
     | potato.py
     | .gitignore (we can ignore this file)
```

Notice how there is an **__input__.py** file (ignore the \)? Python needs this file in order to import modules from a sub folder.

**Challenge 7: Create a __input__.py file in your newly created folder**

Great! Now we need to change the imports in the main.py file.
The syntax for importing from a subfolder is as follows

`from <your folder>.<your file> import <your class>`

**Challenge 8: Change your imports in main.py**
