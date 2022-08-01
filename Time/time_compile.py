import Time.timedate_scripts as tds


#Compile a list with all of the formats that will be needed by other commands.
#This way we can call to this list in any scripts that require a time or date


def timedate_list():
    td_list = []
    
    #0
    #date in YYYYMMDD form
    day = tds.getdate()
    td_list.append(day)

    #1
    #start time in HH:MM form (24 hours, requires a 0 for single digit numbers, i.e. 08)
    stime = tds.start_time()
    td_list.append(stime)

    #2
    #end time in HH:MM form (24 hours, requires a 0 for single digit numbers, i.e. 08)
    etime = tds.end_time()
    td_list.append(etime)

    #3 
    #date in YYYY-MM-DD form
    dashed_date = tds.date_dash(day)
    td_list.append(dashed_date)


    return td_list