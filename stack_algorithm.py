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
        self.top = -1

    def push(self, value):
        if self.top == self.limit:
            raise StackOverflow("")
        else:
            self.stack.append(value)
            self.fullstackview()

    def fullstackview(self):
        print("Stack View")
        # print(self.stack)
        for e in reversed(self.stack):
            print(" ---")
            print(f"| {e} |")
        print(" ---")

    def pop(self):
        if len(self.stack) == 0:
            raise StackUnderflow
        else:
            print(f"Element Removed: {self.stack[self.top-1]}")
            self.stack.remove(self.stack[self.top-1])
            self.top -= 1
            self.fullstackview()

    def peek(self):
        if len(self.stack) == 0:
            raise StackUnderflow
        else:
            print(f"Element at the top is: {self.stack[self.length - 1]}")


if __name__ == "__main__":
    limit = int(input("Enter the limit of the stack: "))
    
    # print(f"Stack to work on: {stack.stack}")
    input_array = input("Do you want to operate on the computer generated arary y or n : ")
    if input_array=="y":
        len_stack = int(input("Enter the length of stack to do operations on: "))
    if input_array == "n":
        len_stack = int(input("Enter the length of stack to do operations on: "))
        if len_stack >= limit:
            raise StackLimitError("Limit must be greater than the length")
        stack = Stack()
        stack.stack.clear()
        for i in range(len_stack):
            integer_int = int(input("Enter the element of index " + str(i + 1) + ": "))
            stack.stack.append(integer_int)
    stack=Stack()
    run_again = "y"
    while run_again == "y":
        operation = int(input("(1)Push\n"
                              "(2)Pop\n"
                              "(3)Peek\n"
                              "(4)FullStack View\n"
                              "Enter the number in bracket: "))
        if operation == 1:
            v = int(input("Enter the value to append: "))
            stack.push(v)
        elif operation == 2:
            stack.pop()
        elif operation == 3:
            stack.peek()
        elif operation == 4:
            stack.fullstackview()
        run_again = input("Want to run the program again - (y)Yes or (n)No: ")
        if run_again == "n":
            sys.exit("Exit operation commanded")  