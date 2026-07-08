import pandas as pd

data = {
    "Product":['Wireless Earbuds', 'Smartphone', 'Laptop','Smartwatch', 'Bluetooth Speaker'],
    'Brand':['Sony', 'Apple', 'Dell', 'Fitbit', 'JBL'],
    "Price":[2999,15999,52999,4999,1999],
    'Stock':[50,30,20,40,60],
    'Bestseller':[True, False,False,True,True]
}

df = pd.DataFrame(data)
print(df)


df1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["Alice","Bob"],
    "Age":[25,30]
})

df2 = pd.DataFrame({
    "ID":[2,3],
    "Name":["David","Charlie"],
    "Age":[28,35]
})

df_combined = pd.concat([df1,df2],axis=0)
print(df_combined)

df_combined = pd.concat([df1,df2],axis=1)
print(df_combined)

print(df,'\n')
df.pivot_table(values="Price",index="Brand", columns="Stock",aggfunc="max")

print(df)

pd.crosstab(df["Brand"],df['Stock'])

import pandas as pd
import numpy as np

data3 = {
    "A" : [1,2,np.nan,4,5],
    "B" : [np.nan,4,3,np.nan,1],
    "C" : [2,np.nan,np.nan,8,10]
}

df3 = pd.DataFrame(data3)
print("Original DataFrame with Null Values:\n",df3)


df_dropna = df3.dropna()
print("DataFrame After Dropping Null Values:\n",df_dropna)

df3_interpolate = df3.interpolate()
print("DataFrame After Interpolation:\n",df3_interpolate)

from google.colab import files
uploaded = files.upload()

import pandas as pd

df4 = pd.read_csv("email.csv")
print(df4)
