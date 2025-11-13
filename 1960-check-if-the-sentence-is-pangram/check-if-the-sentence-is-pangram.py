class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        return alphabet.issubset(sentence)