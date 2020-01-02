import pandas as pd

df1
pd.DataFrame(M1, index=l1, columns=l2) # index = dates , 

----------pandas IO -----------------
pd.read_csv(s1)
pd.read_html(s1) #reads all <table> tags in html, make dfs and return a list of dfs
pd.read_json
pd.read_excel(s1) # s1 the string of file url, file:///home/.../a.xlx http://www.sth.com/hi.xlx
pd.read_sql(s1)

pd.to_csv ,...
--------------------------------------
df1.to_numpy() # out dated: df1.values
df1.sort_index()
df1.sort_values()
---------
df1.head(n) # returns the first n rows

df1[o1] # column
df1[i1:i2]
df1.loc[]
df1.iloc[]

df[].values
df1=df2.copy()


