# holbertonschool-AirBnB_clone

![Image text](https://github.com/AvelinoC5/holbertonschool-AirBnB_clone/blob/main/images/hbnb.png)

HBnB, is a clone of the AirBnB website. It gives the ability to create different locations, users, and reviews for the locations. Currently it only runs as a console. It can desplay all of the instances of all created objects, or display only the instances of a specific type of object (user, review, city, place, state, amenity). The user can also delete any of these created objects.

This repository contains several packages that include the various models that will be employed in the application as objects, a file storage schema class, and various tests written using the unittest module of Python.

![Image text](https://github.com/AvelinoC5/holbertonschool-AirBnB_clone/blob/main/images/estructura.PNG)

## MIRO WHITEBOARD STRUCTURE OF THE PROYECT
![Image text](https://github.com/AvelinoC5/holbertonschool-AirBnB_clone/blob/main/images/AIRBNB%20MIRO.jpg)

# Interactive Mode and Non-interactive mode

The project was created in UBUNTU 14.04.3 LTS and Python 3.4.3. Run the HBnB console.py file in your terminal:

Interactive Mode:

    $ ./console.py
    Welcom to hbnb!

    (hbnb)

Non-interactive Mode:

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $

### Tasks Mandatory Commands of The Console
-------------------------------------------------------------------------------------------------
| Command   | Usage                                       | Functionality                       |
| ----------| --------------------------------------------|-------------------------------------|
|  create   | create <class>                              | creates a new instance of a class   |
|  show     | show <class> <id>                           | shows a specific instance           |
|  destroy  | destroy <class> <id>	                      | deletes a specific instance         |
|  all      | all or all <class>	                        | shows all instances or a class      |
|  update   | update <class> <id> <attribute> <value>	    | updates an attribute of an instance |
|  quit     | quit	                                      | quits the console                   |
|  help     | help	                                      | displays a list of the commands     |
-------------------------------------------------------------------------------------------------

### Installation

    git clone https://github.com/AvelinoC5/holbertonschool-AirBnB_clone.git

## AUTHORS
-
Avelino Carvajal 

David Santiago Arias Lombana 

Cohorte 18
