# Python program to implement Reversed a stck using recursion

class stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def display(self):
        for data in reversed(self.item):
            print(data)

    def insert_at_bottom(self, data):
        if self.is_empty():
            self.push(data)
        else:
            popped = self.pop()
            self.insert_at_bottom(data)
            self.push(popped)

    def reversed_stack(self):
        if not self.is_empty():
            popped = self.pop()
            self.reversed_stack()
            self.insert_at_bottom(popped)

s = stack()
data_list = input("Enter an elements to push : ").split()
for data in data_list:
    s.push(int(data))

print("The stack : ")
s.display()
s.reversed_stack()
print("After reversing : ")
s.display()


# Python program to implement Reversed a stck using recursion
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
 
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
 
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()
