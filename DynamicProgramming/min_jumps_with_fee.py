def find_min_fee(fee):
  return find_min_fee_recursive(fee, 0)


"""
Time complexity - O(3 ^ N)
Space complexity - O(N)
"""
def find_min_fee_recursive(fee, currentIndex):
  n = len(fee)
  if currentIndex > n - 1:
    return 0

  # if we take 1 step, we are left with 'n-1' steps;
  take1Step = find_min_fee_recursive(fee, currentIndex + 1)
  # similarly, if we took 2 steps, we are left with 'n-2' steps;
  take2Step = find_min_fee_recursive(fee, currentIndex + 2)
  # if we took 3 steps, we are left with 'n-3' steps;
  take3Step = find_min_fee_recursive(fee, currentIndex + 3)

  _min = min(take1Step, take2Step, take3Step)

  return _min + fee[currentIndex]


def find_min_fee_memoization(fee):
  dp = [0 for x in range(len(fee))]
  return find_min_fee_memoization_recursive(dp, fee, 0)


def find_min_fee_memoization_recursive(dp, fee, currentIndex):
    n = len(fee)
    if currentIndex > n-1:
        return 0

    if dp[currentIndex] == 0:
        # if we take 1 step, we are left with 'n-1' steps
        take1Step = find_min_fee_memoization_recursive(dp, fee, currentIndex + 1)
        # similarly, if we took 2 steps, we are left with 'n-2' steps
        take2Step = find_min_fee_memoization_recursive(dp, fee, currentIndex + 2)
        # if we took 3 steps, we are left with 'n-3' steps
        take3Step = find_min_fee_memoization_recursive(dp, fee, currentIndex + 3)

        dp[currentIndex] = fee[currentIndex] + min(take1Step, take2Step, take3Step)

    return dp[currentIndex]

def find_min_fee_tabulation(fee):
  n = len(fee)
  dp = [0 for x in range(n+1)]  # +1 to handle the 0th step
  dp[0] = 0  # if there are no steps, we don't have to pay any fee
  dp[1] = fee[0]  # only one step, so we have to pay its fee
  # for 2 steps, since we start from the first step, so we have to pay its fee
  # and from the first step we can reach the top by taking two steps, so
  # we don't have to pay any other fee.
  dp[2] = fee[0]

  # please note that dp[] has one extra element to handle the 0th step
  for i in range(2, n):
    dp[i + 1] = min(fee[i] + dp[i], 
                    fee[i - 1] + dp[i - 1], 
                    fee[i - 2] + dp[i - 2])

  return dp[n]


def main():
    # First Approach
    print(find_min_fee([1, 2, 5, 2, 1, 2]))
    print(find_min_fee([2, 3, 4, 5]))

    # Second Approach
    print(find_min_fee_memoization([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_memoization([2, 3, 4, 5]))


    # Third Approach
    print(find_min_fee_tabulation([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_tabulation([2, 3, 4, 5]))


main()