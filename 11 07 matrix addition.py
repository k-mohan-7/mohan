a=[[1,2,2,3],[8,6,3,5],[6,3,5,1]]
k=[[5,6,3,2],[8,6,4,2],[9,5,1,2]]
c=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range (len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+k[i][j]
print(c)
            
                   
                   
