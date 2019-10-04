"""Functions that manipulate lists without using Python's built-in list methods.

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations.
They include:

    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

Implement functions that each use just one of the above operations.

The docstring of each function describes what it should do.

DO NOT USE ANY OF THE BUILT IN LIST METHODS, OR len()!
"""


def head(input_list):
    """Return the first element of the input list.

    For example:

    >>> head(['Jan', 'Feb', 'Mar'])
    'Jan'

    """
    month = input_list[0:1]

    return month[0]


def tail(input_list):
    """Return all elements of the input list except the first.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """

    return input_list[1:]

def last(input_list):
    """Return the last element of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """
    month = input_list[-1:]
    # print(month)
    return month[0]

def init(input_list):
    """Return all elements of the input list except the last.

    For example:

    >>> init(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """

    return input_list[:-1]

def first_three(input_list):
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """

    return input_list[:3]

def last_five(input_list):
    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """

    return input_list[-5:]


def middle(input_list):
    """Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """

    return input_list[2:-2]
    
##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#
# Please ask for a code review from an Education team member before proceeding.
##############################################################################

# This is the part were we actually run the doctests.

if __name__ == "__main__":

    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")