class numb:
    def __init__(self):
        self.stack = []

    def is_even(self, num):
        return num % 2 == 0

    def push(self, num):
        if self.is_even(num):
            self.stack.append(num)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)


even_stack = numb()
even_stack.push(2)
even_stack.push(4)
even_stack.push(5) 
even_stack.push(5)
print("Stack:", even_stack.stack)  
print("Pop:", even_stack.pop())     
print("Peek:", even_stack.peek())   
print("Stack size:", even_stack.size())  
