__author__ = 'youzipi'


# -*- coding:utf-8 -*-

class BinarySearch:
    def getPos(self, A, n, val):
        low = 0
        high = n - 1
        first_found = n
        while low <= high:
            index = int(low + high) / 2
            print A[index]
            if A[index] == val:
                first_found = min(index, first_found)
                high = index - 1
            elif A[index] > val:
                high = index - 1
            else:
                low = index + 1
        if first_found != n:
            return first_found
        else:
            return -1


a = BinarySearch()
print a.getPos([4, 4, 10, 21], 4, 4)
