class ListManager:
    def __init__(self):
        self.my_list = []

    def insert(self, index, element):
        self.my_list.insert(index, element)

    def find(self, element):
        try:
            index = self.my_list.index(element)
            return f"Елемент {element} знаходиться в поx`зиції {index}"
        except ValueError:
            return f"Елемент {element} не знайдено в списку"

    def select(self, index):
        try:
            return self.my_list[index]
        except IndexError:
            return "Недійсний індекс"

    def delete(self, index):
        try:
            deleted_element = self.my_list.pop(index)
            return f"Вилучено елемент {deleted_element}"
        except IndexError:
            return "Недійсний індекс"

    def get_neighbors(self, index):
        prev_index, next_index = index - 1, index + 1
        prev = self.my_list[prev_index] if prev_index >= 0 else None
        next_element = self.my_list[next_index] if next_index < len(self.my_list) else None
        return f"Попередній елемент: {prev}, Наступний елемент: {next_element}"

    def merge(self, other_list):
        self.my_list.extend(other_list)


if __name__ == "__main__":
    list_manager = ListManager()

    list_manager.insert(0, 10)
    list_manager.insert(1, 20)
    list_manager.insert(2, 30)

    print(list_manager.my_list)

    print(list_manager.find(20))
    print(list_manager.select(1))
    print(list_manager.delete(1))
    print(list_manager.my_list)

    print(list_manager.get_neighbors(1))

    other_list = [40, 50]
    list_manager.merge(other_list)
    print(list_manager.my_list)
