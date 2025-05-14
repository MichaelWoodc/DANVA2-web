## Here's how we work with our time stuff
trialDict = {}
trialResponses = {}
dictIndex = 0
trialIndex = 0
danvasubtest = 'Adult' # The default test if no selection is made, gets altered when drop select is changed
data_dict = {}
stimsList = {}
correctAnswers = {}
incorrectAnswers = {}
errorList = []
NamesCorrectAnswers = {}
intensity = ''
gender = ''
genderOfAnswer = ''
intensityOfAnswer = ''
correctAnswerForString = ''
currentAnswer = 0

highIntensityErrors = 0
lowIntensityErrors = 0
errorList = []
skippedErrors = 0
errorsByMisjudgement = 0
totalErrors = 0
happyHighIntensityErrors = 0
happyLowIntensityErrors = 0
sadHighIntensityErrors = 0
sadLowIntensityErrors = 0
angryHighIntensityErrors = 0
angryLowIntensityErrors = 0
fearfulHighIntensityErrors = 0
fearfulLowIntensityErrors = 0
happyErrors = 0
sadErrors = 0
angryErrors = 0
fearfulErrors = 0
lowIntensityErrors = 0
misattributedHappySad = 0
misattributedHappyAngry = 0
misattributedHappyFearful = 0
misattributedSadHappy = 0
misattributedSadAngry = 0
misattributedSadFearful = 0
misattributedAngryHappy = 0
misattributedAngrySad = 0
misattributedAngryFearful = 0
misattributedFearfulHappy = 0
misattributedFearfulSad = 0
misattributedFearfulAngry = 0
maleHappyErrors = 0
maleSadErrors = 0
maleAngryErrors = 0
maleFearfulErrors = 0
maleTotalErrors = 0
femaleHappyErrors = 0
femaleSadErrors = 0
femaleAngryErrors = 0
femaleFearfulErrors = 0
femaleTotalErrors = 0
stimuliEndTime = 0

dictionaryloop = 0
dictionaryloop2 = 0

stimuliStart = 0
displayTime = 2  # NOTE: Not sure if this is what I changed
stimuliEndTime = 1
# This is to set the number of the trial for scoring the right data

dictionarydefinitions = ["participant","age","skippedErrors","totalErrors","totalerrors","happyHighIntensityErrors","happyLowIntensityErrors",
                         "sadHighIntensityErrors","sadLowIntensityErrors","angryHighIntensityErrors",
                         "angryLowIntensityErrors","fearfulHighIntensityErrors","fearfulLowIntensityErrors",
                         "happyErrors","sadErrors","angryErrors","fearfulErrors","lowIntensityErrors",
                         "highIntensityErrors","misattributedHappySad","misattributedHappyAngry",
                         "misattributedHappyFearful","misattributedSadHappy","misattributedSadAngry",
                         "misattributedSadFearful","misattributedAngryHappy","misattributedAngrySad",
                         "misattributedAngryFearful","misattributedFearfulHappy","misattributedFearfulSad",
                         "misattributedFearfulAngry","errorsByMisjudgement","danvasubtest","maleHappyErrors",
                         "maleSadErrors","maleAngryErrors","maleFearfulErrors","maleTotalErrors",
                         "femaleHappyErrors","femaleSadErrors","femaleAngryErrors","femaleFearfulErrors","femaleTotalErrors",
                         "totalErrors1","totalErrors2","happyErrors2","sadErrors2","angryErrors2","fearfulErrors2",]



