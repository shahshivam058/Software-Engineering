What is Sorting?
At its core, sorting is the process of arranging elements of a list (or an array, file, etc.) into a specific order. This order can be numerical, alphabetical, chronological, or based on any custom criterion.

Why is sorting important?

Sorting is a fundamental operation in computer science with widespread applications:
Searching: Much faster to find an element in a sorted list (e.g., Binary Search).
Data Analysis: Easier to identify patterns, minimum/maximum values, or perform statistical analysis on sorted data.
Database Operations: Indexing and querying often rely on sorted data.
User Experience: Presenting data in a logical order (e.g., search results by relevance, file explorer by name).

Key Concepts and Terminology
Before we explore specific algorithms, let's understand some important terms:

In-place vs. Out-of-place:
In-place (or In-situ): An algorithm that sorts the elements directly within the original data structure, requiring only a constant amount of extra auxiliary space (O(1)) beyond the input itself. Examples: Bubble Sort, Insertion Sort, Selection Sort, Heap Sort.

Out-of-place: An algorithm that requires additional memory space proportional to the input size (O(n) or O(logn)) to perform the sort. It typically creates a temporary copy of the data. Examples: Merge Sort.

Stable vs. Unstable:

Stable: A sorting algorithm is stable if it preserves the relative order of equal elements. If two elements have the same value, and one appeared before the other in the original unsorted list, it will still appear before the other in the sorted list. This is crucial when elements have associated data that needs to maintain its original grouping.

Example: Sorting a list of students by their grade, and if two students have the same grade, their original relative order is maintained.

Examples: Bubble Sort, Insertion Sort, Merge Sort, Counting Sort.

Unstable: An algorithm that does not guarantee to preserve the relative order of equal elements.

Examples: Selection Sort, Quick Sort, Heap Sort.

Comparison Sort vs. Non-Comparison Sort:

Comparison Sort: These algorithms sort by comparing elements to each other. They rely on comparison operators (e.g., >,<,==).

The theoretical lower bound for comparison sorts is O(nlogn) time complexity.

Examples: Bubble Sort, Quick Sort, Merge Sort, Heap Sort.

Non-Comparison Sort: These algorithms do not rely on comparisons. They typically work by making assumptions about the nature of the input data (e.g., range of values). They can achieve better than O(nlogn) time complexity in specific scenarios.

Examples: Counting Sort, Radix Sort, Bucket Sort.

Time Complexity: Measures how the running time of an algorithm grows with the input size (n).

Best Case: The minimum time an algorithm takes for a specific input (e.g., already sorted array).

Average Case: The time an algorithm takes on a typical random input.

Worst Case: The maximum time an algorithm takes for a specific input (e.g., reversely sorted array for some algorithms).

Common notations: O(n ** 2), O(nlogn), O(n), etc.

Space Complexity: Measures how much auxiliary memory an algorithm uses relative to the input size.

O(1) (constant space), O(logn), O(n).

