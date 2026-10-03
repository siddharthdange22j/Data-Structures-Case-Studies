# 🛒 E-Commerce Product Sorting using Divide and Conquer

## 1. Introduction

E-commerce platforms contain a large number of products. Users commonly need to sort products according to their price.

This case study demonstrates **Merge Sort**, which uses the **Divide and Conquer** strategy to efficiently sort e-commerce products based on price.

## 2. Problem Statement

Develop a product sorting system that sorts e-commerce products according to their price using the Divide and Conquer strategy.

### Example

| Product | Price |
|---|---:|
| Laptop | ₹60,000 |
| Mobile | ₹25,000 |
| Headphones | ₹3,000 |
| Keyboard | ₹1,500 |
| Monitor | ₹12,000 |

After sorting:

| Product | Price |
|---|---:|
| Keyboard | ₹1,500 |
| Headphones | ₹3,000 |
| Monitor | ₹12,000 |
| Mobile | ₹25,000 |
| Laptop | ₹60,000 |

## 3. Algorithm Used

**Merge Sort**

Merge Sort follows three main steps:

1. Divide
2. Conquer
3. Combine

## 4. Algorithm

```text
MERGE_SORT(array, low, high)

if low < high:
    mid = (low + high) / 2
    MERGE_SORT(array, low, mid)
    MERGE_SORT(array, mid + 1, high)
    MERGE(array, low, mid, high)
```

## 5. Working

Example:

```text
60000  25000  3000  1500  12000
```

The list is divided into smaller sublists until individual elements are obtained. The elements are then merged in sorted order.

Final result:

```text
1500  3000  12000  25000  60000
```

## 6. Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

**Space Complexity:** O(n)

## 7. Real-World Applications

- E-commerce product sorting
- Price-based filtering
- Rating-based sorting
- Customer records
- Transaction records
- Large database sorting

## 8. Advantages

- Efficient for large datasets.
- Guaranteed O(n log n) running time.
- Stable sorting algorithm.
- Suitable for large product databases.

## 9. Conclusion

Merge Sort provides an efficient way to sort a large collection of e-commerce products. By dividing the problem into smaller subproblems and combining their sorted results, the Divide and Conquer strategy makes the sorting process efficient and systematic.

## Run the Program

```bash
python merge_sort.py
```
