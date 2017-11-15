clear
*NOTE: Do-file requires you to tap any key on the keyboard to
*page through regression and estout output in STATA. 
*Program will pause until you have done so. 


*Utilizing raw dataset for project
import delimited I:\17181-ECON480B\SAMUELSHOWALTER_2018\ECON2\ATC_Data_FINAL.csv

* get pretty reg results package
ssc install estout, replace
eststo clear

* Removed aug, sweden, and switzerland variables to prevent multicollinearity
regress flt_arr_1_dly_15 private flt_arr_1 ///
		france germany netherlands unitedkingdom /// 
		jan feb mar apr may jun jul sep oct nov dec, robust

*Store regression analysis for country controlled analysis (country dummies) (with robust SE)

* Number of delays that were over 15 minutes
eststo: regress flt_arr_1_dly_15 private flt_arr_1 ///
		france germany netherlands unitedkingdom /// 
		jan feb mar apr may jun jul sep oct nov dec, robust
					 
* Number of minutes of delay on average per day
eststo: regress dly_apt_1 private flt_arr_1 ///
		france germany netherlands unitedkingdom /// 
		jan feb mar apr may jun jul sep oct nov dec, robust
					 
* Number of minutes of delay due to inefficient ATC capacity
eststo: regress dly_apt_arr_c_1 private flt_arr_1 ///
		france germany netherlands unitedkingdom /// 
		jan feb mar apr may jun jul sep oct nov dec, robust
		
* Number of minutes of delay due to ATC staffing issue
eststo: regress dly_apt_arr_s_1 private flt_arr_1 ///
		france germany netherlands unitedkingdom /// 
		jan feb mar apr may jun jul sep oct nov dec, robust
			
			
*Re-labeling Data
label variable flt_arr_1_dly_15 "Dly15min+"
label variable flt_arr_1 "NumFlights"
label variable dly_apt_1 "AvgMinDly"
label variable dly_apt_arr_c_1 "DlyATCCap"
label variable dly_apt_arr_s_1 "DlyATCStaff"

*Output saved regression table
esttab, se varwidth(25) label r2 ar2 nogaps ///
title(OLS Analysis of ATC Efficiency and the impact of Corporate Structure) ///
addnotes(Standard Errors robust. Sweden, Switzerland, Aug removed to prevent multicollinearity.)


* Not store regression results for airline analysis
eststo clear
