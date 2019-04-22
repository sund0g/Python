# Example of in-place array reversal. Note that while sys.argv[] is considered
# a list in Python, technically it is implemented from C as an array.
#
# Time/space complexity: O(n) where n is the length of the array, and the
# array is only in the buffer.

import sys

def reverse_in_place(array):
    # Declare head and tail pointers
    head = 0
    tail = len(array)-1

    while(head <= tail):

        # Point temp to head
        temp = array[head]

        # Point head to tail
        array[head] = array[tail]

        # Point tail to temp
        array[tail] = temp

        # Increment head
        head += 1

        # Decrement tail
        tail -= 1
    
    return array
# end reverse_in_place()

def main():

    # Different method to test input than try/catch
    if not sys.argv[1:]:
        print(f"\nPlease enter some ' '-delimited characters/words\n")

    else:
        print(f"\noriginal string: {sys.argv[1:]}")
        print(f"reversed string: {reverse_in_place(sys.argv[1:])}")

if __name__ == "__main__":
    main()
