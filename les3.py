class ListManager:
    def __init__(self):
        self.my_list = []

    # Вставка елемента в список за індексом
    def insert_element(self, index, element):
        self.my_list.insert(index, element)

    # Локалізація елемента в списку
    def find_element(self, element):
        try:
            index = self.my_list.index(element)
            return f"Елемент {element} знаходиться в позиції {index}"
        except ValueError:
            return f"Елемент {element} не знайдено в списку"

    # Вибір елемента зі списку за індексом
    def select_element(self, index):
        try:
            return self.my_list[index]
        except IndexError:
            return "Недійсний індекс"

    # Вилучення елемента зі списку за індексом
    def delete_element(self, index):
        try:
            deleted_element = self.my_list.pop(index)
            return f"Вилучено елемент {deleted_element}"
        except IndexError:
            return "Недійсний індекс"

    # Вибірка попереднього і наступного елемента
    def get_previous_next(self, index):
        previous_index = index - 1
        next_index = index + 1

        previous = self.my_list[previous_index] if previous_index >= 0 else None
        next_element = self.my_list[next_index] if next_index < len(self.my_list) else None

        return f"Попередній елемент: {previous}, Наступний елемент: {next_element}"

    # Об'єднання двох списків в один
    def merge_lists(self, other_list):
        self.my_list.extend(other_list)

# Приклад використання
if __name__ == "__main__":
    list_manager = ListManager()

    list_manager.insert_element(0, 10)
    list_manager.insert_element(1, 20)
    list_manager.insert_element(2, 30)

    print(list_manager.my_list)  # Виводимо список: [10, 20, 30]

    print(list_manager.find_element(20))  # Локалізація елемента
    print(list_manager.select_element(1))  # Вибір елемента за індексом
    print(list_manager.delete_element(1))  # Вилучення елемента за індексом
    print(list_manager.my_list)  # Виводимо оновлений список: [10, 30]

    print(list_manager.get_previous_next(1))  # Вибірка попереднього і наступного елемента

    other_list = [40, 50]
    list_manager.merge_lists(other_list)
    print(list_manager.my_list)  # Об'єднання двох списків: [10, 30, 40, 50]
