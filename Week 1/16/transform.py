#!/usr/bin/env python3

def transform(s1, s2):
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))
    products = []
    for l1_item, l2_item in zip(l1, l2):
        products.append(l1_item * l2_item)
    return products

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
