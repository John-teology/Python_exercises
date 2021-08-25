def minion_game(string):
    """
    This function takes any string args and count how many words you can create with that string 
    that starts with consosnants and vowel and print the winner. Kevin for the vowels and Stuart for the consonants
    """
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ str(S)) #consonants
    elif K>S:
        print("Kevin"+" "+ str(K))  # vowels
    else:
        print("Draw")
        
        
minion_game('Banana')
        
