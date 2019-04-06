import numpy
import sys
import timeit

def main():

#    str1 = sys.argv[0]
#    str2 = sys.argv[1]

    str1 = "clcl"
    str2 = "lclc"

    # lengths of the 2 strings
    str1_len = len(str1)
    str2_len = len(str2)

    # Truth table for the comparison.
    match_table = numpy.empty(shape=(str1_len, str2_len))

    # Maximum length of the substring.
    max_substrlen = 0 

    # substr to return
    substr = []

    # Iterate along each row
    for i in range(str1_len):
        # Iterate along each column
        for j in range(str2_len):
            # If the chars of each string match,
            if (str1[i] == str2[j]):
                # If either index is 0, start of a substr has been found.
                if (i==0 or j==0):
                    match_table[i][j] = 1
                else:
                    # Contiguous char has been found, add 1 to the previous match.
                    match_table[i][j] = match_table[i-1][j-1] + 1
                # If curent match sum > max_substrlen, a longer common substr
                # has been found. Reset max_substrlen to current match.
                if (match_table[i][j] > max_substrlen):
                    substr = []
                    max_substrlen = match_table[i][j]
                    substr.append(str1[int(i-max_substrlen+1):int(i+1)])
                elif (match_table[i][j] == max_substrlen):
                    substr.append(str1[int(i-max_substrlen+1):int(i+1)])
            else:
                match_table[i][j] = 0


#            lcs_temp = 0
#            match = ''
#            while ((i+lcs_temp < str1_len) and
#                    (j+lcs_temp < str2_len) and
#                    str1[i+lcs_temp] == str2[j+lcs_temp]):
#                match += str2[j+lcs_temp]
#                lcs_temp += 1
#            if (len(match) > len(substr)):
#                substr = match
#    print(f"longest common substr = {substr}")

    print(f"\ntruth table=\n{match_table}")

    print(f"\nlcs={substr}")

if __name__ == "__main__":
    main()
