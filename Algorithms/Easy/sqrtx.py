"""
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""


class MySqrt:
    # Binary Search
    def mySqrt1(self, x: int) -> int:
        i = 1
        j = x/2

        while i <= j:
            mid = int(i + (j-i)/2)

            if (mid*mid == x):
                return mid
            elif (mid * mid > x):
                j = mid - 1
            else:
                i = mid + 1

        return i-1

    # Linear Search
    def mySqrt2(self, x: int) -> int:
        r = x
        while r*r > x:
            r = int(r+x/r)//2
        return r


if __name__ == "__main__":
    print(MySqrt().mySqrt1(9))
    print(MySqrt().mySqrt1(9))
