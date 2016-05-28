#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Finding Distinct Elements with a Sublinar Algorithm
O(N) in time and O(log N) in space.

For any integer c > 2, Pr[1/c <= F*/F <= c] >= 1-2/c
where F* is the output of the Aproximate Algorithm
and F is the amount of unique elements.
"""

import random

class AproximateCounter(object):
    """Sublinear Algorithm to Count Distinc Elements
    """
    def __init__(self):
        """Constructor.
        """
        self.modulus = 17 # Just a random int.

    def _hash(self, number):
        """Evaluate the hash function over number
        Args:
            number (int): Element to be evaluated.
        """
        return (3*number + 1) % self.modulus

    def _to_binary(self, number):
        """Recursive function to get the binary representation of a number.
        Args:
            number (int): Number to be decomposed.
        """
        if number == 0:
            return [0]
        elif number == 1:
            return [1]
        else:
            temp = self._to_binary(number//2)
            temp.extend([number%2])
            return temp

    def _trailing_zeros(self, number):
        binary_repr = self._to_binary(number)
        counter = 0
        while binary_repr != [] and binary_repr[-1] == 0:
            counter += 1
            binary_repr = binary_repr[:-1]
        return counter

    def count(self, elements):
        """Returns the aproximate amount of unique elements.
        Args:
            elements (list of int): List over which we count.

        Returns:
            An aproximation of the unique elements of elements.
        """
        self.modulus = len(elements)
        max_trailing = 0
        for element in elements:
            hashed_element = self._hash(element)
            trailing = self._trailing_zeros(hashed_element)
            if max_trailing < trailing:
                max_trailing = trailing
        return 2**max_trailing

def random_test(max_value=10000, list_size=1000, seed=None):
    """Run a pseudo-random test.

    Args:
        max_value (int): Generate int in [0, max_value].
        list_size (int): Generate list_size integers.
        seed (int, str): Param for random.seed().

    Returns:
         A 2-tuple of int with the count of unique elements
         and the aproximation of the algorithm.

    Notes:
        Try with differents combinations of max_value and list_size.
        max_value = 100 and list_size = 1000
    """
    # Set seed
    random.seed(seed)

    # Generate a pseudo-random list of elements
    tests = [int(random.uniform(0, max_value))
             for item in range(list_size)]

    # Count unique elements (deterministic)
    present = [False for item in range(max_value)]
    for item in tests:
        present[item] = True
    det_unique_counter = present.count(True)

    # Count unique elements (aprox)
    counter = AproximateCounter()
    aprox_unique_counter = counter.count(tests)

    # Report
    return (det_unique_counter, aprox_unique_counter)

def main():
    """Tests
    """
    counter = AproximateCounter()
    tests = list(range(9))
    print('Testing: Private functions...')
    for test in tests:
        print('{} > {} ({})'.format(
            test,
            counter._to_binary(test),
            counter._trailing_zeros(test)))
    test = [4, 7, 1, 4, 7, 1, 4, 7]
    print('Unique in {}: {}'.format(
        test,
        counter.count(test)))

    for test in range(5):
        print('Random test #{}: {rtst[0]} vs. {rtst[1]}'.format(
            test+1, rtst=random_test()))

if __name__ == '__main__':
    main()
