class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words) - 1):
          word = words[i]
          next_word = words[i + 1]

          for j in range(len(word)):
            if j >= len(next_word):
              return False
            if order.index(word[j]) < order.index(next_word[j]):
              break
            elif order.index(word[j]) > order.index(next_word[j]):
              return False
        return True
