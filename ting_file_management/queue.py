from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._items = list()

    def __len__(self) -> int:
        return len(self._items)

    def enqueue(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("O valor deve ser um inteiro.")
        self._items.append(value)

    def dequeue(self) -> None | int:
        if len(self._items) == 0:
            return None
        return self._items.pop(0)

    def search(self, index: int) -> Exception | int:
        if (index < 0) or (index > (len(self._items) - 1)):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._items[index]
