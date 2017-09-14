import os
import pandas as pd

os.chdir("/Users/Sam/Documents/Depauw/04 Senior Year/Econ Seminar/Economics_Seminar/02_ATC_Delays")

#Read in data from csv
raw_data = pd.read_csv("ECON2_Data_ATC.csv", encoding = 'latin-1')


def reformat_data(data):

	#Drop unnecessary columns
	data.drop(data.columns[[0,1,10]], axis = 1, inplace = True)

	# Add new field to identify if country uses PPP (more Private) or a government corporation
	data["Private"] = data.STATE_NAME
	data.replace({"Private:":{'France': 0, 'Germany': 0, 'Netherlands': 1,"Switzerland": 1, "Sweden": 0,"United Kingdom": 1}}, regex = True, inplace = True)


	# Change code for months to dummy variables
	month_dummies = pd.get_dummies(pd.Series(list(data.MONTH_MON)))
	data = pd.concat([data,month_dummies], axis = 1)
	data.drop(data.columns[[0]], axis = 1, inplace = True)


	#Change code for country to dummy variables
	country_dummies = pd.get_dummies(pd.Series(list(data.STATE_NAME)))
	data = pd.concat([data,country_dummies], axis = 1)
	data.drop(data.columns[[1]], axis = 1, inplace = True)


	#Change code for work status to dummy variables
	apt_dummies = pd.get_dummies(pd.Series(list(data.APT_NAME)))
	data = pd.concat([data,apt_dummies], axis = 1)
	data.drop(data.columns[[0]], axis = 1, inplace = True)


	# Drop Index
	data.set_index('FLT_ARR_1', inplace = True)

	#print(data.describe().T)
	data.to_csv('ATC_Data_FINAL.csv', sep = ',')


	#return data
	return data



#Generate Summary Data 
data = reformat_data(raw_data)


#Generate summary statistics page
data.describe().T.to_csv("ATC_Summary_Stats.csv")











