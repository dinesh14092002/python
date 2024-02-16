# Function to find the minimum number of players who need to get shot
def min_players_to_be_shot(N, K, heights):
    count = 0
    for height in heights:
        if height >= K:
            count += 1
    return count

# Input the number of test cases
T = int(input("Enter the number of test cases: "))

# Iterate through each test case
for _ in range(T):
    # Input N and K for each test case
    N, K = map(int, input().split())
    # Input heights of players for each test case
    heights = list(map(int, input().split()))
    # Call the function to find the minimum number of players to be shot
    result = min_players_to_be_shot(N, K, heights)
    # Output the result
    print(result)
