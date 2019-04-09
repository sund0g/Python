# This example removes all duplicate characters from an input string and is
# unique to Python; other languages will have different algorithms as this
# solution uses Python methods "set()" to removes duplicates and ".join()" 
# to recreate the unordered and ordered duplicate-less strings.
#
# Time complexity: O(strbuffer)
#
# Space complexity: O(input_str + unordered_str + ordered_str) 

from collections import OrderedDict
import sys
import timeit

def main():

    try:
    # Add some whitespace at the end to verify ' 's are counted as duplicates.
        strbuffer = len(sys.argv[1]) + 10
    
    except:
        print(f"\nPlease enter a string\n")
        sys.exit(1)

    # Null terminate the string to verify removals after is is encountered.
    input_str = "{:{buffer}}".format(sys.argv[1]+'\0', buffer=strbuffer)

    # Not using f-strings here because I want to format with tabs.
    print("input string:\t\t'{}'".format(input_str))

    # set() returns the unique characters of the string in random order.
    # .join() returns the unique characters as a string. "" means no separator.
    unordered_str = "".join(set(input_str))

    print("unordered string:\t'{}'".format(unordered_str))

    # If order matters, use an ordered dictionary.
    ordered_str = "".join(OrderedDict.fromkeys(input_str))

    print("ordered string:\t\t'{}'".format(ordered_str))

if __name__ == "__main__":
    main()
