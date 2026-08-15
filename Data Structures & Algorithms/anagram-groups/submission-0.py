from collections import defaultdict # defaultdict from collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= defaultdict(list) # My dictionary of lists
        for word in strs:
            count=[0]*26 #create a 26 length array for each letter/charater
            for character in word:
                count[ord(character)-ord('a')] +=1 #convert letter to index
            groups[tuple(count)].append(word) #convert count to tuple and use it as a dict
        return list (groups.values())