import pandas as pd
pd.options.display.max_rows=9
Newdata=pd.read_csv('data.csv')
print(Newdata.to_string())
##print(pd.options.display.max_rows)
