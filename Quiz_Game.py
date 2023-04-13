print("Welcome to Quiz Game")

playing = input("Do you want to play?(yes/no) ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
life = 3
print('You have '+ str(life) + "\U00002665")

while life > 0:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit" :
        print('Correct!')
    else :
        print('Incorrect :| ')
        life -= 1
        print('You have '+ str(life) + "\U00002665")

    answer = input("What does GPU stand for? ")
    if answer.lower() == "graphics processing unit" :
        print('Correct!')
    else :
        print('Incorrect :| ')
        life -= 1
        print('You have '+ str(life) + "\U00002665")

    answer = input("What does RAM stand for? ")
    if answer.lower() == "random access memory" :
        print('Correct!')
    else :
        print('Incorrect :| ')
        life -= 1
        print('You have '+ str(life) + "\U00002665")
        if life == 0:
             break

    answer = input("What does PSU stand for? ")
    if answer.lower() == "power supply unit" :
        print('Correct!')
        break
    else :
        print('Incorrect :| ')
        life -= 1
        print('You have '+ str(life) + "\U00002665")
        if life == 0:
             break

if life > 0:
            print("You have WON! :)")
            quit()      
else: 
     print('You are a disappointment') 

