import pandas as pd
df=pd.read_csv('final.csv')

print("Hello~",df.shape)
del df['pl_orbpererr1']
del df['pl_orbpererr2']
del df['pl_orbperlim']
del df['pl_orbsmax']
del df['pl_orbsmaxerr1']
del df['pl_orbsmaxerr2']
del df['pl_orbsmaxlim']
del df['pl_orbeccen']
del df['pl_orbeccenerr1']
del df['pl_orbeccenerr2']
del df['pl_orbeccenlim']
df.to_csv('new.csv')