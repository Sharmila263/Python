import random
print("Welcome to the Guessing Number Game")
generated_num=random.randint(1,100)
attempts=5
print("you should have to guess a number between 1-100 in 5 atttempts")
while attempts>0:
    user_guess=int(input("Guess the number: "))
    if user_guess<1 or user_guess>100:
        print("Invalid choice")
        continue

    if user_guess>generated_num:
        print("Too High,You have",attempts-1,"attempts left")
    
    elif user_guess<generated_num:
        print("Too low,You have",attempts-1,"attempts left")
    
    else:
        print("you won!! the num is" ,generated_num)
        break
    attempts-=1
if attempts==0:
    print("you are out of chances,generated number is: ",generated_num)

    

        
