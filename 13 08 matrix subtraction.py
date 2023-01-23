a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[4,6,2],[9,0,3],[2,3,5]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        r[i][j]=a[i][j]-b[i][j]
for i in r:
    print(i)
