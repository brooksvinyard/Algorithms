#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  profit = -math.inf
  # Have to buy before the last number
  # Have to sell before the last number
  # Need to find the maximum between the minimum number and the max number

  # Loop through each value in the array => i
  #   Loop through the rest of the values in the array => j
  #   subtract j-i to find the biggest
  for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
      if prices[j]-prices[i] > profit:
        profit = prices[j]-prices[i]

  print("prices:", prices, "profit:", profit)
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))