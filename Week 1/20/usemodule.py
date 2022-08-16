#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    a = 3
    b = 4
    c = 5
    triangle.hypothenuse(a, b)
    triangle.area(a, b)

if __name__ == "__main__":
    main()
