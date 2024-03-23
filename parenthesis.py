




class Solution:
    
    def isValid(self, s: str) -> bool:
        openb=['(','[','{']
        closeb=[')',']','}']
        flag=2
        #print(s)

        for i in range(0,len(s),2):
            #print(i)
            
            if s[i] in openb :
                ind=openb.index(s[i])
                #print(2)
                if closeb[ind]==s[i+1] and s[i+1] in closeb:
                    print(s[i+1])
                    flag=1
                else:
                    flag=2
            else:
                flag=2
        #print(3)
        if flag==1:
            print( True)
            
        else:
            print( False)
        


s=Solution()
s.isValid(")")