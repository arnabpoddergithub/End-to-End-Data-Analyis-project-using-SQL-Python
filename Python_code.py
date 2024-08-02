<br>
#import libraries
#!pip install opendatasets
#!pip install pandas
#!pip install kaggle
import kaggle

!kaggle datasets download ankitbansal06/retail-orders -f orders.csv

#extract file from zip files 
import zipfile
zip_ref = zipfile.ZipFile('C:\\Users\\Hp\\sq+python\\orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


#import datasets into pandas and to read first 30 rows from the datasets
import pandas as pd
df=pd.read_csv('C:\\Users\\Hp\\sq+python\\orders.csv')
df.head(30)



#read data from the file and handle null values
df=pd.read_csv('C:\\Users\\Hp\\sq+python\\orders.csv',na_values=['Not Available','unknown'])
df.head(30)
df['Ship Mode'].unique()#shows the number of unique values present inside ship mode


#rename columns names ..make them lower case and replace space with underscore
df.columns=df.columns.str.lower()
df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.replace(' ','_')
df.head(5)



#derive new columns discount , sale price and profit
df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df



#convert order date from object data type to datetime
import datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df.dtypes



#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
df.head(5)

#load the data into sql server using replace option
import sqlalchemy as sal
engine=sal.create_engine('mssql://Arnab-Podder/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()
df.to_sql('df_orders',con=conn,index=False,if_exists='replace')


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


