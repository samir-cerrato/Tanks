import sys
def maximize_eliminated_units(tanks):
    n = len(tanks)

    # Initialize a 2D table to store results of subproblems
    dp = [[0] * n for _ in range(n)]

    # For a single tank, the eliminated units will be its value multiplied by n
    for i in range(n):
        dp[i][i] = tanks[i] * n
    
    highest = -float('inf')

    # Build the table using bottom-up approach
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            day = n - length + 1

            dp[i][j] = max(tanks[i] * day + dp[i + 1][j], tanks[j] * day + dp[i][j - 1])

            if dp[i][j] > highest: 
                highest = dp[i][j]

    return highest

L = []
for line in sys.stdin:
    try:
        L.append(int(line))
    except:
        break

result = maximize_eliminated_units(L)
print(result)
