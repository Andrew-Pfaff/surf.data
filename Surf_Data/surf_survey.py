def surf_survey():
    survey_list = []
    
        #0 - overall quality (1-5 rating)
        #1 - power (1-5 rating)
        #2 - avg size (approx ft)
        #3 - max size (approx ft)
        #4 - choppyness (1-5 rating)
        #5 - rate of closeouts (1-5 rating)
        #6 - steepness (1-5 rating [1 close to 90 degrees 5 closer to 45])


    quality = input('Rate the overall quality of the surf. Input an integer value between 1 and 5, 1 being bad, 5 being good: ')
    survey_list.append(quality)

    power = input('')
    survey_list.append(power)

    avg_size = input('')
    survey_list.append(avg_size)

    max_size = input('')
    survey_list.append(max_size)    

    chop = input('')
    survey_list.append(chop)    

    closeout = input('')
    survey_list.append(closeout)

    steep = input('')
    survey_list.append(steep)




    return survey_list