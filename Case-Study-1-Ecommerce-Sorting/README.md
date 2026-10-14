# Case Study 1: E-Commerce Product Sorting Using Merge Sort

## 1. Introduction
E-commerce websites display hundreds or thousands of products. Customers often want to arrange products by price so they can compare cheaper and more expensive items easily. Sorting product records is therefore an important operation in an online shopping system.

This case study demonstrates how the **Merge Sort** algorithm can arrange products in ascending order of price. Merge Sort follows the **Divide and Conquer** strategy.

## 2. Problem Statement
Given a collection of products, where each product has a name and a price, sort all products from the lowest price to the highest price without losing the relationship between each product name and its price.

## 3. Objectives
- Understand the Divide and Conquer approach.
- Implement Merge Sort in Python.
- Sort product records by price.
- Display the product list before and after sorting.
- Analyse the time and auxiliary-space complexity.

## 4. Data Structures and Algorithm Used
- **List:** Stores the product records.
- **Dictionary:** Stores each product's name and price.
- **Merge Sort:** Divides the product list into smaller parts, sorts those parts, and merges them in order.

## 5. Working Principle
1. Check whether the list contains zero or one product. If so, it is already sorted.
2. Divide the list into two halves.
3. Recursively sort the left half.
4. Recursively sort the right half.
5. Compare the first unprocessed product in each half and append the lower-priced product to the result.
6. Append any remaining products.
7. Continue until the complete list is sorted.

## 6. Example
Suppose the store has these products:

| Product | Price (Rs.) |
|---|---:|
| Wireless Mouse | 599 |
| Keyboard | 899 |
| USB Drive | 399 |
| Headphones | 1299 |
| Laptop Stand | 749 |

After sorting, the USB Drive appears first because it has the lowest price, followed by the Wireless Mouse, Laptop Stand, Keyboard, and Headphones.

## 7. Time and Space Complexity
| Case | Complexity |
|---|---|
| Best case | O(n log n) |
| Average case | O(n log n) |
| Worst case | O(n log n) |
| Auxiliary space | O(n) |

Merge Sort provides predictable O(n log n) running time, but it uses additional memory while merging.

## 8. Applications
- Sorting products by price, rating, or name.
- Organising product catalogues.
- Sorting records in data-processing systems.
- Handling large lists where predictable performance is useful.

## 9. Advantages
- Efficient for large collections.
- Stable: products with equal prices can retain their relative order.
- Uses the same divide-and-conquer idea for different data types when a comparison rule is supplied.

## 10. Limitations
- Requires extra memory for merging.
- Recursive calls add overhead for small input lists.
- This demonstration sorts an in-memory sample list and is not connected to a live shopping website.

## 11. Conclusion
This case study shows how Merge Sort can efficiently organise e-commerce products by price. It demonstrates divide and conquer, recursive processing, merging, and complexity analysis.

## 12. How to Run
Make sure Python 3 is installed. Open a terminal in this folder and run:

```bash
python merge_sort.py
```

The sample result is saved in `output.txt`.
