ch= input("Enter alphabet =>").upper()


vowel = ['A','E','I','O','U']

def checkVowOrCon(ch):
    '''
        This is a docstring this function checkVowOrCon
    '''
    if ch.isalpha(): 
        if ch in vowel:
            return "{} is a vowel".format(ch)
        else:
            return f"{ch} is a consonant"
    else:
        return "enter a Alphabetic"

print(checkVowOrCon(ch))