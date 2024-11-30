class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_counter = 0
        text = list(s)
        substring = ""
        longest_substring_length = 0
        outer_string_counter = 0
        for letter in text:
            string_counter = outer_string_counter
            #print(letter)
            while string_counter <= len(text)-1:
                #print(string_counter, substring, substring_counter)
                if s[string_counter] not in substring:
                    substring += s[string_counter]
                    substring_counter += 1
                    if substring_counter > longest_substring_length:
                        longest_substring_length =  substring_counter  
                    string_counter += 1
                else:
                    #print("Character is repeating")
                    substring_counter = 0
                    substring = ""
                    string_counter = len(text) + 1
                    #print(string_counter, substring, substring_counter)
            outer_string_counter += 1
        return longest_substring_length
