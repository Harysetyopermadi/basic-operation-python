import pandas as pd
import pyodbc

#koneksi
# Define the connection parameters
try:
    server = '192.168.0.41'
    database = 'REKON_CASH'
    username = 'hary'
    password = '1234'
    # Create a connection string
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    # Establish a connection
    cnxn = pyodbc.connect(connection_string,autocommit=True)
    # Create a cursor object to interact with the database
    cursor = cnxn.cursor()
    print("Koneksi Berhasil")
except:
    print("Gagal Koneksi")
    
#change query to pandas/ table
df=pd.read_sql("select * from stg_ej_atm",cnxn)

#function filter example
df=df[(df['status']=='Gagal')& (df['narrative']=='Terindikasi Host Stored')]

#reset index 
df=df.reset_index()

#drop index old
df.drop('index',axis=1,inplace=True)

#pandas to array
#df=df.values

#pandas to JSON
#df=df.to_json(orient='records')

#pattern cell
#df=df.iloc[1,1]

#sum column 
#df=df['amount'].sum()

#average column
#df=df['amount'].mean()

#sum with filter
#df=df['amount'][df['atm_id']=='AT802903'].sum()

#filter column with contain or in sql with like
#df = df[df['atm_id'].str.contains('AT80', case=False, regex=True)]

#sort column
#df = df.sort_values(by='amount', ascending=False)

#create column rank
#df['Rank'] = df['amount'].rank(ascending=False).astype(int)

print(df)
