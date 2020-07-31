import sys
from list_creation import unordered_array  # list of numbers of desired length randomly ordered no repetition


class QueueOverflow(Exception):
    pass


class QueueUnderflow(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = unordered_array(length_array)
        self.limit = limit_array
        self.length = len(self.queue)
        self.front = self.length-1
        self.rear = 0

    def is_full(self):
        if self.front >= self.limit:
            raise QueueOverflow("Queue Overflow")
        else:
            print("Space available for operations :)")

    def is_empty(self):
        if self.length == self.rear:
            raise QueueUnderflow("Queue Underflow! No operations can be done")
        else:
            print("Space available for operations")

    def enqueue(self, val):
        if self.front == self.limit:
            raise QueueOverflow("Queue Overflow! No operations can be done")
        else:
            self.queue.insert(0, val)
            print(f"Enqueue : {self.queue}")

    def dequeue(self):
        if self.front == self.rear:
            raise QueueUnderflow("Queue Underflow! No operations can be done")
        else:
            print(f"Element to be popped out is: {self.queue[self.front]}")
            self.queue.pop(self.length - 1)
            print(f"Dequeue : {self.queue}")


if __name__ == '__main__':
    run_again = "y"
    while run_again == "y":
        length_array = int(input("Length of queue: "))
        limit_array = int(input("Limit of queue: "))
        if length_array >= limit_array:
            raise QueueOverflow("Limit must be grater than length of the array! Re-run the program")
        operation = input("which operation to do: (f)if_full, (m)is_empty, (e)enqueue, (d)dequeue: ")
        q = Queue()
        print(f"Queue to be operated on: {q.queue}")
        if operation == 'f':
            q.is_full()
        elif operation == 'm':
            q.is_empty()
        elif operation == 'e':
            value = int(input("Enter the value to enqueue: "))
            q.enqueue(value)
        elif operation == 'd':
            q.dequeue()
        run_again = input("Want to run program again - Yes(y) or (n)No")
        if run_again == "n":
            sys.exit("Exit operation commanded")
