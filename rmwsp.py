
import re  # Python Regular Expressions module
import sys

def main ():
    try:
        input_string = sys.argv[1]

    except:
        print(f"\nplease enter a string")

    else:
        # Substitute all whitespace (\s+) with nothing ('') in input_string
        string_with_whitespace_removed = re.sub(r'\s+', '', input_string)

        print(f"\nstring = {string_with_whitespace_removed}")

if __name__ == "__main__":
    main()
