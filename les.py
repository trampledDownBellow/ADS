stack = []

def push_to_stack(number):
    stack.append(number)

def split_stack(stack, even_stack, odd_stack):
    if not stack:
        return
    else:
        number = stack.pop()
        split_stack(stack, even_stack, odd_stack) 
        if number % 2 == 0:
            even_stack.append(number)
        else:
            odd_stack.append(number)


def print_stack(stack):
    if not stack:
        return
    else:
        number = stack.pop()
        print(number)
        print_stack(stack)  


while True:
        number = int(input("Введіть число (або 0 для завершення): "))
        if number == 0:
            break
        push_to_stack(number)



even_stack = []
odd_stack = []

split_stack(stack, even_stack, odd_stack)
print("Стек чисел:")
print_stack(stack)
print("Парні числа:")
print_stack(even_stack)
print("Непарні числа:")
print_stack(odd_stack)
