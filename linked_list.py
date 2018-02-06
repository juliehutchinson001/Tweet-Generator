class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({!r})'.format(self.data)


class Linked_list(object):

    def __init__(self, items=None):
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        items = []

        node = self.head  

        while node != None: 

            items.append(node.data)

            node = node.next  

        return items  

    def is_empty(self):
        if self.head is None:
            return True
        
        return False

    def length(self):
        # if self.is_empty():
        #     return 0
        # current_node = self.head
        # ctr = 1
        # while current_node.next != None:
        #     ctr += 1
        #     current_node = current_node.next
        # return ctr
        return self.size
 
    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.head = new_node
        self.size += 1


    def find(self, state_qual):
        current_node = self.head

        # while current_node.data != state_qual:
        #     current_node = current_node.next
        #     if current_node is None:
        #         return None
        # return current_node.data
        # Implementing find with callback (state_qual)
        while current_node is not None:
            if state_qual(current_node.data[0]):
                return current_node.data
            
            current_node = current_node.next

        return None

    def delete(self, item):
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        self.size -= 1

        if self.length() == 1:
            self.head = None
            self.tail = None
            return

        current_node = self.head

        while current_node.data != item:
            previous_node = current_node
            current_node = current_node.next

            if current_node is None:
                raise ValueError('Item not found: {}'.format(item))
        
        if current_node == self.head:
            self.head = current_node.next
            return

        if current_node == self.tail:
            self.tail = previous_node

            previous_node.next = None
            return

        previous_node.next = current_node.next


def main():
    # Testing Purposes 
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    ll = Linked_list()
    print(ll)
    ll.append(node1)
    print(ll)
    ll.append(node2)
    print(ll)
    ll.append(node3)
    print(ll)
    print(ll.head)

if __name__ == '__main__':
    main()


