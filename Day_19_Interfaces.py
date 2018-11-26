'''
Day 19: Interfaces
This program is for learning the concept of interface
In this program, the AdvancedArithmetic interface is defined,
and is followed by the Calculator class which implements the interface
It seems to me that interface >> class >> instance in terms of the level of concreteness

'''


class AdvancedArithmetic(object):       # define the interface AdvancedArithmetic
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):   # define the Calculator class that implements the interface AdvancedArithmetic
    def divisorSum(self, n):            # define the method of the calculator class: divisor sum
        total_sum = 0                   # define the outcome variable < total_sum > as 0
        for i in range(1,n+1):          # check all the numbers from 1 to n
            if n % i == 0:              # if i is a divisor of n,
                total_sum += i          # add i to the outcome variable : total_sum
        return total_sum                # return the outcome variable


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)