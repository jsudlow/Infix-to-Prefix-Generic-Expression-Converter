#!/usr/bin/python
#stack implementation in python
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print 'stack popped off'
            return 'god-signal'
    def peek(self):
        return self.items[len(self.items) -1]
    def size(self):
        return len(self.items)





#stack = Stack()
#stack.push('jiggaman')
#print stack.is_empty()
#test = stack.pop()

#print test
#print stack.is_empty()
#g = stack.pop()
#print stack.is_empty()
