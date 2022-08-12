#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(dis)

    x = (-b + sqrt_val)/(2*a)
    y = (-b - sqrt_val)/(2*a)
    return (x,y)


def main():
    print(solve_quadratic(-2,2,1))

if __name__ == "__main__":
    main()
