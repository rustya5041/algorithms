# this script contains the implementations of basic stack &
# stack with max extraction in python

# == LIFO == last in, first out
# each stack operation is O(1)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)


# on normal stack, max function will take O(n), 
# but we can make it O(1) by storing max as a stack object property
class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        cur_max = self.max_stack.top() if not self.max_stack.empty() else item
        to_push = max(cur_max, item)
        self.max_stack.push(to_push)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()
    
    def top(self):
        return self.stack.top()
    
    def max(self):
        return self.max_stack.top()
    
    def __str__(self):
        return f'stack: {str(self.stack)}, maxStack: {str(self.max_stack)}'
    
# if __name__ == '__main__':
#     s = MaxStack()
#     s.push(1)
#     s.push(3)
#     s.push(2)
#     s.push(150)
#     print(s.max())
#     print(s.pop())
#     print(s.max())