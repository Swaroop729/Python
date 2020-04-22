import re

def func(s,l):
    for i in range(len(s)+1):
        word = s[0:i]
        if word not in l:
            if(word!=''):
                l.append(s[0:i])

def count_substring(string, sub_string):
    l=[]
    f=0
    for i in string:
        s=string.find(sub_string,f,len(string))
        if s !=-1:
            l.append(s)
            f=s+1
    return(len(l))

def minion_game(givenstring):
    # your code goes here
    if(0<len(givenstring)<=10**6):
        s=givenstring
        l=[]
        for i in range(len(s)):
            func(s,l)
            s=s[1:]
        vowels="AEIOU"
        Stuart=0
        Kevin=0
        for i in l:
            if(i[0] in vowels):
                Kevin = Kevin + count_substring(givenstring, i)
            else:
                print(i)
                Stuart = Stuart + count_substring(givenstring, i)
        if( Stuart > Kevin  ):
            print(f"Stuart {Stuart}")
        elif (Stuart < Kevin):
            print(f"Kevin {Kevin}")
        elif(Stuart == Kevin ):
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)