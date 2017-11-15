import os
import pandas as pd
from numpy import mean, median

os.chdir("/Users/Sam/Documents/Depauw/04 Senior Year/Econ Seminar/Economics_Seminar/05_LOVE")

#Read in data from csv
raw_data = pd.read_csv("Speed_Dating_Raw_Data.csv")


def reformat_data(data):

	"""

	field_cd: 	field coded 
	1= Law  
	2= Math
	3= Social Science, Psychologist 
	4= Medical Science, Pharmaceuticals, and Bio Tech 
	5= Engineering  
	6= English/Creative Writing/ Journalism 
	7= History/Religion/Philosophy 
	8= Business/Econ/Finance 
	9= Education, Academia 
	10= Biological Sciences/Chemistry/Physics
	11= Social Work 
	12= Undergrad/undecided 
	13=Political Science/International Affairs 
	14=Film
	15=Fine Arts/Arts Administration
	16=Languages
	17=Architecture
	18=Other


	race:
	Black/African American=1
	European/Caucasian-American=2
	Latino/Hispanic American=3
	Asian/Pacific Islander/Asian-American=4
	Native American=5
	Other=6


	goal:
	What is your primary goal in participating in this event? 
	Seemed like a fun night out=1
	To meet new people=2
	To get a date=3
	Looking for a serious relationship=4
	To say I did it=5
	Other=6

	"""

	obc_dict =   {1:"obc_fun_night",
				  2:"obc_new_ppl",
				  3:"obc_get_date.",
				  4:"obc_ser_rel.",
				  5:"obc_tosayso.",
				  6:"obc_ther"}


	#Replace race codes with values
	data.replace({'race':
				 {1:"Black",
				  2:"White",
				  3:"Hispanic.",
				  4:"Asian.",
				  5:"Native_Am.",
				  6:"race_other"}}, regex = True, inplace = True)
	
	#Replace partner race codes with values
	data.replace({'P_Race':
				 {1:"P_Black",
				  2:"P_White",
				  3:"P_Hispanic.",
				  4:"P_Asian.",
				  5:"P_Native_Am.",
				  6:"P_race_other"}}, regex = True, inplace = True)

	#Replace field codes with values
	data.replace({'Field_code':
				 {1:"Law",
				  2:"Math",
				  3:"Social_Sc.",
				  4:"Medical_Sc.",
				  5:"Engineering",
				  6:"Journal.Eng.",
				  7:"History.Rel.",
				  8:"Business.Econ.",
				  9:"Education",
				  10:"Bio.Chem.Phys.",
				  11:"Social.Wrk.",
				  12:"Undecided.Stud.",
				  13:"PoliSci.Intl.",
				  14:"Film",
				  15:"Fine_Arts",
				  16:"Language",
				  17:"Architecture",
				  18:"fd_other"}}, regex = True, inplace = True)

	#Replace goal codes with values
	data.replace({'goal':
			 {1:"obc_fun_night",
			  2:"obc_new_ppl",
			  3:"obc_get_date.",
			  4:"obc_ser_rel.",
			  5:"obc_tosayso.",
			  6:"obc_ther"}}, regex = True, inplace = True)


	#Create dummy variables for field
	field_dummies = pd.get_dummies(pd.Series(list(data.Field_code)))
	data = pd.concat([data,field_dummies], axis = 1)

	#Create dummy variables for race
	race_dummies = pd.get_dummies(pd.Series(list(data.race)))
	data = pd.concat([data,race_dummies], axis = 1)

	#Create dummy variables for goal
	goal_dummies = pd.get_dummies(pd.Series(list(data.goal)))
	data = pd.concat([data,goal_dummies], axis = 1)

	#Replace blank values (that represent zero here) with zero
	data.P_Pref_Shar.fillna(0, inplace = True)
	data.Pref_Shar.fillna(0, inplace = True)

	#Replace values and refine data for "Met"
	data.replace({'Met':{1:0}}, regex = True, inplace = True)
	data.replace({'Met':{2:1}}, regex = True, inplace = True)
	data.Met.fillna(0,inplace = True)

	#Re-calibrate data for more intuitively understanding in analysis
	data.date = 7 - data.date
	data.Go_Out = 7 - data.Go_Out

	#Drop unnecessary fields
	data.drop('Field_code', axis = 1, inplace = True)
	data.drop('race', axis = 1, inplace = True)
	data.drop('goal', axis = 1, inplace = True)
	data.drop('P_Race', axis = 1, inplace = True)

	#Separate data and reformat axes
	male_data = data[data.Male == 1]
	male_data.reset_index(drop = True, inplace =True)
	female_data = data[data.Female == 1]
	female_data.reset_index(drop = True, inplace =True)

	# #Drop Index
	# data.set_index('Male', inplace = True)

	# #print(data.describe().T)
	# data.to_csv('MLDA_Data.csv', sep = ',')

	return male_data, female_data

def format_by_gender(data):

	#Fill missing partner ratings
	data.P_Attr.fillna(data.P_Attr.median(), inplace = True)
	data.P_Sinc.fillna(data.P_Sinc.median(), inplace = True)
	data.P_Intel.fillna(data.P_Intel.median(), inplace = True)
	data.P_Fun.fillna(data.P_Fun.median(), inplace = True)
	data.P_Amb.fillna(data.P_Amb.median(), inplace = True)
	data.P_Shar.fillna(data.P_Shar.median(), inplace = True)

	#Fill missing ratings
	data.Attr.fillna(data.Attr.median(), inplace = True)
	data.Sinc.fillna(data.Sinc.median(), inplace = True)
	data.Intel.fillna(data.Intel.median(), inplace = True)
	data.Fun.fillna(data.Fun.median(), inplace = True)
	data.Amb.fillna(data.Amb.median(), inplace = True)
	data.Shar.fillna(data.Shar.median(), inplace = True)

	data.dropna(inplace = True)

	return data


#Generate Summary Data 
#data = reformat_data(raw_data)

male_data, female_data = reformat_data(raw_data)

male_data = format_by_gender(male_data)
female_data = format_by_gender(female_data)

# print(male_data.describe())

male_data.to_csv("male_love_data.csv")
female_data.to_csv("female_love_data.csv")














