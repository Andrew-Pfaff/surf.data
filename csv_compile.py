from csv import writer

import Time.time_compile as tc
import Surf_Data.surf_survey as ss
import Surf_Data.tidedata as td
import Surf_Data.wind as wind

#--CSV order key--
    #0.   date
    #1.   start_time
    #2.   end_time
    #3.   init_tide
    #4.   final_tide
    #5.   start_wind_speed
    #6.   end_wind_speed
    #7.   average_wind_speed
    #8.   start_wind_direction
    #9.   end_wind_direction
    #10.  mode_wind_direction
    # overall quality (1-5 rating)
    # power (1-5 rating)
    # avg size (approx ft)
    # max size (approx ft)
    # choppyness (1-5 rating)
    # rate of closeouts (1-5 rating)
    # steepness (1-5 rating [1 close to 90 degrees 5 closer to 45])



#get time for inputs
day_time = tc.timedate_list()



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

#3. init_tide
new_csv_row.append(tide_list[0])
#4. final_tide
new_csv_row.append(tide_list[1])



#run wind script
wind_list = wind.wind(day_time)

#5. start_wind_speed
new_csv_row.append(wind_list[0])
#6. end_wind_speed
new_csv_row.append(wind_list[1])
#7. average_wind_speed
new_csv_row.append(wind_list[2])
#8. start_wind_direction
new_csv_row.append(wind_list[3])
#9. end_wind_direction
new_csv_row.append(wind_list[4])
#10. mode_wind_direction
new_csv_row.append(wind_list[5])


#survey
survey_results = ss.surf_survey()
# - overall quality (1-5 rating)
new_csv_row.append(survey_results[0])
# - power (1-5 rating)
new_csv_row.append(survey_results[1])
# - avg size (approx ft)
new_csv_row.append(survey_results[2])
# - max size (approx ft)
new_csv_row.append(survey_results[3])
# - choppyness (1-5 rating)
new_csv_row.append(survey_results[4])
# - rate of closeouts (1-5 rating)
new_csv_row.append(survey_results[5])
# - steepness (1-5 rating [1 close to 90 degrees 5 closer to 45])
new_csv_row.append(survey_results[6])







#add to the csv
import csv
with open("sands.csv", "a", newline='') as fp:
    wr = csv.writer(fp)
    wr.writerow(new_csv_row)

print('Session added to sands.csv.')