def createDictionary():
    global dictionaryloop, skippedErrors, totalErrors, data_dict, errorList,NamesCorrectAnswers, trialDict, incorrectAnswers, correctAnswers, stimsList, correctAnswerForString, femaleTotalErrors, maleTotalErrors
    global highIntensityErrors, lowIntensityErrors, happyErrors, sadErrors, angryErrors, fearfulErrors
    global happyHighIntensityErrors, happyLowIntensityErrors, sadHighIntensityErrors, sadLowIntensityErrors, angryHighIntensityErrors, angryLowIntensityErrors, fearfulHighIntensityErrors, fearfulLowIntensityErrors
    global femaleHappyErrors, femaleSadErrors, femaleAngryErrors, femaleFearfulErrors
    global maleHappyErrors, maleSadErrors, maleAngryErrors, maleFearfulErrors, misattributedHappySad, misattributedHappyAngry, misattributedHappyFearful, misattributedSadHappy, misattributedSadAngry, misattributedSadFearful, misattributedAngryHappy, misattributedAngrySad, misattributedAngryFearful, misattributedFearfulHappy, misattributedFearfulSad, misattributedFearfulAngry
    data_dict = {}
    stimsList = {}
    incorrectAnswers = {}
    errorList = []
    NamesCorrectAnswers = {}
    genderOfAnswer = ''
    intensityOfAnswer = ''
    totalerrors = totalErrors
    
    for i in trialDict:
        # Let's do the basic things first:
        stimsList['stim' + str(dictionaryloop)] = (trialDict[dictionaryloop]['stimFile'])
        
        if trialDict[dictionaryloop]['response'] == '0':
            skippedErrors = skippedErrors + 1
        
        # Let's concact a string to fill in the correct answer with intensity and gender column, we'll start with emotion
        if trialDict[dictionaryloop]['correctAnswer'] == '1':
            correctAnswerForString = 'Happy '
        elif trialDict[dictionaryloop]['correctAnswer'] == '2':
            correctAnswerForString = 'Sad '
        elif trialDict[dictionaryloop]['correctAnswer'] == '3':
            correctAnswerForString = 'Angry '
        elif trialDict[dictionaryloop]['correctAnswer'] == '4':
            correctAnswerForString = 'Fearful '
            
        # Now let's grab the intensity
        if  trialDict[dictionaryloop]['intensity'] == '1':
            intensityOfAnswer = 'Low '
        elif trialDict[dictionaryloop]['intensity'] == '2':
            intensityOfAnswer = 'High '
        else:
            pass
        
        # Now let's grab the gender:
        if  trialDict[dictionaryloop]['stimuliGender'] == '1':
            genderOfAnswer = 'Female'
        elif trialDict[dictionaryloop]['stimuliGender'] == '2':
            genderOfAnswer = 'Male'
        else:
            pass
        
        # Now let's plug that into the PDF
        correctAnswers['correctAnswer'+ str(dictionaryloop)] = (correctAnswerForString) + (intensityOfAnswer) + (genderOfAnswer)

        if trialDict[dictionaryloop]['response'] != trialDict[dictionaryloop]['correctAnswer']:
            totalErrors = totalErrors + 1
            response = int(trialDict[dictionaryloop]['response'])
            correctAnswerKey = trialDict[dictionaryloop]['correctAnswer']
            
            if trialDict[dictionaryloop]['stimuliGender'] == '2':
                maleTotalErrors = maleTotalErrors + 1
            elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                femaleTotalErrors = femaleTotalErrors + 1
            else:
                pass
            
            if  trialDict[dictionaryloop]['intensity'] == '1':
                lowIntensityErrors = lowIntensityErrors + 1
            elif trialDict[dictionaryloop]['intensity'] == '2':
                highIntensityErrors = highIntensityErrors + 1
            else:
                pass        
            
            if correctAnswerKey == '1':
                happyErrors = happyErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    happyLowIntensityErrors = happyLowIntensityErrors + 1
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    happyHighIntensityErrors = happyHighIntensityErrors + 1
                else:
                    pass        

                if response == 2:
                    misattributedHappySad = misattributedHappySad + 1
                elif response == 3:
                    misattributedHappyAngry = misattributedHappyAngry + 1
                elif response == 4:
                    misattributedHappyFearful = misattributedHappyFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleHappyErrors = maleHappyErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleHappyErrors = femaleHappyErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '2':
                sadErrors = sadErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    sadLowIntensityErrors = sadLowIntensityErrors + 1     
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    sadHighIntensityErrors = sadHighIntensityErrors + 1                
                else:
                    pass

                if response == 1:
                    misattributedSadHappy = misattributedSadHappy + 1
                elif response == 3:
                    misattributedSadAngry = misattributedSadAngry + 1
                elif response == 4:
                    misattributedSadFearful = misattributedSadFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleSadErrors = maleSadErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleSadErrors = femaleSadErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '3':
                angryErrors = angryErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    angryLowIntensityErrors = angryLowIntensityErrors + 1        
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    angryHighIntensityErrors = angryHighIntensityErrors + 1                
                else:
                    pass
                
                if response == 1:
                    misattributedAngryHappy = misattributedAngryHappy + 1
                elif response == 2:
                    misattributedAngrySad = misattributedAngrySad + 1
                elif response == 4:
                    misattributedAngryFearful = misattributedAngryFearful + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleAngryErrors = maleAngryErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleAngryErrors = femaleAngryErrors + 1
                else: 
                    pass
                
            if correctAnswerKey == '4':
                fearfulErrors = fearfulErrors + 1
                if  trialDict[dictionaryloop]['intensity'] == '1':
                    fearfulLowIntensityErrors = fearfulLowIntensityErrors + 1
                elif trialDict[dictionaryloop]['intensity'] == '2':
                    fearfulHighIntensityErrors = fearfulHighIntensityErrors + 1
                else:
                    pass
                
                if response == 1:
                    misattributedFearfulHappy = misattributedFearfulHappy + 1
                elif response == 2:
                    misattributedFearfulSad = misattributedFearfulSad + 1
                elif response == 3:
                    misattributedFearfulAngry = misattributedFearfulAngry + 1
                else:
                    pass
                
                if trialDict[dictionaryloop]['stimuliGender'] == '2':
                    maleFearfulErrors = maleFearfulErrors + 1
                elif trialDict[dictionaryloop]['stimuliGender'] == '1':
                    femaleFearfulErrors = femaleFearfulErrors + 1
                else:
                    pass
            else:
                pass

            if response == 1:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Happy'        
            elif response == 2:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Sad'
            elif response == 3:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Angry'
            elif response == 4:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Fearful'
            else:
                incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Skipped'
        dictionaryloop = dictionaryloop + 1

