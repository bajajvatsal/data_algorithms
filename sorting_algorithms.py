import sys
from list_creation import unordered_array


class Sorting:

    def __init__(self, array_length):
        self.array = unordered_array(array_length)

        self.length = len(self.array)

    def bubble_sort(self):
        print(f"{self.array} is unordered array")
        for i in range(self.length - 1):
            for j in range(self.length - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        print(f"{self.array} is ordered array")

    def insertion_sort(self):
        print(f"{self.array} is unordered array")
        for i in range(1, self.length):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j = j - 1
            self.array[j + 1] = key
        print(f"{self.array} is ordered array")

    def selection_sort(self):
        print(f"{self.array} is unordered array")
        for i in range(self.length):
            minimum = i
            for j in range(i + 1, self.length):
                if self.array[j] < self.array[minimum]:
                    minimum = j
            if self.array[i] > self.array[minimum]:
                self.array[i], self.array[minimum] = self.array[minimum], self.array[i]
        print(f"{self.array} is ordered array")


if __name__ == '__main__':
    run_again = "y"
    while run_again == "y":
        len_array = int(input("No of elements to work upon: "))
        s = Sorting(len_array)
        sort_method = input('''Enter the method for sorting: (b)Bubble sort, (i)Insertion sort, (s)Selection sort''')
        if sort_method == "b":
            s.bubble_sort()
        elif sort_method == "i":
            s.insertion_sort()
        elif sort_method == "s":
            s.selection_sort()
        run_again = input("Want to run the program again- (y)Yes or (n)No")
        if run_again == "n":
            sys.exit("Exit operation commanded")
