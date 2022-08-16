#!/usr/bin/env python3

def reverse_dictionary(d):
    fin_to_eng = {}
    for key, value in d.items():
        for i in value:
            if i not in fin_to_eng:
                fin_to_eng[i] = []
            fin_to_eng[i].append(key)
    return fin_to_eng

def main():
    eng_to_fin = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(eng_to_fin))

if __name__ == "__main__":
    main()
