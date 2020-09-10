# --------------------------------------------------------------------------
# Name:        Bulls and Cows
# Author(s):   Phu Tran
# --------------------------------------------------------------------------
"""
    You are playing the following Bulls and Cows game with your friend:
      You write down a number and ask your friend to guess what the number
      is. Each time your friend makes a guess, you provide a hint that 
      indicates how many digits in said guess match your secret number
      exactly in both digit and position (called "bulls") and how many
      digits match the secret number but locate in the wrong position
      (called "cows"). Your friend will use successive guesses and
      hints to eventually derive the secret number.

    Write a function to return a hint according to the secret number and 
    friend's guess, use A to indicate the bulls and B to indicate the cows. 

    Please note that both secret number and friend's guess may contain duplicate digits.

    Example 1:
      Input: secret = "1807", guess = "7810"
      Output: "1A3B"
      Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
    
    Example 2:
      Input: secret = "1123", guess = "0111"
      Output: "1A1B"
      Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
    
    Note: You may assume that the secret number and your friend's guess 
          only contain digits, and their lengths are always equal.
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        secretList = list(secret)
        guessList = list(guess)
        
        for i in range(len(secretList)):
            if secretList[i] == guessList[i]:
                bull += 1
                secretList[i] = "*"
                guessList[i] = "*"
        
        for i in range(len(secretList)):
            digit = secretList[i]
            if digit != "*" and digit in guessList:
                guessList[guessList.index(digit)] = "*"
                cow += 1
        
        return str(bull) + "A" + str(cow) + "B"
            
        
        
                    
            
        
        
        
        
        
        
        
        
    
        
            
        
 



        
'''other faster methods (from other submissions)
##################################################
def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(secret[i] == guess[i] for i in range(len(guess)))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return "{}A{}B".format(bulls, both-bulls)
##################################################
def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        A = B = 0
        for i, c in enumerate(guess):
            if c == secret[i]:
                A += 1
            else:
                s1[c] += 1
                s2[secret[i]] += 1
        for key in s1.keys():
            if key in s2:
                B += min(s1[key], s2[key])
        return "{}A{}B".format(A, B)
##################################################
def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = sum(s == g for s, g in zip(secret, guess))
        total = collections.Counter(secret) & collections.Counter(guess)
        return "{}A{}B".format(a, sum(total.values()) - a)
##################################################
'''
