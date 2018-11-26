import sys


class Solution:
    def __init__(self):
        self.stack_a = []           # instance attribute: a stack (list type)
        self.queue_a = []           # instance attribute: a queue (list type)

    def pushCharacter(self, char):
        self.stack_a.append(char)   # push a character into the stack

    def enqueueCharacter(self, char):
        self.queue_a.append(char)   # enqueue a character into the queue

    def popCharacter(self):
        return self.stack_a.pop()   # pop the top thing from the stack

    def dequeueCharacter(self):
        return self.queue_a.pop(0)  # dequeue the first thing from the queue

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")