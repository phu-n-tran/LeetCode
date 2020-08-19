# --------------------------------------------------------------------------
# Name:        Goat Latin
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    A sentence S is given, composed of words separated by spaces. 
    Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin"
    (a made-up language similar to Pig Latin.)

    The rules of Goat Latin are as follows:
      1. If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
         For example, the word 'apple' becomes 'applema'.

      2. If a word begins with a consonant (i.e. not a vowel), remove the
         first letter and append it to the end, then add "ma".
         For example, the word "goat" becomes "oatgma".

      3. Add one letter 'a' to the end of each word per its word index in
         the sentence, starting with 1. For example, the first word gets "a" 
         added to the end, the second word gets "aa" added to the end and so on.
         Return the final sentence representing the conversion from S to Goat Latin. 

    Example 1:
      Input: "I speak Goat Latin"
      Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    
    Example 2:
      Input: "The quick brown fox jumped over the lazy dog"
      Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


    Notes:
      1. S contains only uppercase, lowercase and spaces. Exactly one space between each word.
      2. 1 <= S.length <= 150.
"""


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        newGL = ""
        vowelsTup = ("a", "e", "i", "o", "u")
        addA = "a"
        MA = "ma"
        
        for letter in S.split(" "):
            if newGL != "":
                newGL += " "
                
            if letter[0].lower() in vowelsTup:
                newGL += letter + MA + addA
            else:
                newGL += letter[1:] + letter[0] + MA + addA
            
            
            addA += "a"
        
        return newGL
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return ' '.join((w[not v:]+w[:not v]+'ma'+('a'*i) for ((w,v),i) in zip(map((lambda s: (s,s[0].lower() in ['a','e','i','o','u'])),S.split(' ')),itertools.count(1))))
##################################################
def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        def proc(i,w):
            ans = ''
            if w[0] not in 'aeiouAEIOU':
                ans = w[1:]+w[0]+'ma' + 'a'*i
            else:
                ans = w+'ma'+ 'a'*i
            return ans
            
        
        return  ' '.join([proc(i,w) for i,w in enumerate(S.split(' '),1)])
##################################################
def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel=set(['a','e','i','o','u','A','E','I','O','U'])
        arr=S.split(' ')
        space=' '
        count=1
        for i in range(len(arr)):
            if arr[i][0] in vowel:
                arr[i]=arr[i]+'ma'
            else:
                temp=arr[i][0]
                arr[i]=arr[i][1:]
                arr[i]=arr[i]+temp+'ma'
            
            arr[i]=arr[i]+'a'*count
            count+=1
        return space.join(arr)
##################################################
def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(' ')
        new_words = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (i + 1)
            new_words.append(word)
        return ' '.join(new_words)
'''
