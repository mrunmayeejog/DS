"""
Stack is a linear data structure which follows a particular order in which the operations are performed.
The order may be LIFO(Last In First Out) or FILO(First In Last Out) and all following APIs take place in O(1)
empty() - Check if stack is empty
size() – Returns the size of the stack – Time Complexity : O(1)
top() – Returns a reference to the top most element of the stack
push(g) – Adds the element g at the top of the stack
pop() – Deletes the top most element of the stack
peek() -  Return top element
Implementation of Stack in Python can be done using List and deque classes from collections module with append() and pop() functions.
Stack can also be implemented using linkedlist and array as well.
Standard problems based on stack are : Infix, prefix, postfix problems, Tower of Hanoi, balanced parenthesis evaluation, arithmatic expression evaluation etc
"""


Max = 20


class Array_stack:
    def __init__(self):
        self.top = -1
        self.stack = Max * [None]

    def peek(self):
        print(self.stack[self.top])
        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == Max - 1:
            return True
        return False

    def push(self, val):
        if self.is_full():
            return
        if val:
            self.top += 1
            self.stack[self.top] = val

    def pop(self):
        if self.is_empty():
            return
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def print_stack(self):
        if not self.is_empty():
            for each in self.stack:
                if each:
                    print((' ' + str(each)), end=' ')

        else:
            print('Stack is empty')


if __name__ =="__main__":
    s = Array_stack()
    s.is_full()
    s.print_stack()