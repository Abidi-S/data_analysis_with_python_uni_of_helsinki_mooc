#!/usr/bin/env python3

def main():
    dices = [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    for dice in dices:
        print(dice)

if __name__ == "__main__":
    main()
