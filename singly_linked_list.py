import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            sys.exit("Empty list no elements in the linked list")
        else:
            sl_list = []
            ptr = self.head
            while ptr.next is not None:
                sl_list.append(ptr.data)
                ptr = ptr.next
            sl_list.append(ptr.data)
            # sl_list.remove(None)
            print("->".join(str(i) for i in sl_list))

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None

    def delete_head(self):
        if self.head is None:
            print("No elements in the list, deletion not possible")
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            second_node = current_node.next
            current_node.next = None
            self.head = second_node

    def delete_tail(self):
        if self.head is None:
            print("No elements in the list, deletion not possible")
        else:
            current_node = self.head
            second_node = current_node.next
            while second_node.next is not None:
                current_node = current_node.next
            current_node.next = None


if __name__ == '__main__':
    sl = SinglyLinkedList()
    run_again = "y"
    while run_again == "y":
        operation = input("(i) Insert or (d) Delete or (e) Exit: ")
        if operation == "e":
            sys.exit("Exit operation commanded")
        operation_type = input(f"Operation on - (t) Tail, (h) Head: ")
        if operation == "e":
            sys.exit("Exit operation commanded")
        elif operation == "i":
            val = int(input(f"Value to insert: "))
            if operation_type == 'h':
                sl.insert_head(val)
                sl.traverse()
            elif operation_type == 't':
                sl.insert_tail(val)
                sl.traverse()
        elif operation == "d":
            if operation_type == "h":
                sl.delete_head()
                sl.traverse()
            elif operation_type == "t":
                sl.delete_tail()
                sl.traverse()
        run_again = input("Want to run program again - (y)Yes or (n)No: ")
        if run_again == "n":
            sys.exit("Exit operation commanded")
