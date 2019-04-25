# Example of in-place array reversal. Note that while sys.argv[] is considered
# a list in Python, technically it is implemented from C as an array.
#
# Time/space complexity: O(n) where n is the length of the array, and the
# array is only in the buffer.
#
# TODO: add recursion method

import sys

def convert_to_string(my_list):
    # The reason for doing this versus just casting my_list as str(my_list)
    # is that casting does not really create a string from the list, e.g. it
    # preserves the []s, ""s and 's. This function removes those to create a
    # proper string.
    #
    # There's a few ways to do this. 1 is to use a regular expression, e.g.
    #   my_str = re.sub(r'\[|\]|\'|\,', '', str(my_list))
    #   return my_str
    #
    # (have to import re if using this method)
    #
    # Another way is to concatenate the list elements into a string using the 
    # str method .join(), e.g.
    #   my_str = " ".join(my_list)
    #   return my_str (or just return the results of the join)
    #
    # Using the second method here for clarity.

    return " ".join(my_list)
# end convert_to_string()

def reverse_in_place(my_array):
# This method should work in any language

    # Declare head and tail pointers
    head = 0
    tail = len(my_array)-1

    while(head <= tail):

        # Point temp to head
        temp = my_array[head]

        # Point head to tail
        my_array[head] = my_array[tail]

        # Point tail to temp
        my_array[tail] = temp

        # Increment head
        head += 1

        # Decrement tail
        tail -= 1
    
    return my_array
# end reverse_in_place()

def reverse_iterable(my_iterable):

    print (f"\nReversing as {type(my_iterable)}")
    
    print(f"\nOriginal:\t{my_iterable}")

    if (type(my_iterable) == list):

        # Reverse list with the .reverse() method
        # first, make a copy of my_iterable to avoid modifying it which will
        # affect later reversals.
        my_iterable_copy = my_iterable.copy()

        my_iterable_copy.reverse()
        print(f".reverse():\t{my_iterable_copy}")
        
        # Reverse in-place
        # calling with a "shallow copy" ([:]) to avoid modifying my_iterable
        # This avoids "reversing the reverse" in subsequent reverse calls.
        print(f"In-place:\t{reverse_in_place(my_iterable[:])}")

        # A way to reverse each element within a list using a for-loop and
        # slicing
        print(f"for-loop:\t{[element[::-1] for element in my_iterable]}")

    # Slicing is the only reversal method as Python strings are immutable
    # NOTE: this makes a copy of iterable so will be slower than .reverse()
    print(f"Slicing:\t{my_iterable[::-1]}")

    return
# end reverse_my_iterable()

def main():

    # Different method to test input than try/catch
    if not sys.argv[1:]:
        print(f"\nPlease enter some characters/words\n")

    else:
        # Reverse as a Python list
        reverse_iterable(sys.argv[1:])

        # Reverse as a string
        reverse_iterable(convert_to_string(sys.argv[1:]))
# end main()

if __name__ == "__main__":
    main()
