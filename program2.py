class Solution(object):
    def romanToInt(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
       if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
            result -= roman_values[s[i]]
       else:
            result += roman_values[s[i]]
     return result
print(romanToInt("III"))      
print(romanToInt("LVIII"))    
print(romanToInt("MCMXCIV"))  
      """
        :type s: str
        :rtype: int
        """
        pass
