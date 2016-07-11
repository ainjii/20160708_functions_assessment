# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def meal_plus_tax(cost, state, tax=0.05):
    """Calculates the cost of a meal plus tax.

    >>> meal_plus_tax(10, 'GA')
    10.5

    Returns total cost of meal plus tax.
    """

    if state == 'CA':
        return cost * 1.07
    else:
        return cost * (tax + 1)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_berry(fruit_name):
    """Determines whether a given fruit is a berry.

    >>> is_berry("strawberry")
    True

    >>> is_berry("cherry")
    True

    >>> is_berry("blackberry")
    True

    >>> is_berry("pear")
    False

    Returns boolean.
    """

    berries = ['strawberry', 'cherry', 'blackberry']

    if fruit_name in berries:
        return True
    else:
        return False

def shipping_cost(fruit_name):
    """Determines shipping cost for fruit.

    >>> shipping_cost("cherry")
    0

    >>> shipping_cost("pear")
    5

    Returns int.
    """

    if is_berry(fruit_name):
        return 0
    else:
        return 5

def is_hometown(town):
    """Determines whether the given town is my hometown.

    >>> is_hometown("Bethlehem")
    True

    >>> is_hometown("Philadelphia")
    False

    Returns boolean.
    """

    if town == 'Bethlehem':
        return True
    else:
        return False

def full_name(first, last):
    """Creates one full name from individual first and last names.

    >>> full_name("Angie", "Roscioli")
    'Angie Roscioli'

    Returns a string.
    """
    return first + ' ' + last

def hometown_greeting(first, last, town):
    """Prints a kind greeting.

    >>> hometown_greeting("Angie", "Roscioli", "Bethlehem")

    Returns nothing.
    """

    name = full_name(first, last)
    if is_hometown(town):
        "Hi, %s, we're from the same place!" % name
    else:
        print "Hi %s, where are you from?" % name

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x=1):
    """Increments a number.

    >>> a = increment()
    >>> a(5)
    6

    >>> addfive = increment(5)
    >>> addfive(5)
    10

    >>> addfive(20)
    25

    Returns the incremented number.
    """

    def add(y):
        return x + y

    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20. 
"""
See doctest above for part 2
"""

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def append(num, nums):
    """Adds a number to a list.

    >>> append(5, [1, 2, 3, 4])
    [1, 2, 3, 4, 5]

    Returns a list.
    """

    nums.append(num)
    return nums
#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print