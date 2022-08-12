#!/usr/bin/env python3
def triple(n):
    return n * 3

def square(n):
    return n**2

def main():
    for i in range(1, 11):
        triple_i = triple(i)
        square_i = square(i)
        if square_i > triple_i:
            break
        print(f"triple({i})=={triple_i}", end = " ")
        print(f"square({i})=={square_i}")


if __name__ == "__main__":
    main()
