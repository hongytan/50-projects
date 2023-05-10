'''
    Strategy for this problem is to essentially in one loop through the array:
        1. Find the minimum value
        2. Find the maximum profit for this minimum value

    (1) can be done by checking if current min > current value or
        using 'pointers' like the algorithm below
'''

def maxProfit(prices): # O(n) time
    n = len(prices)
    max_profit = 0
    i = 0 # Left pointer
    j = 1 # Right pointer

    while j < n:
        if prices[i] <= prices[j]:
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            j += 1
        else:
            i = j
            j += 1

    print(max_profit)

n = [886,729,539,474,5,653,588,198,313,111,38,808,848]

maxProfit(n)

def maxProfit2(prices):
    '''
    Here is another way, which I thought is really clean.
    '''
    
    profit = 0
    x=10001 # Constrants say that values are between 0 and 10,000

    for i in prices:
        if x > i:
            x = i
        elif i-x > profit:
            profit = i-x

    return profit