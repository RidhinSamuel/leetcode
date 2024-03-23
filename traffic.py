#Traffic Flow

n,m=map(int,input().split())
trafficGrid=[]
fastest_time=0
for i in range(n):
    l=list(map(int,input().split()))
    trafficGrid.append(l)
string=input().split()
start=(int(string[0])-1,int(string[1])-1)
string=input().split()
end=(int(string[0])-1,int(string[1])-1)
i,j=start
x,y=end
flag=0
#fastest_time = find_fastest_route(trafficGrid, start, end)

while(True):
    if i>x or j>y:
        flag=0
        break
    if (i,j)==end:
        flag=1
        break
    down_sum = 0
    right_sum=0

    right_sum=sum(trafficGrid[i][j:])
    for k in range(i,x):
        down_sum += trafficGrid[k][j]
    if (right_sum<down_sum or i==x) and j!=m-1:
        j+=1
    else:
        i+=1
    fastest_time+=trafficGrid[i][j]
if flag==1:
    fastest_time+=trafficGrid[start[0]][start[1]]
else:
    fastest_time=-1
print(fastest_time,end="")