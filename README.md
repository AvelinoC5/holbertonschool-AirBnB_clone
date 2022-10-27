# :bulb: holbertonschool-AirBnB_clone :bulb:

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

### Resources

Read or watch:

 >UUID
* [Youtube Uuid](https://www.youtube.com/watch?v=MUK5qZxlWFg)
* [UUID objects according to RFC 4122](https://docs.python.org/3.8/library/uuid.html)
* [How to create a GUID/UUID in Python](https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python)
 
 >Datatime
* [Isoformat() Method Of Datetime Class In Python](https://www.geeksforgeeks.org/isoformat-method-of-datetime-class-in-python/)
* [Python datetime](https://www.programiz.com/python-programming/datetime)
* [La librería Datetime](https://aprendeconalf.es/docencia/python/manual/datetime/)
 
 >Dictionary
* [How to Update a Python Dictionary?](https://www.askpython.com/python/dictionary/how-to-update-a-python-dictionary#:~:text=In%20order%20to%20update%20the,key%20in%20the%20input%20dictionary)
* [dict python](https://j2logo.com/python/tutorial/tipo-dict-python/#:~:text=Para%20crear%20un%20diccionario%20vac%C3%ADo,Sin%20par%C3%A1metros)
* [Agregar diccionario en Python](https://www.delftstack.com/es/howto/python/add-dictionary-to-a-dictionary-python/)
* [Python Remove Key from a Dictionary: A Complete Guide](https://careerkarma.com/blog/python-remove-key-from-a-dictionary/#:~:text=The%20Python%20del%20statement%20deletes,not%20present%20in%20a%20dictionary)
* [How to avoid "RuntimeError: dictionary changed size during iteration" error?](https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error)
* [Check if a Key Exists in a Python Dictionary](https://able.bio/rhett/check-if-a-key-exists-in-a-python-dictionary--73iajoz#:~:text=To%20simply%20check%20if%20a,%23%20Dogs%20found!&text=A%20dictionary%20can%20be%20a,counting%20the%20occurrence%20of%20items)
* [Función Pandas DataFrame.to_dict()](https://www.delftstack.com/es/api/python-pandas/pandas-dataframe-dataframe.to_dict-function/)
* [Convertir dos listas en diccionario en Python](https://www.delftstack.com/es/howto/python/python-convert-list-into-dictionary/#:~:text=contiene%20los%20valores.-,Usar%20zip()%20y%20dict()%20para%20convertir%20dos%20listas,partir%20de%20la%20colecci%C3%B3n%20dada)

>args kwargs
* [How To Use *args and **kwargs in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
* [*args and **kwargs](https://book.pythontips.com/en/latest/args_and_kwargs.html)
 
 >setattr()
* [Python setattr()](https://www.programiz.com/python-programming/methods/built-in/setattr)

>JSON
* [json.dump() in Python](https://www.geeksforgeeks.org/json-dump-in-python/)
* [Validate JSON data using Python](https://pynative.com/python-json-validation/)
* [json.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 190) [duplicate]](https://stackoverflow.com/questions/48140858/json-decoder-jsondecodeerror-extra-data-line-2-column-1-char-190)
* [Python Cheat Sheet](https://blog.finxter.com/como-agregar-datos-a-un-archivo-json-en-python-video/#:~:text=Para%20actualizar%20un%20objeto%20JSON,dump(data%2C%20file)%20)
* [Pretty Print a JSON File in Python](https://www.delftstack.com/howto/python/how-to-pretty-print-a-json-file/)

>load and dumps
* [Reading and Writing JSON to a File in Python](https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/)
* [How to update a JSON file in Python](https://www.adamsmith.haus/python/answers/how-to-update-a-json-file-in-python)

>Reload
* [Reloading modules in Python](https://www.geeksforgeeks.org/reloading-modules-python/#:~:text=reload()%20reloads%20a%20previously,which%20has%20been%20successfully%20imported)
* [Reloading modules in Python?](https://www.tutorialspoint.com/reloading-modules-in-python)
* [Reloading a Module](https://realpython.com/lessons/reloading-module/)
* [How do I unload (reload) a Python module?](https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module)

>unittest
* [A simple Python unittest](https://www.pythonsheets.com/notes/python-tests.html)
* [unittest — Unit testing framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python unittest – assertIsInstance() function](https://www.geeksforgeeks.org/python-unittest-assertisinstance-function/)
* [Tutorial unittest capítulo 1: Introducción y ejemplo](https://www.youtube.com/watch?v=1UtkZHHOBWo)

>cmd
* [cmd — Soporte para intérpretes orientados a línea de comandos](https://docs.python.org/es/3/library/cmd.html)
* [cpython](https://github.com/python/cpython/blob/3.10/Lib/cmd.py)
* [Multiple Ways To Print Blank Line in Python](https://www.pythonpool.com/python-print-blank-line/)

>__str__ and __repr__
* [What is the difference between __str__ and __repr__?](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr)
* [Python - Public, Protected, Private Members](https://www.tutorialsteacher.com/python/public-private-protected-modifiers)

## AUTHORS
- Avelino Carvajal C18

- David Santiago Arias Lombana C18
