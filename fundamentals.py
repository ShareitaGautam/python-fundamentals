# This line makes sure the code runs only when the file is executed directly
if __name__ == '__main__':

    # -------------------------------
    # STRING SLICING
    # -------------------------------

    b = "Hello, World!"
    print(b[2:8])  # prints characters from index 2 to 7

    b = "Hello, World!"
    print(b[-5:-2])  # prints characters using negative index (from end)

    # -------------------------------
    # STRING CASE METHODS
    # -------------------------------

    a = "Hello, World!"
    print(a.upper())  # converts string to uppercase

    a = "Hello, World"
    print(a.lower())  # converts string to lowercase

    # -------------------------------
    # REMOVE WHITESPACE
    # -------------------------------

    a = " Hello, World! "
    print(a.strip())  # removes spaces from beginning and end

    # -------------------------------
    # REPLACE TEXT
    # -------------------------------

    a = "Hello, World!"
    print(a.replace("H", "J"))  # replaces H with J

    # -------------------------------
    # SPLIT STRING
    # -------------------------------

    a = "Hello, World!"
    print(a.split(","))  # splits string at comma

    # -------------------------------
    # STRING CONCATENATION
    # -------------------------------

    a = "Hello"
    b = "World"

    c = a + b  # combine without space
    c = a + " " + b  # combine with space
    print(c)

    # -------------------------------
    # STRING FORMAT METHOD
    # -------------------------------

    age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age))  # inserts age into string

    quantity = 3
    itemno = 567
    price = 49.95

    myorder = "I want {} pieces of item {} for {} dollars."
    print(myorder.format(quantity, itemno, price))

    # using index numbers in format
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(price, itemno, quantity))

    # -------------------------------
    # BOOLEAN COMPARISON
    # -------------------------------

    print(10 > 9)   # True
    print(10 == 9)  # False
    print(10 < 9)   # False

    # -------------------------------
    # IF ELSE CONDITION
    # -------------------------------

    a = 200
    b = 33

    if b > a:
        print("b is greater than a")
    else:
        print("a is greater than b")

    # -------------------------------
    # BOOLEAN VALUES
    # -------------------------------

    print(bool("abc"))  # True (string is not empty)
    print(bool(123))    # True
    print(bool(["apple", "cherry", "banana"]))  # True

    print(bool(False))  # False
    print(bool(None))   # False
    print(bool(''))     # False
    print(bool())       # False
    print(bool([]))     # False

    # -------------------------------
    # NUMBER TYPES
    # -------------------------------

    x = 1      # integer
    y = 2.8    # float

    print(type(x))
    print(type(y))

    # large integers and negative integers
    x = 1
    y = 3456723456
    z = -2344522

    print(type(x))
    print(type(y))
    print(type(z))

    # -------------------------------
    # TYPE CONVERSION
    # -------------------------------

    x = 1
    y = 2.8

    a = float(x)  # convert int to float
    b = int(y)    # convert float to int

    print(a)
    print(b)

    print(type(a))
    print(type(b))

    # -------------------------------
    # RANDOM NUMBERS
    # -------------------------------

    import random

    print(random.randrange(1, 10))  # random number from 1 to 9
    print(random.randint(1, 10))    # random number from 1 to 10

    # -------------------------------
    # DICTIONARY BASICS
    # -------------------------------

    # dictionary example
    thisdinct = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    print(thisdinct["year"])  # get value using key
    print(len(thisdinct))     # number of items in dictionary

    # create dictionary using dict() function
    thisdict = dict(name="John", age=36, country="Norway")
    print(thisdict)

    # get specific value
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    x = thisdict["model"]
    print(x)

    # -------------------------------
    # GET KEYS AND VALUES
    # -------------------------------

    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    y = car.keys()
    print(y)  # show keys

    car["color"] = "white"  # add new key
    print(y)

    z = thisdict.values()
    print(z)  # show values

    x = car.values()
    print(x)

    car["year"] = 1984  # change value
    print(x)

    x = thisdict.items()
    print(x)  # show key and value pairs

    # -------------------------------
    # CHECK IF KEY EXISTS
    # -------------------------------

    if "color" in thisdict:
        print("'color' exists")
    else:
        print("'color' does not exist")

    # -------------------------------
    # REMOVE ITEMS FROM DICTIONARY
    # -------------------------------

    thisdisct = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdisct.pop("model")  # removes model
    print(thisdisct)

    # delete entire dictionary
    thisdisct = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    del thisdisct

    # clear dictionary (remove all items)
    thisdisct = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    thisdisct.clear()
    print(thisdisct)

    # -------------------------------
    # LOOP THROUGH DICTIONARY
    # -------------------------------

    thisdisct = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    # print keys
    for x in thisdisct:
        print(x)

    # print values
    for x in thisdisct.values():
        print(x)

    # print keys again
    for x in thisdisct.keys():
        print(x)

    # print keys and values
    for x, y in thisdisct.items():
        print(x, y)

    # -------------------------------
    # COPY DICTIONARY
    # -------------------------------

    mydict = thisdisct.copy()
    print(mydict)

    # another way to copy
    mydict = dict(thisdisct)
    print(mydict)
