#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0:
    return 1
  if n<= 2:
    return n
  
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

# Cookies: 0 => 1 [1]
# Cookies: 1 => 1 [1]
# Cookies: 2 => 2 [2] [1,1]
# Cookies: 3 => 4 [3] [2,1] [1,2] [1,1,1]
# 3:1
# 2:1 1:1 
# 1:1 2:1
# 1:3

# Cookies: 4 => 7 [3,1] [1,3] [2,2] [2,1,1] [1,2,1] [1,1,2] [1,1,1,1] 
# 3:1 1:1

# 2:2 
# 2:1 1:2

# 1:4
# 1:2 2:1
# 1:1 3:1
# 1:1 2:1 1:1

# Cookies: 5 => 13
# 3:1 2:1
# 3:1 1:2

# 2:2 1:1 
# 2:1 1:2 2:1
# 2:1 1:3 

# 1:5
# 1:1 3:1 1:1
# 1:1 2:2
# 1:1 2:1 1:2
# 1:2 3:1
# 1:2 2:1 1:1
# 1:2 2:2
# 1:3 2:1
# Cookies: 10 => 274


# print(eating_cookies(0)) # 1
# print(eating_cookies(1)) # 1
# print(eating_cookies(2)) # 2
# print(eating_cookies(5)) # 13
# print(eating_cookies(10))# 274