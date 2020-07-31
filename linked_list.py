# class of element object to add to our linked list
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
# linked list class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    # adds object to last position of our linked list. if the list is empty the given
    # element is added as a head.#
    def __str__(self):
        a = []
        current = self.head
        while current is not None:
            a.append(current.value)
            current = current.next
            print(a)
            return str(a)
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    # returns element at specified position.
    # positioning starts at 1 for head
    # if position is out of range it returns None
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    # adds new element at given element
    # just like in get position index starts at 1
    # for example if insert is at position 3 the new element is added between 2nd and 3rd element
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    # deletes the first element with given value
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next



