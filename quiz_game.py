print ("Welcome to my computer quiz!")
playing = input("Do you want to play? ").lower()

if playing != "yes":
     print("wrong answer")
     quit()
else:
     print("okay! let play :)")
     score = 0
answer = input("What does cpu stand for? ").lower()
if answer == "central processing unit":
     print("Correct answer")
     score+=1

else:
     print("incorrect answer")

answer = input("What does gpu stand for? ").lower()
if answer == "graphic processing unit":
     print("Correct answer")
     score+=1
else:
     print("incorrect answer")

answer = input("What does psu stand for? ").lower()
if answer == "power supply unit":
     print("Correct answer")
     score+=1
else:
     print("incorrect answer")

answer = input("What does ram stand for? ").lower()
if answer == "read access memory":
     print("Correct answer")
     score+=1
else:
     print("incorrect answer")

print("you got "+ str(score) + " question correct") 
print("you score is " + str((score/4)*100)+ "%.")



     
     