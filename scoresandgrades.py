import random

def grades(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: "+ str(score) +"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: "+ str(score) +"; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: "+ str(score) +"; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: "+ str(score) +" Your grade is A"
        else:
            print "You failed"
    print "End of program. Bye!"
    
grades(10)

