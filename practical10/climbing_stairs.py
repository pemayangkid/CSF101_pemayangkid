def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

test_cases = [1, 2, 3, 5, 45]

for n in test_cases:
    print(f"climbStairs({n}) = {climbStairs(n)}")