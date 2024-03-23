"""
Minimum Length of String After Deleting Similar Ends
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

"""


def minimumLength(s):
    left=0;right=len(s)-1
    while (left<right):
        if s[left]==s[right]:
            while(left+1<right):
                if s[left]==s[left+1]:
                    left+=1
                else:
                    break
            while(right-1>left):
                if s[right]==s[right-1]:
                    right-=1
                else:
                    break
        else:
            return len(s[left:right+1])
case=[input() for i in range (3)]

for i in (case):
    print("INPUT :-",i)
    print(minimumLength(i))