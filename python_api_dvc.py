# Get url from DVC
import pandas as pd
import dvc.api

path='data/wine_original.csv'
repo=r'C:\Users\janni\Dropbox\university\DSTI\004_MLOps\labs\lab_01\data_versioning'

data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  rev='v1'
  )

data_v1 = pd.read_csv(data_url, sep=";")
print(data_v1)



data_url = dvc.api.get_url(
  path=path,
  repo=repo,
  )

data_latest = pd.read_csv(data_url, sep=";")
print(data_latest)