def createPDF():
    global dictionaryloop, dictionaryloop2, correctAnswers, age, participant, errorsByMisjudgement
    dictionaryloop2 = 0
    totalerrors = totalErrors
    age = ageInput.get_value()
    participant = participantInput.get_value()
    errorsByMisjudgement = totalErrors - skippedErrors
    
    totalErrors1 = totalerrors
    totalErrors2 = totalerrors
    happyErrors2 = happyErrors
    sadErrors2 = sadErrors
    angryErrors2 = angryErrors
    fearfulErrors2 = fearfulErrors

    for i in (dictionarydefinitions):
        data_dict [dictionarydefinitions[dictionaryloop2]] = (eval(dictionarydefinitions[dictionaryloop2]))
        dictionaryloop2 = dictionaryloop2 + 1

    data_dict.update(stimsList)
    data_dict.update(expInfo)
    data_dict.update(incorrectAnswers)
    data_dict.update(correctAnswers)

    filename = expInfo['date'] + participant + danvasubtest + '.pdf'
    sanitized_filename = sanitize_filename(filename)
    filepath = 'reports/'+sanitized_filename

    fillpdfs.write_fillable_pdf('src/pdfMagic/completed.pdf', (filepath), data_dict, flatten=False) # was fillpdfs.write_fillable_pdf('src/pdfMagic/completed.pdf', 'reports/completed.pdf', data_dict, flatten=False)


    cur_path = os.getcwd()
    print('current path',cur_path)

    new_path = os.path.relpath(filepath, cur_path)
    print('new path',new_path)
    openAttempts = 0
    number_of_allowed_attempts = 1000
    while True:
        print('Attempt:',openAttempts)
        try:
            os.startfile(new_path)
            break
        except:
            openAttempts += 1
            
        if openAttempts > number_of_allowed_attempts:
            break
        
