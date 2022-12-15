import pandas as pd
data=pd.DataFrame({'1':['TOI','Hindu','ET','BM','Ht'],'Monday':[3,2.5,4,1.5,2],
                   'Tue':[3,2.5,4,1.5,2]

             	,'wed':[3,2.5,4,1.5,2]

               	,'Thur':[3,2.5,4,1.5,2]
                  ,'fri':[3,2.5,4,1.5,2]
                  ,'sat':[5,4,4,1.5,4]
                   ,'sun':[6,4,10,1.5,4]})
print(data)
b=data.sum(axis=1)
print(a)
b.map()
v = input()
for i in b:
    for j in i:
        if (b[i]+b[j]<=v):
        print(i,j)
