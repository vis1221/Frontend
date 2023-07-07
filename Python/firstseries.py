import pandas as pd
a=[1,2,3,4]
b=[1,2,3,4]
myvar=pd.Series(a)
print(myvar)
print("accessing first value in Series",myvar[0])
Labels=pd.Series(a,index=["X","Y","Z","A"])
print(Labels["A"])
