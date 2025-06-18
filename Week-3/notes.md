## **Bubble Sort (O(n²))**

Bubble sort compares **adjacent values** in the array and repeatedly **swaps** them if they are in the **wrong order**. With each full pass through the array, the **largest unsorted value "bubbles" to the end**. The process is repeated until the array is sorted.

### 🔢 Steps:

1. Start from the beginning of the array.
2. Compare the current element with the next one.
3. If they are out of order, **swap** them.
4. Continue this till the end of the array (last item gets sorted).
5. Repeat the process, reducing the range each time (since the last elements are already sorted).

---

## **Selection Sort (O(n²))**

Selection sort finds the **smallest item** from the unsorted portion of the array and **places it at the correct position** in the sorted portion. This is done by **repeatedly selecting** the minimum element from the unsorted part.

### 🔢 Steps:

1. Start from the first index.
2. Look through the remaining unsorted part to find the **smallest element**.
3. Swap it with the current index.
4. Move to the next index and repeat.
5. Continue until the array is sorted.

---

## **Insertion Sort (O(n²))**

Insertion sort divides the array into a **sorted** and an **unsorted** section. It takes one element at a time from the unsorted part and **inserts it into its correct position** in the sorted part. It works like how people sort playing cards in their hands.

### 🔢 Steps:

1. Start from the second element (first element is considered sorted).
2. Compare it with the elements in the sorted part (left side).
3. Shift all larger sorted elements one position to the right.
4. Insert the current element into its correct spot.
5. Repeat for all elements.

---

## **Merge Sort (O(n log n))**

Merge sort uses the **divide and conquer** approach. It **divides** the array into two halves, sorts each half, and then **merges** the two sorted halves into one sorted array. The key idea is that **merging two sorted arrays is easy and efficient**.

### 🔢 Steps:

1. If the array has more than one element:
2. Divide it into two halves.
3. Recursively apply merge sort on each half.
4. Merge the two sorted halves into a single sorted array.
5. Return the merged array.

---

## **Quick Sort (O(n log n) on average)**

Quick sort is another **divide and conquer** algorithm. It picks a **pivot** element and partitions the array so that:

* All elements **smaller than the pivot** go to the left,
* All elements **larger than the pivot** go to the right.

Then it recursively applies the same process to both sides. For small partitions, **insertion sort** may be used to optimize performance.

### 🔢 Steps:

1. Pick a pivot (can be first, last, middle, or random element).
2. Partition the array into two parts:

   * Elements less than pivot.
   * Elements greater than pivot.
3. Recursively apply quick sort to both sides.
4. Combine the sorted parts with the pivot in between.
