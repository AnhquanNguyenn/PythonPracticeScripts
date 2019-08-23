class Solution:
    def minSubArrayLen(self, nums, s):
        n = len(nums)
        current_sum = 0
        min_length = float('inf')
        j = 0
        for i in range(n):
            while (current_sum <= s and j < n):
                current_sum += nums[j]
                j += 1

            # when we reach a sum greater than or equal to the target we need to adjust the min length if needed
            if current_sum >= s:
                # min length is either the current subarray or the current one
                min_length = min(j - i, min_length)
                # current sum is the current sum - the first subarray value
                current_sum = current_sum - nums[i]

        if min_length == float('inf'):
            return 0
        else:
            return min_length


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 9))
