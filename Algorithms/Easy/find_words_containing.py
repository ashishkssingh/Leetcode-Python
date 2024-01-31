"""
2942. Find Words Containing Character

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

 

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
"""


class FindWordsContaining(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        index_list = []
        for index, word in enumerate(words):
            if x in word:
                index_list.append(index)
        return index_list

    def findWordsContaining2(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        return [i for i, w in enumerate(words) if x in w]


if __name__ == "__main__":
    words1, x1 = ["leet", "code"], "e"
    words2, x2 = ["abc", "bcd", "aaaa", "cbc"], "a"
    words3, x3 = ["abc", "bcd", "aaaa", "cbc"], "z"

    print(FindWordsContaining().findWordsContaining(words=words1, x=x1))
    print(FindWordsContaining().findWordsContaining(words=words2, x=x2))
    print(FindWordsContaining().findWordsContaining(words=words2, x=x3))
