import os
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc } #creating a dictionary of dictionaries


cars = pd.DataFrame(cars_dict) #create dataframe from dictionary

cars.index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']	#creating row labels

dir_path = os.path.dirname(os.path.realpath(__file__)) #get current folder
csv_path = dir_path + '\\files\\cars.csv'

cars_csv_df  = pd.DataFrame (pd.read_csv(csv_path,index_col=0)) #create data frame from a csv, first col contains row labels

cars_csv_df['country'] #reference a column as a series
cars_csv_df[['country']] #reference a column as a data frame
cars_csv_df[['country','drives_right']] #reference two columns as a data frame
cars_csv_df[0:3] #reference first three columns
cars_csv_df.loc[['AUS','EG']] #reference the AUS and EG rows
cars_csv_df.loc[['MOR'],['drives_right']] #reference the MOR row, drives right column
cars_csv_df.loc[['RU','MOR'],['country','drives_right']] #reference the RU and MOR row, country and drives right col

import numpy as np
cars_per_cap = cars_csv_df['cars_per_cap']
np.logical_or(cars_per_cap<200,cars_per_cap==809) #a pandas series with True or False values if either criteria is True

cars_csv_df[cars_csv_df['drives_right']] #return df where drives right is true

for lab,row in cars_csv_df.iterrows():
	cars_csv_df.loc[lab,"COUNTRY"] = row["country"].upper() #create a new column via iterrows
	
cars_csv_df["COUNTRY"] = cars_csv_df["country"].apply(str.upper) #a non iterative way to update a DF