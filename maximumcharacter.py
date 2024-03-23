import time
def findMaximumCharacter(s:str)->int:
    maxFrequency=0
    maxChar=''
    for i in s:
        if maxFrequency==0:
            maxChar=i
            maxFrequency+=1
        elif i!=maxChar:
            maxFrequency-=1
        else:
            maxFrequency+=1
    if maxFrequency==0:
        return s,maxFrequency,maxChar,False
    return s,maxFrequency,maxChar,True
limit=int(input())
print(f"Limit is {limit}")
for i in range(limit):
    result=findMaximumCharacter(input())
    print(f"The maximum character for the string '{result[0]}' appears {result[1]} times Char={result[2]} True/False={result[3]}")