# you are given array prices where prices[i] is the price of a given stock on the ith day
# you want to maximize profit by choosing single day to buy stock, and diff day in future to sell
# return max profit
prices = [7,1,5,3,6,4]
# output = 5

profit = 0
lowest = prices[1]
# the price to sell at must be after a value that is lower than it
for i in prices:
    if i < lowest:
        lowest = i
    profit = max(profit, i - lowest)

print(profit)