from collections import defaultdict # defaultdict from collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) #create default dic 
        for word in strs:
            key = "".join(sorted(word)) #sort the word theb create a key from it 
            groups[key].append(word) #
        return list(groups.values())