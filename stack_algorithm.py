import sys
from list_creation import unordered_array


class StackLimitError(Exception):
    pass


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


class Stack:
    def __init__(self):
        self.stack = unordered_array(len_stack)
        self.limit = limit
        self.length = len(self.stack)
        self.top = self.length

    def push(self, value):
        if self.top == self.limit:
            raise StackOverflow("No space is available for operations")
        else:
            self.top = +1
            self.stack.append(int(value))
            print(self.stack)

    def pop(self):
        if self.top == -1:
            raise StackUnderflow("Empty stack")
        else:
            self.stack.remove(self.stack[self.length - 1])
            print(self.stack)
            self.top = - 1

    def peek(self):
        if self.top == -1:
            raise StackUnderflow("Empty stack")
        else:
            print(f"Element at the top is: {self.stack[self.length - 1]}")


if __name__ == "__main__":
    len_stack = int(input("Enter the length of stack to do operations on: "))
    limit = int(input("Enter the limit of the stack: "))
    if len_stack >= limit:
        raise StackLimitError("Limit must be greater than the length")
    stack = Stack()
    print(f"Stack to work on: {stack.stack}")
    run_again = "y"
    while run_again == "y":
        operation = int(input("(1)Push\n"
                              "(2)Pop\n"
                              "(3)Peek\n"
                              "Enter the number in bracket: "))
        if operation == 1:
            v = int(input("Enter the value to append: "))
            stack.push(v)
        elif operation == 2:
            stack.pop()
        elif operation == 3:
            stack.peek()
        run_again = input("Want to run program again - (y)Yes or (n)No: ")
    if run_again == "n":
        sys.exit("Exit operation commanded")
