import Time.time_compile as tc
import Surf_Data.surf_survey as ss
import Surf_Data.tidedata as td


#--CSV order key--
#0. date
#1. start_time
#2. end_time
#3. init_tide
#4. final_tide
#5. 
#
#
#last will be the survey


#get inputs
day_time = tc.timedate_list()
survey_results = ss.surf_survey()


#create a new entry to the csv file
#a list is created and the data should be appended in the order shown in the key above
new_csv_row = []


#0. date
new_csv_row.append(day_time[0])

#1. start_time
new_csv_row.append(day_time[1])

#2. end_time
new_csv_row.append(day_time[2])


#run tide script
tide_list = td.tide(day_time)
init_tide = tide_list[0]
final_tide = tide_list[1]


#3. init_tide
new_csv_row.append(init_tide)
#4. final_tide
new_csv_row.append(final_tide)


print(new_csv_row)