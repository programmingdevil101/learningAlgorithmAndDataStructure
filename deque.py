class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element, position = 'first'):
        n = 0
        if position == 'last':
        	n = 0
        elif position != 'first':
        	raise Exception('Enter valid input')
        self.storage.append(n)

    def peek(self, position = 'first'):
        return self.storage[0] 

    def dequeue(self, position = 'first')
        a = self.storage.pop(0)
        return a