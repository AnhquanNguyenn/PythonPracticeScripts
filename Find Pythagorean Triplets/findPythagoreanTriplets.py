def findPythagoreanTriplets(nums):
    # Fill this in.
    # Square all the elements to prepare calcualtions for addition
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    # sorting the array in order
    nums.sort()

    # range(start value, end value, step)
    # fix one element and then try to find the other two to make it equal
    # start index variables at both corners
    for i in range((len(nums) - 1), 1, -1):
        j = 0
        k = i - 1
        # stop when when index overlaps
        while j < k:
            # found a triple
            if (nums[j] + nums[k] == nums[i]):
                return True
            else:
                # if the sum is less, move the smallest number to a higher number
                if (nums[j] + nums[k] < nums[i]):
                    j += 1
                # if sum is more, then move the total sum to be smaller
                else:
                    k -= 1

    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
