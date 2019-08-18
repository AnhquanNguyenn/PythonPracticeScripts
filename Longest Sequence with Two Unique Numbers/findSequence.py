# Python 3 program to find longest
# subarray with k or less distinct elements.

# function to print the longest sub-array


def findSequence(seq):
    n = len(seq)  # the end value for the loop
    k = 2			# the number of unique values we want

    # empty list to hold which values have been visited and longest sequence
    freq = [0] * n

    start = 0			# start of current longest sequence
    end = 0				# end of current longest sequence
    uniqueNumbers = 0  	# number of unique numbers increments as we go through the list
    l = 0
    for i in range(n):

        # mark the element visited
        freq[seq[i]] += 1

        # if its visited first time, then increase
        # the counter of distinct elements by 1
        if (freq[seq[i]] == 1):
            uniqueNumbers += 1

        # When the counter of distinct elements
        # increases from k, then reduce it to k
        while (uniqueNumbers > k):

            # from the left, reduce the number
            # of time of visit
            freq[seq[l]] -= 1

            # if the reduced visited time element
            # is not present in further segment
            # then decrease the count of distinct
            # elements
            if (freq[seq[l]] == 0):
                uniqueNumbers -= 1

            # increase the subsegment mark
            l += 1

        # check length of longest sub-segment
        # when greater then previous best
        # then change it
        if (i - l + 1 >= end - start + 1):
            end = i
            start = l

    newList = []
    # print the longest sub-segment
    for i in range(start, end + 1):
        newList.append(seq[i])
        print(seq[i], end=" ")

    print("\nThe Length of the longest sequence of 2 unique numbers is: ", len(newList))


# Driver Code
if __name__ == "__main__":

    seq = [1, 3, 5, 3, 1, 3, 1, 5]
    seq1 = [1, 1, 1, 1, 1, 1, 2]
    findSequence(seq)
    findSequence(seq1)
'''
def findSequence(seq):
	i = 0
	j = 1
	counter = 0
	sequence = []
	checkSequence = []

	while i < len(seq):
		if ((seq[i] in sequence) == False):
			sequence.append(seq[i])
			counter += 1
		else: 
			sequence.append(seq[i])
		# If we have more than 2 unique numbers then we're going to clear the array 
		# and move the 
		if counter > 2:
			sequence.clear()
			sequence.append(seq[j])


	


print findSequence([1, 3, 5, 3, 1, 3, 1, 5])
# 4
'''
