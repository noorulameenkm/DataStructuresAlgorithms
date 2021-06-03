"""
Time complexity - O(2 ^ m+n)
Space complexity - O(m+n)
"""
def find_SI(m, n,  p):
  return search(m, n, p, 0, 0, 0)

def search(m, n, p, mInd, nInd, pInd):
  mLen, nLen, pLen = len(m), len(n), len(p)

  if mInd == mLen and nInd == nLen and pInd == pLen:
    return True

  if pInd == pLen:
    return False
  
  b1, b2 = False, False
  if mInd < mLen and m[mInd] == p[pInd]:
    b1 = search(m, n, p, mInd+1, nInd, pInd+1)
  
  if nInd < nLen and n[nInd] == p[pInd]:
    b2 = search(m, n, p, mInd, nInd+1, pInd+1)

  return b1 or b2

def find_SI_memoization(m, n, p):
  return search_memoization({}, m, n, p, 0, 0, 0)

def search_memoization(dp, m, n, p, mIndex, nIndex, pIndex):
  mLen, nLen, pLen = len(m), len(n), len(p)
  # if we have reached the end of the all the strings

  if mIndex == mLen and nIndex == nLen and pIndex == pLen:
    return True

  # if we have reached the end of 'p' but 'm' or 'n' still has some characters left
  if pIndex == pLen:
    return False

  subProblemKey = str(mIndex) + "-" + str(nIndex) + "-" + str(pIndex)
  if subProblemKey not in dp:
    b1, b2 = False, False
    if mIndex < mLen and m[mIndex] == p[pIndex]:
      b1 = search_memoization(dp, m, n, p, mIndex + 1, nIndex, pIndex + 1)

    if nIndex < nLen and n[nIndex] == p[pIndex]:
      b2 = search_memoization(dp, m, n, p, mIndex, nIndex + 1, pIndex + 1)

    dp[subProblemKey] = b1 or b2

  return dp.get(subProblemKey)


"""
Time Complexity - O(m * n)
Space Complexity - O(m * n)
"""
def find_SI_tabulation(m, n, p):
    mLen, nLen, pLen = len(m), len(n), len(p)

    if (mLen + nLen) != pLen:
        return False

    dp = [[False for _ in range(nLen + 1)] for _ in range(mLen + 1)]

    for mInd in range(mLen + 1):
        for nInd in range(nLen + 1):

            if mInd == 0 and nInd == 0:
                dp[mInd][nInd] = True
            elif mInd == 0 and n[nInd - 1] == p[mInd + nInd - 1]:
                dp[mInd][nInd] = dp[mInd][nInd - 1]
            elif nInd == 0 and m[mInd - 1] == p[mInd + nInd - 1]:
                dp[mInd][nInd] = dp[mInd - 1][nInd]
            else:
                if mInd > 0 and m[mInd - 1] == p[mInd + nInd - 1]:
                    dp[mInd][nInd] = dp[mInd - 1][nInd]
                
                if nInd > 0 and n[nInd - 1] == p[mInd + nInd - 1]:
                    dp[mInd][nInd] |= dp[mInd][nInd - 1]
                
    
    return dp[mLen][nLen]
            

def main():
  print(find_SI("abd", "cef", "abcdef"))
  print(find_SI("abd", "cef", "adcbef"))
  print(find_SI("abc", "def", "abdccf"))
  print(find_SI("abcdef", "mnop", "mnaobcdepf"))

  # memoization
  print(find_SI_memoization("abd", "cef", "abcdef"))
  print(find_SI_memoization("abd", "cef", "adcbef"))
  print(find_SI_memoization("abc", "def", "abdccf"))
  print(find_SI_memoization("abcdef", "mnop", "mnaobcdepf"))

  # Tabulation
  print(find_SI_tabulation("abd", "cef", "abcdef"))
  print(find_SI_tabulation("abd", "cef", "adcbef"))
  print(find_SI_tabulation("abc", "def", "abdccf"))
  print(find_SI_tabulation("abcdef", "mnop", "mnaobcdepf"))


main()