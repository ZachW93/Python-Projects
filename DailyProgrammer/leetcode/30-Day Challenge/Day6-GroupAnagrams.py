# -*- coding: utf-8 -*-
"""
Problem: Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        outputList = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in wordDict: wordDict[sortedWord].append(word)
            else: wordDict[sortedWord] = [word]
        for key in wordDict: outputList.append(wordDict[key])
        return outputList

                    
                    