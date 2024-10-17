import numpy as np
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

cars_per_cap = cars_csv_df['cars_per_cap']
np.logical_or(cars_per_cap<200,cars_per_cap==809) #a pandas series with True or False values if either criteria is True

cars_csv_df[cars_csv_df['drives_right']] #return df where drives right is true

for lab,row in cars_csv_df.iterrows():
	cars_csv_df.loc[lab,"COUNTRY"] = row["country"].upper() #create a new column via iterrows
	
cars_csv_df["COUNTRY"] = cars_csv_df["country"].apply(str.upper) #a non iterative way to update a DF

cars_csv_df.head(2) #returns df containing first 2  rows of df
cars_csv_df.values #a numpy array, each value is a numpy row representing a row from the df 
cars_csv_df.columns #object containing all column names from the df
cars_csv_df.index #returns the index label of the dataframe
cars_csv_df.sort_values("COUNTRY") #sort df

cars_csv_df[cars_csv_df["cars_per_cap"] >700] # filter where cars_per_cap > 700
cars_csv_df[(cars_csv_df["cars_per_cap"] >700) & (cars_csv_df["cars_per_cap"] >800)] # filter on multiple cols
cars_csv_df[cars_csv_df["country"].isin(["Egypt","Russia"])] #IN where clause
cars_csv_df[cars_csv_df['cars_per_cap'] == cars_csv_df['cars_per_cap'].max()] #filtering using a calculation
cars_csv_df["double_cars_per_cap"] =cars_csv_df["cars_per_cap"]*2 #a new calculated column

cars_csv_df.info() #num of records, col names, col types

cars_csv_df["cars_per_cap"].mean()  #returns mean of column

def example(column):
	return 2*column.sum() #double the sum of the column
print(cars_csv_df['cars_per_cap'].agg(example)) #use agg to apply custom functions to df

print (cars_csv_df["cars_per_cap"].cumsum()) #cumulative sum 


new_row = pd.DataFrame([['United States','True','809','UNITED STATES','3000']]
					   		,columns=['country','drives_right','cars_per_cap','COUNTRY','double_cars_per_cap']
							,index = ['US']) #create a new row to add to df, country already exists in original df

pd.concat([cars_csv_df,new_row]).drop_duplicates(subset=['country'],keep='last') #drop the duplicate record, keeping the last one

cars_csv_df["drives_right"].value_counts() #count the number of rows for each value of the field

cars_csv_df["cars_per_cap"].count() #count number of records with a value
cars_csv_df.groupby("drives_right")["cars_per_cap"].sum() #group by and sum
cars_csv_df.groupby("drives_right")["cars_per_cap"].agg(["min","max","mean","median"]) #calculate various aggregates
cars_csv_df.groupby("drives_right")["cars_per_cap"].agg([min,max,np.mean,np.median]) #using non pandas function to agg - in this case numpy functions
cars_csv_df.pivot_table(values='cars_per_cap',
						index="drives_right",
						columns="COUNTRY",
						aggfunc=["mean","median"],
						fill_value=0) #creating a pivot table - not a great dataset for showing the functionality but it demonstrates the point'


cars_csv_df = cars_csv_df.reset_index().set_index(['drives_right','country_code'],drop=False)#.sort_index(level=['drives_right','country_code'],ascending=[True,False]) #set an index for df, keep the column
cars_csv_df = cars_csv_df.sort_index(level = ['drives_right','country_code'],ascending=[True,False]) #sort the index
cars_csv_df =  cars_csv_df.sort_index() #enables lex sorting, which allows index slicing
cars_csv_df.loc[(False,'AUS'):(False,'IN')] #index slicing
cars_csv_df.loc[(False,'AUS'):(False,'IN'),'COUNTRY':'double_cars_per_cap'] #index slicing and slicing columns too
cars_csv_df.iloc[0:2,0:3] #slicing using row/col number

pd.DataFrame({ 'colA':[1,2,3], 'colB': [4,None,6]} ).isna() #check values for NULL values
pd.DataFrame({ 'colA':[1,2,3], 'colB': [4,None,6]} ).isna().any() #check cols for NULL values
pd.DataFrame({ 'colA':[1,2,3], 'colB': [4,None,6]} ).dropna() #remove rows with na

csv_path = dir_path + '\\files\\cars_output.csv'
cars_csv_df.to_csv(csv_path) #output dataframe to file