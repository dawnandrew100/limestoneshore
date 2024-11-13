from random import randint, choice
from string import ascii_lowercase
from timeit import timeit
import limestone as ls

"""
This module displays the run time for the distance metric of each algorithm that has a distance metric
The purpose of this project is not speed but added functionality so this module is only for reference
This module is intended to be run from the command line as follows -> python benchmarks.py
"""

test_strings1 = ["".join(choice(ascii_lowercase) for _ in range(randint(50,100))) for _ in range(100)]
test_strings2 = ["".join(choice(ascii_lowercase) for _ in range(randint(50,100))) for _ in range(100)]

def test_NW():
    [ls.needleman_wunsch.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_SW():
    [ls.smith_waterman.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_WSB():
    [ls.waterman_smith_beyer.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_WF():
    [ls.wagner_fischer.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_LW():
    [ls.lowrance_wagner.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_H():
    [ls.hamming.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_J():
    [ls.jaro.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_JW():
    [ls.jaro_winkler.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_LCS():
    [ls.longest_common_subsequence.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def test_SCS():
    [ls.shortest_common_supersequence.distance(a, b) for a, b in zip(test_strings1, test_strings2)]

def main():
    print("Each of the following tests creates a list comprehension of 100 sequences that are 50 to 100 charachters each")
    print(f"Needleman Wunsch test: Time = {timeit('test_NW()', globals = globals(), number=1):0.4f}")
    print(f"Smith Waterman test: Time = {timeit('test_SW()', globals = globals(), number=1):0.4f}")
    print(f"Waterman Smith Beyer test: Time = {timeit('test_WSB()', globals = globals(), number=1):0.4f}")
    print(f"Wagner Fischer test: Time = {timeit('test_WF()', globals = globals(), number=1):0.4f}")
    print(f"Lowrace Wagner test: Time = {timeit('test_LW()', globals = globals(), number=1):0.4f}")
    print(f"Hamming test: Time = {timeit('test_H()', globals = globals(), number=1):0.4f}")
    print(f"Jaro test: Time = {timeit('test_J()', globals = globals(), number=1):0.4f}")
    print(f"Jaro Winkler test: Time = {timeit('test_JW()', globals = globals(), number=1):0.4f}")
    print(f"Longest Common Subsequence test: Time = {timeit('test_LCS()', globals = globals(), number=1):0.4f}")
    print(f"Shortest Common Supersequence test: Time = {timeit('test_SCS()', globals = globals(), number=1):0.4f}")

if __name__ == "__main__":
    main()