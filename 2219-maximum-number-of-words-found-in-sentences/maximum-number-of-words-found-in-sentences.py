class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        # 1. Corrected initialization: Python doesn't need "initalize"
        max_words = 0
        
        # 2. Corrected loop syntax: removed "each"
        for sentence in sentences: 
            
            # 3. Corrected split: We need to split on a space " "
            words_list = sentence.split(" ") 
            
            current_words_count = len(words_list)
            
            # 4. Corrected max: You must assign the result back to max_words
            max_words = max(max_words, current_words_count)
            
        return max_words