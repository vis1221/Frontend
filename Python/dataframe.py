import pandas as pd
data={"calories":[40,20,10],
      "duration":[10,20,30]}
NewFrame=pd.DataFrame(data,index=["Day1","Day2","Day3"])
print(NewFrame.loc["Day1"])


