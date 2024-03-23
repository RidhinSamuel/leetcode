
import math



ab=int(input())
bc=int(input())

ac=math.sqrt(pow(ab,2)+pow(bc,2))

mc=ac/2

bm=math.sqrt(pow(bc,2)-pow(mc,2))

tan=mc/bm
angle=math.atan2(tan)
print(angle)