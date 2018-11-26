'''
Day 17: Exceptions
This program is for learning how to define custom exceptions
In this program, I intended to raise exception when at least one of two inputs is negative

'''


class Error(Exception):         # define general error
    pass


class NegativeError(Error):  # define custom error: all numbers should be non-negative
    pass


class Calculator:               # a class that calculates the power of two numbers
    def power(self, n, p):      # a specific method of power calculation
        if n < 0 or p < 0:      # check if there are no problems with the input: all inputs should be non-negative
            raise NegativeError('n and p should be non-negative') # throw error when at least one number is not positive
        else:                   # return the calculated answer if all are okay
            return n ** p

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)