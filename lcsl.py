# Example of finding the longest common substring between two strings using
# Dynamic Programming. This example returns the substring in list format to
# account for the possibility of multiple substring occurrences.
#
# Time complexity: O(str1_len * str2_len)
# Space complexity: O(str1_len * str2_len) There is a better way to do this,
# using only the last 2 rows of the match table rather than creating it with
# the full size of the strings, e.g.
# https://www.quora.com/How-do-I-optimize-the-Longest-Common-Sub-sequence-algorithm-so-that-it-works-better-than-the-O-m*n-complexity

import numpy
import sys

def main():

    try:
        str1=sys.argv[1]
        str2=sys.argv[2]
    
    except:
        print (f"\nPlease provide 2 \"-delimited strings to compare\n")
        sys.exit(1)

    # Lengths of the 2 strings
    str1_len = len(str1)
    str2_len = len(str2)

    # Truth table for the comparison
    match_table = numpy.empty(shape=(str1_len, str2_len))

    # Maximum length of the substring
    max_substrlen = 0 

    # List of substrings to return
    substr_list = []

    # Iterate along each row
    for i in range(str1_len):
    # Iterate along each column
        for j in range(str2_len):
    # If the chars of each string match, a substr has been found
            if (str1[i] == str2[j]):
    # If either index is 0, start of a substr has been found
                if (i==0 or j==0):
    # Set the location in match_table to 1
                    match_table[i][j] = 1
                else:
    # A contiguous char has been found, add 1 to the previous match
                    match_table[i][j] = match_table[i-1][j-1] + 1
    # If curent match sum > max_substrlen, a longer common substr has been found
                if (match_table[i][j] > max_substrlen):
    # Reset substr_list. .clear takes less space than substr_list = []
                    substr_list.clear()
    # Reset max_substrlen to current match
                    max_substrlen = match_table[i][j]
    # Replace the previous substr with the start of the new one 
                    substr_list.append(str1[int(i-max_substrlen+1):int(i+1)])
                elif (match_table[i][j] == max_substrlen):
    # Append the character to the substring in the list
                    substr_list.append(str1[int(i-max_substrlen+1):int(i+1)])
            else:
    # Chars don't match, move on
                match_table[i][j] = 0

    print(f"\ntruth table =\n{match_table}")

    print(f"\nlongest common substring(s) = {substr_list}")

if __name__ == "__main__":
    main()
