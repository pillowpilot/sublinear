#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Finding Distinct Elements with a Sublinar Algorithm
O(N) in time and O(log N) in space.
"""

class ProbabilisticCounter(object):
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

def main():
    """Tests
    """
    counter = ProbabilisticCounter()
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

if __name__ == '__main__':
    main()
