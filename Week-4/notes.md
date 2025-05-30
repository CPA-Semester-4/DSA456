# Searching and Sorting

## Searching

In general there are two ways to search
    - Given a collection and some key, find the item with the same key within your collection

In a list there are two ways to "search"

1) Linear Search
    - start at the beginning of list
    - look at each item to see if it matches. If it does, the item is found
    - if we get to end of list and we don't find the item, the item does not exist
    - O(n)

2) Binary Search
    - Requires 2 things
        - the data must be sorted within the list
        - random access is also required, this means you can get to the i-th item in constant time
    - O(logn)

Given an array of size 1 million where the data is evenly distributed and key has equal probability to be in any spot within the array on average it will cost n/2 checks

Linear Search will on average cost n/2
Binary Search will on average cost logn checks

## Sorting

# Simple Sorts:

* Bubble sort
* Selection sort
* Insertion sort

All of the above have run times of O(n^2) ... but fastest wall clock algorithm is insertion sort.

