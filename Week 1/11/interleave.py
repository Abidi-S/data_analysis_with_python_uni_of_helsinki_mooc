#!/usr/bin/env python3

def interleave(*lists):
    combi_list = list(zip(*lists))
    unpacked_list = []
    for i in combi_list:
        unpacked_list.extend(i)
    return unpacked_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
