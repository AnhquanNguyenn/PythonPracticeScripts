def num_ways_recursive(n, m):
    # base case, returning a 1 when we only have one move left to do
    # either move right 1 or move down 1
    if (n == 1 or m == 1):
        return 1

    # If we have acceptable moves, both left or right, we can recursively
    # find each route, because you can either go left or right
    return num_ways_recursive(n - 1, m) + num_ways_recursive(n, m - 1)


def num_ways_linear(n, m):
        # creating a 2D table for storage
    count = [[0 for x in range(n)] for y in range(m)]

    # count of paths to reach any column is 1
    for i in range(n):
        count[i][0] = 1

    # count of paths to reach any row is 1
    for j in range(m):
        count[0][j] = 1

    for i in range(1, n):
        for j in range(m):
            count[i][j] = count[i - 1][j] + count[i][j - 1]

        return count[n - 1][m - 1]


# Time Complexity: Exponential
print(num_ways_recursive(2, 2))

# Time Complexity: Linear
print(num_ways_linear(2, 2))
# 2
