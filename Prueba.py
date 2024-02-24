class Solution:

    # aab

    # hash = ab
    # final = 1, 2
    # cont = 2
    #

    def lengthOfLongestSubstring(self, s: str):
        hash = {}
        cont = 0
        final = []
        for i, j in enumerate(s):
            if j in hash.values():
                hash.clear()
                hash[i] = j
                final.append(cont)
                cont = 1
            else:
                hash[i] = j
                cont += 1
        final.append(cont)
        print(max(final))


prueba = Solution()
s = "abcabcbb"
prueba.lengthOfLongestSubstring(s)
