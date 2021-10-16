class Solution:
    def firstAlphabet(self, S):
        s = S.split(' ')
        for i in s:
            if i == ' ':
                s.pop(i)
                print(s)
##        c = ''
##        for i in range(len(s)):
##            c +=s[i][0]
##        print(c)
