# Python program to implement stack

class stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self):
        data = int(input("Enter an element to pushed :"))
        self.item.append(data)

    def pop(self):
        print("Popped value : ",self.item.pop())

    def peek(self):
        if self.is_empty():   # if self.item == [] it also work
            print("Stack is empty!..")
        else:
            print("Top most element of stack : ", self.item[-1])

    def display(self):
        if self.is_empty():
            print("stack is empty ")
        for i in self.item:
            print("Elements of stack : ", i)

s = stack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")
    print("5. Display")
    do = int(input("What do you want to do : "))

    opreation = do
    if opreation == 1:
        s.push()

    elif opreation == 2:
        if s.is_empty():
            print("Stack is empty!.")
        else:
            s.pop()

    elif opreation == 3:
        s.peek()

    elif opreation == 4:
        print("Bye.....")
        exit()

    elif opreation == 5:
        s.display()

    else:
        print("Invalid choice..")
