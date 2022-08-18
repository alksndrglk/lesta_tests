class BufferFullException(BufferError):
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.box = []

    def read(self):
        if len(self.box) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        return self.box.pop(0)

    def write(self, data):
        if len(self.box) >= self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.box.append(data)

    def overwrite(self, data):
        if len(self.box) < self.capacity:
            self.write(data)
        else:
            self.read()
            self.write(data)

    def clear(self):
        self.box = []


# -------------------------------
"""
Обе релизации используют стандартный питоновский list, однако во втором случае мы заранее выделяем
память под полный размер циклицческого буффера.Во втором варианте есть возможность посмотреть на 
какой элемент сейчас ссылается "голова". А в первом варианте есть возможность перезаписи элементов с "хвоста".
Замечу, что одним из наиболее удобныхи и питонячих вариантов реализации, считаю работу с dequeue. 
"""
# -------------------------------
class CircularBuff:
    def __init__(self, max_size=10):
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return self.tail == (self.head - 1) % self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("CircularBuffer is full, unable to enqueue item")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def front(self):
        return self.buffer[self.head]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item
