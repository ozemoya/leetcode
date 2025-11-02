class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        sentence_set = set(sentence)
        return alphabet.issubset(sentence_set)