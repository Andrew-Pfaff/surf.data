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
    Error = True
    while Error == True:
        try:
            x = int(quality)
            if x > 0 and x < 6:
                Error = False
            else: 
                print('Invalid input type.')
                quality = input('Rate the overall quality of the surf. Input an integer value between 1 and 5, 1 being bad, 5 being good: ')
        except:
            print('Invalid input type.')
            quality = input('Rate the overall quality of the surf. Input an integer value between 1 and 5, 1 being bad, 5 being good: ')
    survey_list.append(quality)

    
    power = input('Rate the power of the surf. Input an integer value between 1 and 5, 1 being soft, 5 being strong:')
    Error = True
    while Error == True:
        try:
            x = int(power)
            if x > 0 and x < 6:
                Error = False
            else: 
                print('Invalid input type.')
                power = input('Rate the power of the surf. Input an integer value between 1 and 5, 1 being soft, 5 being strong:')
        except:
            print('Invalid input type.')
            power = input('Rate the power of the surf. Input an integer value between 1 and 5, 1 being soft, 5 being strong:')
    survey_list.append(power)

    
    avg_size = input('Approximate the average size of the surf in feet (height of the face): ')
    Error = True
    while Error == True:
        try:
            x = float(avg_size)
            if type(x) == float:
                Error = False
            else: 
                print('Invalid input type.')
                avg_size = input('Approximate the average size of the surf in feet (height of the face): ')
        except:
            print('Invalid input type.')
            avg_size = input('Approximate the average size of the surf in feet (height of the face): ')
    survey_list.append(avg_size)

    
    max_size = input('Approximate the maximum size of the surf in feet (height of the face): ')
    Error = True
    while Error == True:    
        try: 
            x = float(max_size)
            if type(x) == float:
                Error = False
            else: 
                print('Invalid input type.')
                max_size = input('Approximate the maximum size of the surf in feet (height of the face): ')
        except:
            print('Invalid input type.')
            max_size = input('Approximate the maximum size of the surf in feet (height of the face): ')
    survey_list.append(max_size)    

    
    chop = input('Rate the choppyness of the surf. Input an integer value between 1 and 5, 1 being glassy, 5 being very choppy:')
    Error = True
    while Error == True:
        try:
            x = int(chop)
            if x > 0 and x < 6:
                Error = False
            else: 
                print('Invalid input type.')
                chop = input('Rate the choppyness of the surf. Input an integer value between 1 and 5, 1 being glassy, 5 being very choppy:')
        except:
            print('Invalid input type.')
            chop = input('Rate the choppyness of the surf. Input an integer value between 1 and 5, 1 being glassy, 5 being very choppy:')
    survey_list.append(chop)    

    
    closeout = input('Rate the rate at which the waves were closing out.  Input an integer value between 1 and 5, 1 being slowly, 5 being very quickly:')
    Error = True
    while Error == True:
        try:
            x = int(closeout)
            if x > 0 and x < 6:
                Error = False
            else: 
                print('Invalid input type.')
                closeout = input('Rate the rate at which the waves were closing out. Input an integer value between 1 and 5, 1 being slowly, 5 being very quickly:')
        except:
            print('Invalid input type.')
            closeout = input('Rate the rate at which the waves were closing out. Input an integer value between 1 and 5, 1 being slowly, 5 being very quickly:')
    survey_list.append(closeout)

    
    steep = input('Rate the steepness of the waves. Input an integer value between 1 and 5, 1 being close to 90 degrees, 5 being closer to 45])')
    Error = True
    while Error == True:
        try:
            x = int(steep)
            if x > 0 and x < 6:
                Error = False
            else: 
                print('Invalid input type.')
                steep = input('Rate the steepness of the waves. Input an integer value between 1 and 5, 1 being close to 90 degrees, 5 being closer to 45])')
        except:
            print('Invalid input type.')
            steep = input('Rate the steepness of the waves. Input an integer value between 1 and 5, 1 being close to 90 degrees, 5 being closer to 45])')
    survey_list.append(steep)


    return survey_list

y = surf_survey()
print(y)