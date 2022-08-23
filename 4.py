x=999
y=999
res=''
resReversed=''
max=0
while x>=100:
    y=999
    while y>=x:
        res=str(x*y)
        if int(res)<max:
            break
        resReversed=res[::-1]
        if res==resReversed:
            if int(res)>=max:
                max=int(res)
        y-=1
    x-=1
print(max)