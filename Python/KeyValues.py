import pandas as pd
calories={"Day1":20,"Day2":120,"Day3":220,"Day4":40,"Day5":20,}
Keys=pd.Series(calories)
print(Keys)
Keys=pd.Series(calories,index={"Day2","Day3"})
print(Keys)
