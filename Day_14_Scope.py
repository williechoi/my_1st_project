class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max_diff = 0
        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                if max_diff < abs(a[i]-a[j]):
                    max_diff = abs(a[i]-a[j])

        self.maximumDifference = max_diff

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)