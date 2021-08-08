"""
66. Plus One

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""

from typing import List


class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for v in digits:
            number = 10*number + v
        number += 1

        return [int(x) for x in str(number)]


if __name__ == '__main__':
    print(PlusOne().plusOne([1, 2, 3]))
