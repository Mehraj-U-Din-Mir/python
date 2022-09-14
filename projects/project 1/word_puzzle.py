import random
import copy
words=["python", "Mehraj","Mohsin","hello","print"]
score=0
display=" "
for i in range(0,5):
    print("Arrange the letters to form a valid word: ")
    word=random.sample(words,1)
    temp=copy.deepcopy(list(word))
    random.shuffle(word)
    display=''.join(temp)
    print(display)
    user_guess=input()
    if word==user_guess:
        score+=1
        print("correct")
    elif user_guess==" ":
        print("no input")
    else:
        score-=1
        print("wrong")
print("Net score is  :", score)