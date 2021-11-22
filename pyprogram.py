coursework = "English"
score_theory = 53
score_practical = 78

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50 or score_practical > 50):
        # Can't distinguish the error in Science: theory or Science: Practical
        print("Please check the input score for Science.")
    else: print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60 or score_practical > 40):
        # Can't distinguish the error in English: theory or English: Practical
        print("Please check the input score for English.")
    else: print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")