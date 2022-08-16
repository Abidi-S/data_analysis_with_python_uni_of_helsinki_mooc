#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    s = " + ".join([str(ch) for ch in L])
    summed = f" = {sum(L)}"
    return s + summed

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
