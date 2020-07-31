class Element:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = element
            element.prev = current
        else:
            self.head = element

    def get_element(self, position):
        counter = 1
        current = self.head
        if position > 1:
            while counter < position and current.next:
                current = current.next
                