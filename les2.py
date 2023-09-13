class Queue:
    def __init__(self):
        self.items = []

   
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Черга порожня")

    def size(self):
        return len(self.items)

    def display(self):
        print("Елементи черги:", self.items)


queue = Queue()

while True:
    print("\n1. Додати елемент y чергу")
    print("2. Видалити елемент з черги")
    print("3. Вивести елементи черги")
    print("4. Вийти")

    choice = input("Виберіть опцію: ")

    if choice == '1':
        item = input
        queue.enqueue(item)
        print(item)

    elif choice == '2':
        if not queue.is_empty():
            removed_item = queue.dequeue()
            print(removed_item)
        else:
            print("Черга порожня")

    elif choice == '3':
        if not queue.is_empty():
            queue.display()
        else:
            print("Черга порожня")

    elif choice == '4':
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
