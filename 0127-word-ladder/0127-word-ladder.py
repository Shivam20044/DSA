class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        sett=set(wordList)
        if endWord not in sett:
            return 0
        # for i in wordLIst:
        #     sett.add(i)
        queue=deque()
        queue.append((beginWord,1))

        while queue:
            word,level=queue.popleft()
            if word==endWord:
                return level
            for i in range(0,len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if word[i]==c:
                        continue
                    new_word=word[:i]+c+word[i+1:]
                    if new_word in sett:
                        queue.append((new_word,level+1))
                        sett.remove(new_word)
        return 0