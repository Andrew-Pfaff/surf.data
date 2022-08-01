import Time.time_compile as tc
import Surf_Data.surf_survey as ss
import Surf_Data.tidedata as td


#CSV order
#0. date
#1. start_time
#2. end_time
#3. init_tide
#4. final_tide
#5. 

new_csv_row = []

day_time = tc.timedate_list()


tide_list = td.tide(day_time)
init_tide = tide_list[0]
final_tide = tide_list[1]

survey_results = ss.surf_survey()