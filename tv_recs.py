# Asks the question and checks if the answer is valid.
def ask_question(question):
   corect_answer = True
   while corect_answer:
        answer = input(question)
        if answer == "a" or answer == "b" or answer == "c":
            corect_answer = False
      
        else:
            print ("invalid answer")
      
    return answer 
d = {}
d ["aaa"] = "Nobody Wants This"
d ["aba"] = "The White Lotus"
d ["aca"] = "How to Die Alone"
d ["aab"] = "Emily in Paris"
d ["aac"] = "Brooklyn Nine-Nine"


 #print instructions
print (" Welcome to the TV Show Recomender. I will be asking you three questions based on your responses to the questions I will then pick a TV show best fit for you.")

 #Ask first question about the genre and store the answer  
answer1 = ask_question ("what kind of genre?")


# Ask second question about the streaming services used and store the answer.
answer2 = ask_question ("Where do you prefer to stream TV?")

#Ask third question about the number of seasons and store the answer.
answer3 = ask_question ("How many seasons?")

print (d[answer1 + answer2 + answer3])
