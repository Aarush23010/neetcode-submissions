class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        
        if cleaned=="":
            return True
        
        n = len(cleaned)
        half = n//2
        for i in range(0, half+1):
            if cleaned[i]==cleaned[n-i-1]:
                continue
            else : 
                return False
        return True
        