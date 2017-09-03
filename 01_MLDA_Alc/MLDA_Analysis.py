import os
import pandas as pd

os.chdir("/Users/Sam/Documents/Depauw/Senior Year/Econ Seminar/ECON1_MDLA")

#Read in data from csv
raw_data = pd.read_csv("ECON1_MLDA_RAW.csv")


def reformat_data(data):

	data.replace({'CATAG7':{4:1,5:0}}, regex = True, inplace = True)

	data.drop(data.columns[[0,3,4,5,12,15,16]], axis = 1, inplace = True)

	#Drop all nonresponse and error data for yearly alcohol consumption
	data = data[data.ALCYRTOT != 985]
	data = data[data.ALCYRTOT != 994]
	data = data[data.ALCYRTOT != 997]
	data = data[data.ALCYRTOT != 998]

	#Drop other combination races to provide reference for main races (White, Black, Asian)
	data = data[data.NEWRACE2 != 3]
	data = data[data.NEWRACE2 != 4]
	data = data[data.NEWRACE2 != 6]

	#Drop all divorce and widowed Data to provide reference for Marital Status
	data = data[data.IRMARITSTAT != 2]
	data = data[data.IRMARITSTAT != 3]
	data = data[data.IRMARITSTAT != 99]

	data.reset_index(drop = True, inplace =True)

	#Create dummy variables for CATAG7, rename Under21 (occurs later)
	data.replace({'CATAG7':{4:1,5:0}}, regex = True, inplace = True)

	#Create dummy variables for race
	race_dummies = pd.get_dummies(pd.Series(list(data.NEWRACE2)))
	data = pd.concat([data,race_dummies], axis = 1)
	data.rename(columns={1: 'White', 2: 'Black', 5: 'Asian', 7: 'Hispanic'}, inplace=True)

	#Change IRSEX femalse code tozero
	data.replace({'IRSEX':{2:0}}, regex = True, inplace = True)

	#Change Codes to married or nonmarried dummy
	data.replace({'IRMARITSTAT':{4:0}}, regex = True, inplace = True)

	#Change code for education to dummy variables
	educ_dummies = pd.get_dummies(pd.Series(list(data.EDUHIGHCAT)))
	data = pd.concat([data,educ_dummies], axis = 1)
	data.rename(columns={1: 'LessHighS', 2: 'HighSchool', 3: 'SomeCollege', 4: 'CollegeGrad'}, inplace=True)

	#Change code for work status to dummy variables
	data.replace({'IRWRKSTAT':{2:1}}, regex = True, inplace = True)
	work_dummies = pd.get_dummies(pd.Series(list(data.IRWRKSTAT)))
	data = pd.concat([data,work_dummies], axis = 1)
	data.rename(columns={1: 'Employed', 3: 'Unemployed', 4: 'Student/Other'}, inplace=True)

	#Create Income Dummy Variables
	income_dummies = pd.get_dummies(pd.Series(list(data.INCOME)))
	data = pd.concat([data,income_dummies], axis = 1)
	data.rename(columns={1: 'Less20k', 2: '20-50k', 3: '50-75k', 4: 'Over75k'}, inplace=True)

	#Alter ALCYRTOT to include no drinking people
	data.replace({'ALCYRTOT':{991:0, 993:0}}, regex = True, inplace = True)

	#Drop un-needed columns (variables used to create dummies)
	data.drop(data.columns[[5,6, 7, 8]], axis = 1, inplace = True)

	#Final rename of Alcohol Columns
	data.rename(columns={'ALCYRTOT': 'AlcYearTotal', 
						 'IRSEX': 'Male',
						 'CATAG7': 'Under21', 
						 'ABUSEALC':'AlcoholAbuse', 
						 'IRMARITSTAT':'Married',
						 'ALCFLAG':'EverHadAlcohol'}, inplace=True)

	#Drop Index
	data.set_index('Male', inplace = True)

	#print(data.describe().T)
	data.to_csv('MLDA_Data.csv', sep = ',')

	return data



#Generate Summary Data 
data = reformat_data(raw_data)

under21data = data[data.Under21 == 1]
over21data = data[data.Under21 == 0]

under21summary = under21data.describe().T
over21summary = over21data.describe().T

import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import table

ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

under21 = table(ax, under21summary)  # where df is your data frame

plt.savefig('under21desc.png')


print(under21summary)
print()
print(over21summary)








