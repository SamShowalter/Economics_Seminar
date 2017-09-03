clear
*NOTE: Do-file requires you to tap any key on the keyboard to
*page through regression and estout output in STATA. 
*Program will pause until you have done so. 


*Utilizing raw dataset for project
import delimited I:\17181-ECON480B\SAMUELSHOWALTER_2018\ECON1\MLDA_Data.csv

* get pretty reg results package
ssc install estout, replace

*Asian, studentother (lacks precisision), lesshighs, and less20k omitted to prevent multicollinearity in dummy variables
regress alcoholabuse under21 male married white ///
					 black hispanic highschool somecollege ///
					 collegegrad employed studentother v19 v20 over75k

*Store regression analysis (with robust SE)

*Ever had alcohol
eststo: regress everhadalcohol under21 male married white ///
					 black hispanic highschool somecollege ///
					 collegegrad employed unemployed v19 v20 over75k, robust
					 
*Number of days drank last year
eststo: regress alcyeartotal under21 male married white ///
					 black hispanic highschool somecollege ///
					 collegegrad employed unemployed v19 v20 over75k, robust
					 
*Alcohol Abuse ever
eststo: regress alcoholabuse under21 male married white ///
					 black hispanic highschool somecollege ///
					 collegegrad employed unemployed v19 v20 over75k, robust
			
			
*Re-labeling Data
label variable everhadalcohol "EverHadAlc"

*Output saved regression table
esttab, se varwidth(25) label r2 ar2 nogaps ///
title(OLS Regression Discontinuity Design (RDD) MLDA Alcohol Regressions)

