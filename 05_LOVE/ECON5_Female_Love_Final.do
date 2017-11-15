clear
*NOTE: Do-file requires you to tap any key on the keyboard to
*page through regression and estout output in STATA. 
*Program will pause until you have done so. 


*Utilizing raw dataset for project
import delimited I:\17181-ECON480B\SAMUELSHOWALTER_2018\ECON5\female_love_data.csv

* get pretty reg results package
ssc install estout, replace
eststo clear

* Store regression analysis for Female Mate Preference choices in speed dating

* FEMALE regression. 

* No partner attributes or preferences considered
eststo: regress matched ///
		age attr sinc intel fun amb shar like ///
		order_met interest_corr same_race importance_race importance_religion date go_out ///
		architecture biochemphys businessecon education engineering film fine_arts historyrel journaleng language law math medical_sc polisciintl socialwrk social_sc undecidedstud ///
		asian black hispanic white ///
		obc_fun_night obc_get_date obc_new_ppl obc_ser_rel obc_tosayso

* No partner attributes. Dropped all other variables
eststo: regress matched ///
		age date go_out attr sinc intel fun amb shar like ///
		p_age p_attr p_sinc p_intel p_fun p_amb p_shar p_like ///
		order_met interest_corr same_race importance_race importance_religion  ///
		architecture biochemphys businessecon education engineering film fine_arts historyrel journaleng language law math medical_sc polisciintl socialwrk social_sc undecidedstud ///
		asian black hispanic white ///
		obc_fun_night obc_get_date obc_new_ppl obc_ser_rel obc_tosayso

* Everything. Omitted language, race_other, fd_other, 
eststo: regress matched ///
		age date go_out pref_attr pref_sinc pref_intel pref_fun pref_amb ///
		attr sinc intel fun amb shar like ///
		p_age p_pref_attr  p_pref_sinc p_pref_intel p_pref_fun p_pref_amb p_pref_shar ///
		p_attr p_sinc p_intel p_fun p_amb p_shar p_like ///
		order_met interest_corr same_race importance_race importance_religion ///
		architecture biochemphys businessecon education engineering film fine_arts historyrel journaleng language law math medical_sc polisciintl socialwrk social_sc undecidedstud ///
		asian black hispanic white ///
		obc_fun_night obc_get_date obc_new_ppl obc_ser_rel obc_tosayso 

*Output saved regression table
esttab, se varwidth(25) label r2 ar2 nogaps nolabel ///
title(OLS Analysis of Speed Dating and Mate Preference, Women) ///
rename(age Age attr Attractiveness sinc Sincerity intel Intelligence fun Fun amb Ambition shar Shared_Traits like Like_Level date Date_Freq go_out Go_Out_Freq, order_met Order_Met p_age P_Age p_attr P_Attractive p_sinc P_Sincerity p_intel P_Intelligence p_fun P_Fun p_amb P_Ambition p_shar P_Shared_Traits p_like P_Like_Level) ///
drop(architecture biochemphys businessecon education engineering fine_arts historyrel journaleng language law math medical_sc polisciintl socialwrk social_sc undecidedstud interest_corr same_race importance_race importance_religion ///
		asian black hispanic white ///
		age attr sinc intel fun amb shar like date go_out order_met p_age p_attr p_sinc p_intel p_fun p_amb p_shar p_like ///
		pref_attr pref_sinc pref_intel pref_fun pref_amb p_pref_attr  p_pref_sinc p_pref_intel p_pref_fun p_pref_amb p_pref_shar ///
		obc_fun_night obc_get_date obc_new_ppl obc_ser_rel obc_tosayso) ///
order(age attr sinc intel fun amb shar like date go_out order_met p_age p_attr p_sinc p_intel p_fun p_amb p_shar p_like) ///
addnotes(Standard Errors robust. race, field, and obc 'other' fields removed.)


* Not store regression results for airline analysis
eststo clear
