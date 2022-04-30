print('''
███▄▄▄▄    ▄██████▄      ███        ▄████████       ████████████
███▀▀▀██▄ ███    ███ ▀█████████▄   ███    ███       ██        ██
███   ███ ███    ███    ▀███▀▀██   ███    █▀        ██        ██
███   ███ ███    ███     ███   ▀  ▄███▄▄▄           ██        ██
███   ███ ███    ███     ███     ▀▀███▀▀▀       ██████    ██████
███   ███ ███    ███     ███       ███    █▄  ████████  ████████
███   ███ ███    ███     ███       ███    ███ ████████  ████████
 ▀█   █▀   ▀██████▀     ▄████▀     ██████████   ██▓▓      ████  
                                                                 
   ▄████████  ▄█  ███▄▄▄▄   ████████▄     ▄████████    ▄████████ 
  ███    ███ ███  ███▀▀▀██▄ ███   ▀███   ███    ███   ███    ███ 
  ███    █▀  ███▌ ███   ███ ███    ███   ███    █▀    ███    ███ 
 ▄███▄▄▄     ███▌ ███   ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀     ███▌ ███   ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███        ███  ███   ███ ███    ███   ███    █▄  ▀███████████ 
  ███        ███  ███   ███ ███   ▄███   ███    ███   ███    ███ 
  ███        █▀    ▀█   █▀  ████████▀    ██████████   ███    ███ 
                                                      ███    ███
================================================================''')
while True: #loop to repeat once notes printed
    while True: #loop to get usable scale input
        scaleType = input('Major or Minor scale? Q to Quit. ')
        scaleType = scaleType.lower() #makes scaleType lowercase to match variables
        if scaleType == 'major' or scaleType == 'minor':
            break #if usable input continue
        elif scaleType == 'q' or scaleType =='Q':
            quit()
        else:
            print('Please choose a scale listed.')
    print('You chose the', scaleType.capitalize(), 'scale.')        
    
    #checks for input scale type
    #Major Scale Dictionary     
    if scaleType == 'major': 
        major = {'C' : 'C, D, E, F, G, A, B, C', 'C#' : 'C#, D#, F, F#, G#, A#, C, C#', 'D' : 'D, E, F#, G, A, B, C#, D',
        'Eb' : 'Eb, F, G, Ab, Bb, C, D, Eb', 'E' : 'E, F#, G#, A, B, C#, D#, E', 'F' : 'F, G, A, Bb, C, D, E, F',
        'F#' : 'F#, G#, A#, B, C#, D#, F, F#', 'G' : 'G, A, B, C, D, E, F#, G', 'Ab' : 'Ab, Bb, C, D, Eb, F, G, A, Ab',
        'A' : 'A, B, C#, D, E, F#, G#, A', 'Bb' : 'Bb, C, D, Eb, F, G, A, Bb', 'B' : 'B, C#, D#, E, F#, G#, A#, B'}
        print(list(major.keys())) #unintentional double entundre
    
        while True:
            scale = input('Choose a Key from the list:')
            scale = scale.capitalize()#capitalize note leaving b/#
            if scale in major.keys():#check if input in the listed keys continue
                break
            else:
                print("Please choose a Key from the list.")
        #prints the scale and key chosen
        print('=================================================================')
        print('You Choose the', scale, scaleType, 'scale. The notes of the', scale, scaleType, 'scale are:')

        #Checks for input scale
        #Key of C etc
        if scale == 'C':
            #prints the value for the input key from the selected scale dictionary
            print(major ['C'])
        elif scale == 'C#':
            print(major ['C#'])
        elif scale == 'D':
            print(major ['D'])                  
        elif scale == 'Eb':
            print(major ['Eb'])     
        elif scale == 'E':
            print(major ['E']) 
        elif scale == 'F':
            print(major ['F']) 
        elif scale == 'F#':
            print(major ['F#']) 
        elif scale == 'G':
            print(major ['G']) 
        elif scale == 'Ab':
            print(major ['Ab']) 
        elif scale == 'A':
            print(major ['A'])
        elif scale == 'Bb':
            print(major ['Bb']) 
        elif scale == 'B':
            print(major ['B'])

    #Minor Scale Dictionary
    elif scaleType == 'minor': 
        minor = {'C' : 'C, D, Eb, F, G, Ab, Bb, C',  'C#' : 'C#, D#, E, F#, G#, A, B, C#', 'D' : 'D, E, F, G, A, Bb, C, D', 
        'Eb' : 'Eb, F, Gb, Ab, Bb, Cb, Db, Eb', 'E' : 'E, F#, G, A, B, C, D, E', 'F' : 'F, G, Ab, Bb, C, Db, Eb, F', 
        'F#' : 'F#, G#, A, B, C#, D, E, F#', 'G' : 'G, A, Bb, C, D, Eb, F, G', 'Ab' : 'Ab, Bb, Cb, Db, Eb, Fb, Gb, Ab', 
        'A' : 'A, B, C, D, E, F, G, A', 'Bb' : 'Bb, C, Db, Eb, F, Gb, Ab, Bb', 'B' : 'B, C#, D, E, F#, G, A, B'}
        print(list(minor.keys()))

        while True: #loop to get usable input
            scale = input('Choose a Key from the list:')
            scale = scale.capitalize()#capitalize note leaving b/#
            if scale in minor.keys():#check if input in the listed keys continue
                break
            else:
                print("Please choose a Key from the list.")
        print('=================================================================')
        print('You Choose the', scale, scaleType, 'scale. The notes of the', scale, scaleType, 'scale are:')
    
        if scale == 'C':
            print(minor ['C'])
        elif scale == 'C#':
            print(minor ['C#'])
        elif scale == 'D':
            print(minor ['D'])
        elif scale == 'Eb':
            print(minor ['Eb'])
        elif scale == 'E':
            print(minor ['E'])
        elif scale == 'F':
            print(minor ['F'])
        elif scale == 'F#':
            print(minor ['F#'])
        elif scale == 'G':
            print(minor ['G'])
        elif scale == 'Ab':
            print(minor ['Ab'])
        elif scale == 'A':
            print(minor ['A'])
        elif scale == 'Bb':
            print(minor ['Bb'])
        elif scale == 'B':
            print(minor ['B'])
    print('=================================================================')