"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""


class NumJewelsInStones(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count_of_jewels = 0
        for char in jewels:
            count_of_jewels += stones.count(char)
        return count_of_jewels

    def numJewelsInStones2(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count_of_jewels = 0
        for stone in stones:
            if stone in jewels:
                count_of_jewels += 1
        return count_of_jewels


if __name__ == "__main__":
    jewels1, stones1 = "aA", "aAAbbbb"
    jewels2, stones2 = "z", "ZZ"
    print(NumJewelsInStones().numJewelsInStones(jewels=jewels1, stones=stones1))
    print(NumJewelsInStones().numJewelsInStones(jewels=jewels2, stones=stones2))
