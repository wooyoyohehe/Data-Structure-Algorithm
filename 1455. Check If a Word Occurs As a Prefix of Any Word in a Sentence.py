class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(" ")
        for i in range(len(words)):
            if words[i][:len(searchWord)] == searchWord:
                return i+1
        return -1
        