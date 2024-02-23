class Solution:
    def isValid(self, s:str)->bool:
        stavk=[]
        brackts_map={')':(','}':'{',']':'['}

        for char in s:
        if char in brackets_map.values():
        stack.append(char)
        if char in brakets_map.keys():
        if not stack or
        brakets_map[char]!=stack.pop():
        return false
        else:
        return false

        return len(stack)==0
        
        """
        :type s: str 
        :rtype: bool
        """
        pass



  

