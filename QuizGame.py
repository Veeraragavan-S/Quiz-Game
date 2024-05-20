class QuixGame:
    print("Welcome to my console quiz(*.*)")

    play=input("Do you want to play? :) ")
    if play.lower().strip()== "yes":
        print("Okay! Lets go...")
    else:
        quit()
    
    score=0

    #Ques-1    
    answer=input("(Q1)-What does CPU stands for? ")
    if answer.lower().strip()=="central processing unit":
        print("Hurray! That's correct...way to go")
        score+=1
    else:
        print("Oops! That's wrong")
        
    #Ques-2
    answer=input("(Q2)-What does GPU stands for? ")
    if answer.lower().strip()=="graphics processing unit":
        print("Hurray! That's correct...way to go")
        score+=1
    else:
        print("Oops! That's wrong")
        
    #Ques-3
    answer=input("(Q3)-What does PSU stands for? ")
    if answer.lower().strip()=="power supply unit":
        print("Hurray! That's correct...way to go")
        score+=1
    else:
        print("Oops! That's wrong")
        
    #Ques-4   
    answer=input("(Q4)-What is the value of y \nx=1 \nwhile x<4: \n   y=x**2+1 \n   x+=2 ")
    if answer.strip()=="10":
        print("Hurray! That's correct...way to go")
        score+=1
    else:
        print("Oops! That's wrong")
        
    #Ques-5  
    answer=input("(Q5)-Which program in python is used to convert high level code to machine code?  ")
    if answer.lower().strip()=="interpreter":
        print("Hurray! That's correct...way to go")
        score+=1
    else:
        print("Oops! That's wrong")
        
    print("Your scored ", (score/5)*100 , "%")
    print("Thanks for playing....I hope you enjoy:) ")
        

        
