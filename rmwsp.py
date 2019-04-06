# This is an example of removing all whitespace, (not just spaces) from a
# string using the Regular Expressions module re and .sub method to
# replace all instances of whitespace with no space.
#
# Reference: https://docs.python.org/3/library/re.html
#
# the returned string is enclosed in "" to verify that leading/trailing
# whitespace is being removed.
#
# Time complexity: O(re*strlen) where re is the size of the regular expression,
# and strlen is the length of the input string.
#
# Space complexity: n as the string is only in the buffer.

import re
import sys

def main ():
    try:
        # Substitute all whitespace (\s+) with no space ('') in input_string
        print("\nstring = \"{}\"\n".format(re.sub(r'\s+', '', sys.argv[1])))

    except:
        print(f"\nplease enter a \"-delimited string\n")

if __name__ == "__main__":
    main()

