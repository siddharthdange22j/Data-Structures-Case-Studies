# E-Commerce Product Sorting
# Divide and Conquer using Merge Sort

products = [
    ("Laptop", 60000),
    ("Mobile", 25000),
    ("Headphones", 3000),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(products):
    if len(products) <= 1:
        return products

    mid = len(products) // 2

    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    return merge(left, right)


print("===== E-COMMERCE PRODUCT SORTING =====")

print("\nProducts Before Sorting:")
for name, price in products:
    print(f"{name:<15} ₹{price}")

sorted_products = merge_sort(products)

print("\nProducts After Sorting by Price:")
for name, price in sorted_products:
    print(f"{name:<15} ₹{price}")
