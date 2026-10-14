# Case Study 1: E-Commerce Product Sorting using Merge Sort

def merge_sort(products):
    if len(products) <= 1:
        return products

    middle = len(products) // 2
    left = merge_sort(products[:middle])
    right = merge_sort(products[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    products = [
        {"name": "Wireless Mouse", "price": 599},
        {"name": "Keyboard", "price": 899},
        {"name": "USB Drive", "price": 399},
        {"name": "Headphones", "price": 1299},
        {"name": "Laptop Stand", "price": 749},
    ]

    print("E-COMMERCE PRODUCT SORTING")
    print("Products before sorting:")
    for product in products:
        print(f'{product["name"]}: Rs. {product["price"]}')

    sorted_products = merge_sort(products)
    print("\nProducts sorted by price (low to high):")
    for product in sorted_products:
        print(f'{product["name"]}: Rs. {product["price"]}')
