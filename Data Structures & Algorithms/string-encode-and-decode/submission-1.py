class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=[]
        for x in strs:
            encoded_string.append (f"{len(x)}#{x}")
        return "".join(encoded_string)
        

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i=0
        while i<len(s):
            j=i
            while s[j] != '#':
               j +=1
            length = int(s[i:j])
            decoded_list.append(s[j+1 : j+1+length])
            i = j+1+length
        return decoded_list

        
