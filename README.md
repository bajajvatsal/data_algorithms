# Python Data Structures and Algorithms

This repository contains different data structures and algorithms using classes.

## Table of Contents

1. [Array](##Array)
2. [Linked List](##Linked-List)
   - Singly Linked List
   - Doubly Linked List
3. [Queue](##Queue)
4. [Sorting](##Sorting)
   - [Bubble Sort](##Bubble-Sort)
   - [Insertion Sort](##Insertion-Sort)
   - [Merge Sort](##Merge-Sort)
   - [Quick Sort](##Quick-Sort)
   - [Selection Sort](##Selection-Sort)
5. [Stack](/stack_algorithm.py)

## Array

An array is a collection of elements(usually same data type elements), by definition, every element is identified by an index. And this index gives the position of the element in the array starting from 0.  
In this file, a dynamic list(fixed size) can be created and operations like insertion/deletion can be performed at any index or after a given value.

## Linked List

A linked list is a linear collection of elements, identified by pointers (previous or next element or both). By definition, they are the representation of different node sequence altogether. Every node consists of elements and reference links to the next node in the list(apart from the tail and in the circular list).

The first element is called the head and the last element is called the tail, with an exception where the circular linked list is in the discussion.

- In the case of the singly linked list the node/elements are represented by the next element with the symbol →
- In the case of the doubly linked list the node/elements are represented by both the previous and next element with the symbol ↔

The operations that a linked list can perform are insertion and deletion at a given index or after a given value. Also traversing can be done

## Queue

Queues are very similar to stacks but they are open on both sides.  
Queue data structure follows FIFO(first in first out) methodology. But unlike the linked list they don't have any specific characteristics.  
The two main operations which are performed in queues are Enqueue and Dequeue.

- **Enqueue** :- Adding an element to the queue. Enqueue operation can only be done on the rear element
- **Dequeue** :- Removing an element from the queue. Dequeue operation can only be done on the front element  
  Both operations can be only performed at different ends.

## Sorting

Sorting means arranging things in sequence or order according to specific criteria. Sorting data strucutres is a very important, because when projects and products are on big scale you need to sort things accoring to their name, data-type, and various diffrent parameter. To do that efficient and complex sorting techniques are required.

### Bubble Sort

Bubble sort is a simple sorting algorithm that compares two different elements in two nested recursive for loop till all elements in the list are sorted out.

### Insertion Sort

Insertion sort is a sorting algorithm that involves assigning an element sequentially from the start. The algorithm will work on that element until that element is placed in the right position and then eventually array will be divided into a sorted part and an unsorted part. And this algorithm will sort out the array

### Merge Sort

Merge Sort algorithm is a divide and conquer algorithm which divides the array into two subarrays and this process goes on until all elements become a single value element array. Then according to the values algorithm sort them all and merge them into one. And this goes the same for all the sub-arrays until all the elements are sorted out.

### Quick Sort

Quicksort algorithm is also divide and conquer algorithm. This sorting technique involves selecting a pivot element and partitioning the array at the end of that pivot element. At this rate, all the elements are divided into a single element array, and then this algorithm sort the elements by comparing them and putting them in right place.

### Selection Sort

Selection sort algorithm selects the minimum value element and swaps it with the element in the front place. As same as insertion sort, this array will also be divided into two parts sorted one and unsorted one.  
It happens with all elements until all the elements in the list are sorted.

## Stack

Stacks are very silmilar to stacks, though they works on the methodology of LIFO(last in first out). They don't have any other specific charteristics but diffrent data structure are used according to their feautres and limitaions.
The operations that can be performed on the stacks are:

1. Push: Adding element to the top of stack.
2. Pop: Removing element at the top of stack.
3. Peek: Accessing the element at the top of stack.

## License :-

[MIT LICENSE](/LICENSE)
