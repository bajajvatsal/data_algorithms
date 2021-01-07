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

    def partition(self, arr, low, high):
        i = low-1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i+1

    def quick_sort(self, arr, low, high):
        if low < high:
            partition_temp = self.partition(arr, low, high)
            self.quick_sort(arr, low, partition_temp - 1)
            self.quick_sort(arr, partition_temp+1, high)
        return self.array

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return self.array


if __name__ == '__main__':
    run_again = "y"
    while run_again == "y":
        len_array = int(input("No of elements to work upon: "))
        s = Sorting(len_array)
        temp_list = unordered_array(len_array)
        sort_method = input(
            '''Enter the method for sorting: (b)Bubble sort, (i)Insertion sort, (s)Selection sort''')
        if sort_method == "b":
            s.bubble_sort()
        elif sort_method == "i":
            s.insertion_sort()
        elif sort_method == "s":
            s.selection_sort()
        elif sort_method == "q":
            print(s.quick_sort(s.array, 0, len(s.array)-1))
        elif sort_method == "m":
            sorted_list = s.mergeSort(s.array)
            print(sorted_list)
        run_again = input("Want to run the program again- (y)Yes or (n)No")
        if run_again == "n":
            sys.exit("Exit operation commanded")
